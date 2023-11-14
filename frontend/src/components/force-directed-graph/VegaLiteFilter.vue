<template>
  <div class="boundray">
    <svg
      viewBox="0 0 1024 1024"
      xmlns="http://www.w3.org/2000/svg"
      class="narrow-icon"
      @click="$emit('hideMoreBox')"
    >
      <path
        d="M320 885.333333c-8.533333 0-17.066667-4.266667-23.466667-10.666666-12.8-12.8-10.666667-34.133333 2.133334-44.8L654.933333 512 298.666667 194.133333c-12.8-10.666667-14.933333-32-2.133334-44.8 10.666667-12.8 32-14.933333 44.8-2.133333l384 341.333333c6.4 6.4 10.666667 14.933333 10.666667 23.466667 0 8.533333-4.266667 17.066667-10.666667 23.466667l-384 341.333333c-6.4 6.4-12.8 8.533333-21.333333 8.533333z"
      ></path>
    </svg>
    <BaseCard mode="flat" class="content-box">
      <div class="content">
        <div v-for="(insight, index) in currentPageData" class="insight-box">
          <div class="info-box">
            <label>Score</label>
            <div class="score-box">
              <div class="font-box">
                {{ insight["insight-score"].toFixed(3) }}
              </div>

              <svg
                @click="setInsightIndex(index)"
                viewBox="0 0 1024 1024"
                xmlns="http://www.w3.org/2000/svg"
                :class="[
                  'check-icon',
                  { 'check-icon-active': selectedIndex === index },
                ]"
              >
                <path
                  d="M433.1 657.7c12.7 17.7 39 17.7 51.7 0l210.6-292c3.8-5.3 0-12.7-6.5-12.7H642c-10.2 0-19.9 4.9-25.9 13.3L459 584.3l-71.2-98.8c-6-8.3-15.6-13.3-25.9-13.3H315c-6.5 0-10.3 7.4-6.5 12.7l124.6 172.8z"
                ></path>
                <path
                  d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32z m-40 728H184V184h656v656z"
                ></path>
              </svg>
            </div>
            <label>Type</label>
            <div class="font-box">
              {{ insight["insight-type"] }}
            </div>
          </div>

          <div id="vega-lite-filtered-container" ref="vegaContainers"></div>
        </div>
      </div>
      <el-pagination
        small
        :page-size="pageSize"
        layout="prev, pager, next"
        :total="insightList.length"
        v-model:current-page="currentPage"
        class="pagination"
      />
    </BaseCard>
  </div>
</template>

