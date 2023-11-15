<template>
  <div
    class="container"
    v-loading="loading || loading_ph"
    element-loading-text="Computing..."
  >
    <nav class="navBar">
      <div class="nav-title">CoInsight</div>
      <div class="nav-button-box">
        <div class="uploader">
          <SvgIcon iconName="upload" class="nav-icon" @click="triggerFileInput">
          </SvgIcon>
          <input
            type="file"
            ref="fileInput"
            @change="handleFileChange"
            accept=".xls,.xlsx"
            style="display: none"
          />
        </div>

        <SvgIcon
          iconName="photo"
          class="nav-icon"
          @click="togglePhotoMode"
          :class="{ 'active-btn': photoMode }"
        ></SvgIcon>
      </div>
    </nav>
    <div
      :class="['content-box', { notEditMode: !editMode }]"
      @transitionend="handleTransitionEnd"
      :key="refreshFlag"
    >
      <div class="loading-mask" v-if="error.state || error_ph.state">
        <div class="introduction">
          <div>Upload <strong>.xls/.xlsx</strong> files now</div>

          <div>and start exploring <em>Insight Stories</em>!</div>
        </div>
      </div>

      <div :class="['control-panel-box']" v-show="editMode">
        <BaseCard mode="flat" class="control-panel" v-show="animationDone">
          <div class="button-box-content">
            <el-tabs
              v-model="controlPanelMode"
              :stretch="true"
              class="config-panel-tab"
            >
              <el-tab-pane
                label="Config"
                name="base"
                :disabled="photoMode"
              ></el-tab-pane>
              <el-tab-pane label="Table" name="table"></el-tab-pane>
            </el-tabs>
          </div>
          <div class="control-panel-content" v-show="animationDone">
            <div class="base-mode" v-show="controlPanelMode === 'base'">
              <div class="button-box">
                <div>
                  <svg
                    viewBox="0 0 1024 1024"
                    xmlns="http://www.w3.org/2000/svg"
                    @click="restart"
                    class="panel-icon"
                  >
                    <path
                      d="M512 938.666667C276.352 938.666667 85.333333 747.648 85.333333 512S276.352 85.333333 512 85.333333s426.666667 191.018667 426.666667 426.666667-191.018667 426.666667-426.666667 426.666667z m205.653333-210.090667a298.666667 298.666667 0 1 0-79.018666 54.016l-41.6-74.88A213.333333 213.333333 0 1 1 725.333333 512h-128l120.32 216.576z"
                    ></path>
                  </svg>
                </div>
                <div>
                  <svg
                    viewBox="-38 -38 1062 1062"
                    xmlns="http://www.w3.org/2000/svg"
                    @click="stop"
                    class="panel-icon"
                  >
                    <path
                      d="M512 0C229.216 0 0 229.216 0 512s229.216 512 512 512 512-229.216 512-512S794.784 0 512 0z m0 928C282.24 928 96 741.76 96 512S282.24 96 512 96s416 186.24 416 416-186.24 416-416 416z m-192-608h384v384H320z"
                    ></path>
                  </svg>
                </div>
              </div>
              <StatisticsGraph ref="controlGraph"></StatisticsGraph>
            </div>
            <div class="table-mode" v-if="controlPanelMode === 'table'">
              <MiniTable></MiniTable>
            </div>
          </div>
        </BaseCard>
      </div>

      <div class="force-graph-box">
        <transition
          name="forceAnimation"
          mode="out-in"
          @after-leave="handleForceTransitionEnd"
        >
          <ForceDirectedGraph
            ref="forceGraph"
            v-show="!photoMode"
          ></ForceDirectedGraph>
        </transition>

        <TreeGraph v-if="photoMode && transitionEnd"></TreeGraph>
      </div>
    </div>
  </div>