<script>
export default {
  props: ["insightList", "insightIndex"],
  data() {
    return {
      selectedIndex: 0,
      currentIndex: null,
      currentPage: 1,
      pageSize: 3,
      currentPageData: null,
    };
  },
  watch: {
    currentPage(newVal) {
      this.currentPageData = this.getPageDataByNumber(newVal);
    },
    currentPageData(newVal, oldVal) {
      this.$nextTick(() => {
        this.selectedIndex = this.convertSelectedIndex(this.currentIndex);
        this.$refs.vegaContainers.forEach((container, index) => {
          this.drawVegaLite(container, newVal, index);
        });
      });
    },
    // selectedIndex(newVal) {
    //   if (this.view) this.view.finalize();
    //   this.drawVegaLite(newVal);
    // },
    // insightList() {
    //   this.currentIndex = this.insightIndex;
    //   if (this.selectedIndex !== this.currentIndex) {
    //     this.selectedIndex = this.currentIndex;
    //   } else {
    //     this.view.finalize();
    //     this.drawVegaLite(this.selectedIndex);
    //   }
    // },
  },
  methods: {
    getPageDataByNumber(pageNum) {
      const start = this.pageSize * (pageNum - 1);
      let end = start + this.pageSize;
      // if (end > this.insightList.length) end = this.insightList.length;
      return this.insightList.slice(start, end);
    },
    drawVegaLite(containerRef, data, index) {
      const that = this;
      const container = d3.select(containerRef);
      container.selectAll("*").remove();

      let yourVlSpec = JSON.parse(data[index]["vega-lite"]);
      yourVlSpec["width"] = "container";
      yourVlSpec["height"] = "container";

      vegaEmbed(container.node(), yourVlSpec).then((result) => {
        const canvas = container.select("canvas");

        container.select("div").remove();
        container.select("details").remove();
        container.node().appendChild(canvas.node());
        result.view.finalize();
      });
    },
    setInsightIndex(index) {
      const selectedIndexOrigin = this.invertSelectedIndex(index);
      if (selectedIndexOrigin !== this.currentIndex) {
        this.$emit("insightIndexChange", selectedIndexOrigin);
        this.currentIndex = selectedIndexOrigin;
        this.selectedIndex = this.convertSelectedIndex(selectedIndexOrigin);
      }
    },
    convertSelectedIndex(origin) {
      const pageNumber = parseInt(origin / this.pageSize);
      if (pageNumber + 1 === this.currentPage) {
        return origin % this.pageSize;
      } else {
        return -1;
      }
    },
    invertSelectedIndex(origin) {
      return (this.currentPage - 1) * this.pageSize + origin;
    },
  },
  created() {
    this.currentIndex = this.insightIndex;
    this.currentPageData = this.getPageDataByNumber(this.currentPage);
  },
  mounted() {
    // this.$refs.vegaContainers.forEach((container, index) => {
    //   this.drawVegaLite(container, this.currentPageData, index);
    // });
  },
  beforeUnmount() {
    // if (this.view) {
    //   this.view.finalize();
    // }
  },
};
</script>

<style scoped>
.boundray {
  width: 18vw;
  height: 100%;
  padding-bottom: 0.3vw;
  z-index: 1;
}
.narrow-icon {
  position: absolute;
  top: 0;
  right: 18vw;
  width: 2rem;
  height: 2rem;
  fill: #545b77;
  cursor: pointer;
  border-radius: 0.2rem 0 0.2rem 0.2rem;
  border: 0.1rem solid rgba(0, 0, 0, 0.2);
  border-right: none;
  transition: background-color 0.3s, fill 0.3s;
}

.narrow-icon:active,
.narrow-icon:hover {
  background-color: #545b77;
  fill: #fff;
}

.content-box {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;

  background-color: #fff;
  border-radius: 0 0.2rem 0.2rem 0.2rem;
}
.content {
  flex: 93%;
  display: flex;
  flex-direction: column;
}
.insight-box {
  flex: 0 33.5%;
  display: flex;
  flex-direction: column;
  gap: 0.2vw;
  padding: 0 1vw;
  padding-top: 0.4vw;
  border-bottom: 0.1rem solid rgba(0, 0, 0, 0.2);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.insight-box:first-child {
  padding-top: 0.5vw;
}
.insight-box:last-child {
  border: none;
}
.insight-box:hover {
  box-shadow: -0.1rem 0.3rem 0.6rem 0.1rem rgba(0, 0, 0, 0.2);
}
.info-box {
  flex: 0.2;
  display: grid;
  grid-template-columns: 0.2fr 0.8fr;
  align-items: center;
  font-size: 1.1rem;
  font-weight: bold;
}

.font-box {
  font-size: 1.1rem;
  font-weight: normal;
}

.score-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
#vega-lite-filtered-container {
  flex: 0.8;
}
.check-icon {
  cursor: pointer;

  width: 2rem;
  height: 2rem;

  border-radius: 0.2rem;
  fill: #545b77;
  background-color: #fff;
  transition: background-color 0.2s, fill 0.2s;
}

.check-icon:hover,
.check-icon:active {
  background-color: #545b77;
  fill: #fff;
}
.check-icon-active {
  background-color: #545b77;
  fill: #fff;
}
.pagination {
  justify-content: space-evenly;
  flex: 0 7%;
}
</style>
<!-- global style -->
<style lang="less">
.pagination {
  --el-color-primary: #545b77;
  --el-text-color-primary: #888;

  .el-pager {
    justify-content: center;
    flex: 0.8;
  }
}
</style>