</template>
<script>
import ForceDirectedGraph from "@/components/force-directed-graph/ForceDirectedGraph.vue";
import StatisticsGraph from "@/components/control-panel-graph/StatisticsGraph.vue";
import MiniTable from "@/components/control-panel-graph/MiniTable.vue";
import TreeGraph from "@/components/tree-graph/TreeGraph.vue";
import { Tools } from "@element-plus/icons-vue";
export default {
  components: {
    ForceDirectedGraph,
    StatisticsGraph,
    MiniTable,
    TreeGraph,
    Tools,
  },
  data() {
    return {
      count: 0,
      refreshFlag: false,
      editMode: true,
      animationDone: true,
      controlPanelMode: "base",
      photoMode: false,
      transitionEnd: false,
    };
  },
  computed: {
    loading_ph() {
      return this.$store.getters["tree/loading"];
    },
    error_ph() {
      return this.$store.getters["tree/error"];
    },
    loading() {
      return this.$store.getters["force/loading"];
    },

    error() {
      return this.$store.getters["force/error"];
    },
  },
  watch: {
    error(newVal) {
      if (newVal.state) {
        ElMessage.error(`Error: ${newVal.message}`);
        setTimeout(() => ElMessage.error("Please reload again"), 500);
      }
      if (!newVal.state) {
        ElMessage.success(`Calculation complete`);
      }
    },
    error_ph(newVal) {
      if (newVal.state) {
        ElMessage.error(`Error: ${newVal.message}`);
        setTimeout(() => ElMessage.error("Please reload again"), 500);
      }
      if (!newVal.state) {
        ElMessage.success(`Calculation complete`);
      }
    },
  },

  methods: {
    handleForceTransitionEnd() {
      this.transitionEnd = true;
    },
    handleFileChange() {
      const file = event.target.files[0];
      if (file) {
        // 限制为 .xls / .xlsx 类型
        const isExcel =
          file.type ===
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" ||
          file.type === "application/vnd.ms-excel";

        if (!isExcel) {
          ElMessage.warning(`Incorrect file type, please upload again`);
          return;
        }

        this.refreshFlag = true;

        this.$nextTick(() => {
          this.editMode = true;
          this.refreshFlag = false;
          this.photoMode = false;
          this.controlPanelMode = "base";
          // 刷新2个vuex模块的数据，以便2个组件重新加载
          this.$store.commit("force/setFocusState", null);
          this.$store.commit("force/setAllStatesData", null);
          this.$nextTick(() => {
            this.$store.dispatch("force/uploadData", file);
          });
        });
      }
    },

    triggerFileInput() {
      this.$refs.fileInput.value = null;
      this.$refs.fileInput.click();
    },
    stop() {
      this.$refs.forceGraph.simStop();
    },
    restart() {
      this.$refs.forceGraph.restart(
        false,
        this.$refs.forceGraph.focusState,
        null
      );
    },
    toggleEditMode() {
      if (!this.error.state) {
        this.animationDone = false;
        this.editMode = !this.editMode;
      }
    },
    togglePhotoMode() {
      if (!this.error.state) {
        this.transitionEnd = false;
        this.photoMode = !this.photoMode;
        if (this.photoMode) {
          this.$refs.forceGraph.getTreeInfo();

          this.controlPanelMode = "table";
        } else {
          this.$refs.forceGraph.resetTableHighlight();
          this.$refs.forceGraph.simulationRestart(
            this.$refs.forceGraph.globalSimulation
          );
        }
      }
    },

    handleTransitionEnd(event) {
      if (event.propertyName === "grid-template-columns") {
        this.animationDone = true;
      }
    },
  },
};
</script>
<style scoped lang="scss">
.container {
  height: 100%;
  width: 100%;
  /* background: linear-gradient(#fff, #f8f8f8); */
  /* background-color: #fafafa; */
  background-color: #fff;

  @include flex-box(column);
  gap: 0.4vw;
  .navBar {
    flex: 0 1 5%;
    max-height: 5%;

    width: 100%;
    box-shadow: 0rem 0.1rem 0.2rem 0rem rgba(0, 0, 0, 0.2);
    /* margin-bottom: 0.4vw; */
    /* transition: box-shadow 0.3s; */
    z-index: 5;

    background-color: #fff;
    @include flex-box(row);
    align-items: center;
    justify-content: space-between;
    padding: 0 1vw;
    .nav-title {
      font-size: 2rem;
      font-weight: bold;
      color: #545b77;
      /* font-style: italic; */
    }
    .nav-button-box {
      height: 100%;

      @include flex-box(row);
      gap: 0.5vw;
      padding: 0.3vh;

      .nav-icon {
        height: 2.6rem;
        width: 2.6rem;

        cursor: pointer;
        border: none;
        fill: #545b77;
        border-radius: 0.2rem;
        transition: background-color 0.3s ease-out, fill 0.3s ease-out,
          color 0.3s ease-out, filter 0.3s ease-out;
        color: #fff;
        filter: none;

        &.active-btn {
          /* background-color: #545b77; */
          /* fill: #fff; */
          color: #fff;
          filter: url(#inset-shadow);
        }
      }

      .nav-icon:hover,
      .nav-icon:active {
        background-color: #858eb5;
        fill: #fff;
        color: transparent;
        filter: none;
      }
      .uploader {
      }
    }
  }
}

.loading-mask {
  position: absolute;
  z-index: 9;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  /* background-color: rgba(255, 255, 255, 0.8); */
  background-image: linear-gradient(
      to bottom,
      rgba(255, 255, 255, 0.9),
      rgba(255, 255, 255, 0.7)
    ),
    url("/pic/display.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
}

.introduction {
  font-size: 6rem;
  line-height: 120%;
  position: absolute;
  top: 15%;
  left: 10%;
  color: #545b77;
}

.content-box {
  flex: auto;
  display: grid;
  grid-template-columns: 2fr 8fr;
  transition: all 0.2s ease-in-out;
  position: relative;
  overflow: hidden;
}

.content-box.notEditMode {
  grid-template-columns: 0fr 1fr;
}

.force-graph-box {
  max-height: 95vh;
  grid-column: 2;
}
.control-panel-box {
  grid-column: 1;
  width: 100%;
  height: 100%;

  padding: 0.3vw;
  padding-top: 0;
  padding-left: 0;
  max-height: 95vh;
  z-index: 1;
}
.control-panel {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  background-color: #fff;
}
.control-panel-content {
  flex: 0 0 95%;
  padding: 1vw;
  overflow: auto;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* Internet Explorer 10+ */
}

.control-panel-content::-webkit-scrollbar {
  /* WebKit */
  width: 0;
  height: 0;
}
.button-box-content {
  flex: 0 0 5%;
  width: 100%;
  /* height: 100%; */
}

.base-mode {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
  gap: 0.3vw;
}
.button-box {
  flex: fit-content;
  display: flex;
  gap: 0rem;
  justify-content: left;
}

.table-mode {
  width: 100%;
  height: 100%;
}
.tab-btn {
  width: 100%;
  height: 100%;
  border: none;
  background-color: transparent;
  color: #545b77;
  cursor: pointer;
  padding-top: 1.5%;
}
.tab-btn:active,
.tab-btn:hover {
  box-shadow: 0 0.5rem 0rem -0.3rem rgba(0, 0, 0, 0.2);
}
.active-tab-btn {
  box-shadow: 0 0.5rem 0rem -0.3rem rgba(0, 0, 0, 0.2);
}

.no-padding {
  padding: 0 !important;
}
</style>

<style scoped>
.btn {
  border-radius: 1.2rem;
  box-shadow: 0rem 0.1rem 0.4rem rgba(0, 0, 0, 0.26);
}
.edit-btn {
  display: flex;
  align-items: center;
  padding: 0.3rem 0.3rem;
}

.panel-icon {
  cursor: pointer;
  fill: #545b77;
  padding: 0.2rem;

  border-radius: 0.4rem;
  width: 2.5rem;
  height: 2.5rem;
  transition: background-color 0.3s, fill 0.3s;
}

.panel-icon:hover,
.panel-icon:active {
  background-color: #545b77;
  fill: #fff;
  border: none;
}
</style>

<!-- animation -->
<style scoped>
.forceAnimation-enter-from {
  opacity: 0;
  transform: translateY(-3rem);
}

.forceAnimation-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.forceAnimation-leave-from {
  opacity: 1;
  transform: translateY(0);
}
.forceAnimation-leave-to {
  opacity: 0;
  transform: translateY(3rem);
}

.treeAnimation-enter-from {
  opacity: 0;
}

.treeAnimation-enter-to {
  opacity: 1;
}
.treeAnimation-leave-from {
  opacity: 1;
}
.treeAnimation-leave-to {
  opacity: 0;
}

.forceAnimation-enter-active,
.forceAnimation-leave-active {
  transition: all 0.1s ease-out;
}
.treeAnimation-enter-active,
.treeAnimation-leave-active {
  transition: opacity 0.3s ease-out;
}
</style>

<style lang="less">
.config-panel-tab {
  height: 100%;
  --el-tabs-header-height: none;
  --el-color-primary: #545b77;
  padding: 0 1vw;
  --el-font-size-base: 1.5rem;

  .el-tabs__header {
    margin: 0;
  }
  .el-tabs__item {
    color: #aaa;
  }
  .el-tabs__item.is-active {
    color: var(--el-color-primary);
  }
  .el-tabs__item:hover {
    color: var(--el-color-primary);
  }
  .el-tabs__nav,
  .el-tabs__nav-scroll,
  .el-tabs__nav-wrap,
  .el-tabs__header {
    height: 100%;
  }
}
.el-loading-mask {
  --el-color-primary: #545b77;
}
</style>
