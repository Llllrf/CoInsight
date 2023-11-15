<template>
  <div class="statistics-graph-box">
    <BaseCard mode="flat" class="barchart-container">
      <div class="title">Link Relationship</div>

      <div class="link-filter-box">
        <div v-for="link in linkType" class="link-filter">
          <svg
            viewBox="0 0 1024 1024"
            xmlns="http://www.w3.org/2000/svg"
            :class="[
              'check-icon',
              { 'check-icon-active': selectedLinkType[link] },
            ]"
            @click="toggleSelectedLink(link)"
          >
            <path
              d="M433.1 657.7c12.7 17.7 39 17.7 51.7 0l210.6-292c3.8-5.3 0-12.7-6.5-12.7H642c-10.2 0-19.9 4.9-25.9 13.3L459 584.3l-71.2-98.8c-6-8.3-15.6-13.3-25.9-13.3H315c-6.5 0-10.3 7.4-6.5 12.7l124.6 172.8z"
            ></path>
            <path
              d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32z m-40 728H184V184h656v656z"
            ></path>
          </svg>
          <span> {{ link }}</span>
        </div>
      </div>
      <div id="barchart-box">
        <div class="tooltip" style="opacity: 0"></div></div
    ></BaseCard>
    <BaseCard mode="flat" class="histogram-container">
      <div class="title">Insight Type & Score</div>
      <div id="histogram-box">
        <div class="tooltip" style="opacity: 0"></div>
        <svg style="width: 100%; height: 100%">
          <defs>
            <symbol
              id="defs-check-insight"
              viewBox="0 0 1024 1024"
              xmlns="http://www.w3.org/2000/svg"
            >
              <rect width="1024" height="1024" fill="currentcolor"></rect>
              <path
                d="M433.1 657.7c12.7 17.7 39 17.7 51.7 0l210.6-292c3.8-5.3 0-12.7-6.5-12.7H642c-10.2 0-19.9 4.9-25.9 13.3L459 584.3l-71.2-98.8c-6-8.3-15.6-13.3-25.9-13.3H315c-6.5 0-10.3 7.4-6.5 12.7l124.6 172.8z"
              ></path>
              <path
                d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32z m-40 728H184V184h656v656z"
              ></path>
            </symbol>
          </defs>
        </svg>
      </div>
    </BaseCard>
  </div>
</template>
<script>
export default {
  data() {
    return {
      barchartWidth: null,
      barchartHeight: null,
      histogramWidth: null,
      histogramHeight: null,

      linkType: ["siblings", "parent-child", "same-name"],
      typeColorMapping: {
        kurtosis: "#F7A69F",
        correlation: "#53C4B6",
        skewness: "#F7A69F",
        "correlation-temporal": "#53C4B6",
        dominance: "#C69DE9",
        top2: "#C69DE9",
        trend: "#F7A69F",
        outlier: "#C69DE9",
        "outlier-temporal": "#C69DE9",
      },

      stateList: [],
      barchartConfig: null,
      histogramConfig: null,
      selectedLinkType: {
        siblings: true,
        "parent-child": true,
        "same-name": true,
      },
      barchartConfigs: new Map(),
      histogramConfigs: new Map(),
      selectedLinkTypes: new Map(),

      // 画图数据
      linkGroup: null,
      nodeGroup: null,

      // 中间数据
      filteredNodes: null,
      filterdLinks: null,

      // 是否刷新histogra图的axis
      refreshHistogram: false,
    };
  },

  computed: {
    rootFontSize() {
      return parseFloat(getComputedStyle(document.documentElement).fontSize);
    },
    totalData() {
      return this.$store.getters["force/totalData"];
    },

    scoreSelectionMaps() {
      return this.$store.getters["force/scoreSelectionMaps"];
    },
    focusState() {
      return this.$store.getters["force/focusState"];
    },
    scoreSelectionMap() {
      return this.scoreSelectionMaps.get(this.focusState);
    },
  },

  methods: {
    graphDataUpdate(links, nodes) {
      this.groupByLinkType(links);
      this.groupByNodeType({
        data: nodes,
      });
      this.$store.commit("force/setSelectedData", {
        nodes: nodes.map((d) => d.id),
        links: links,
      });
    },
    groupByLinkType(payload) {
      let counts = [];
      if (payload.length > 0) {
        counts = d3
          .rollups(
            payload,
            (D) => D.length,
            (d) => d.type
          )
          .map((d) => ({
            type: d[0],
            count: d[1],
          }));
      }
      this.linkGroup = counts;
    },

    groupByNodeType(payload) {
      const data = payload.data;
      const state = this.focusState;
      const scoreMap = new Map();
      const scoreSelectionMaps = this.scoreSelectionMaps;
      const scoreSelectionMap = this.scoreSelectionMap;

      if (data.length > 0) {
        data.forEach((node) => {
          const id = node.id;
          node["insight-list"].forEach((insight, index) => {
            const type = insight["insight-type"];
            const score = insight["insight-score"];

            let scoreFilter = true;
            if (scoreSelectionMap) {
              const filter = scoreSelectionMap.get(type);
              if (
                !filter.selected ||
                score < filter.selection[0] ||
                score >= filter.selection[1]
              ) {
                scoreFilter = false;
              }
            }

            if (scoreFilter) {
              if (scoreMap.has(type)) {
                const value = scoreMap.get(type);
                value.count += 1;
                value.scores.push({
                  id: id,
                  index: index,
                  score: score,
                });
              } else {
                const value = {
                  count: 1,
                  scores: [
                    {
                      id: id,
                      index: index,
                      score: score,
                    },
                  ],
                };
                scoreMap.set(type, value);
              }
            }
          });
        });
      }

      if (!scoreSelectionMap) {
        const types = new Map();
        for (let type of scoreMap.keys()) {
          types.set(type, { selection: "all", selected: true });
        }
        scoreSelectionMaps.set(state, types);
      }
      this.nodeGroup = scoreMap;
    },

    changeTypeSelected(payload) {
      this.scoreSelectionMap.get(payload.type).selected = payload.selected;
    },
    changeTypeSelection(payload) {
      this.scoreSelectionMap.get(payload.type).selection = payload.selection;
    },
    toggleSelectedLink(link) {
      this.selectedLinkType[link] = !this.selectedLinkType[link];
    },
    drawBarchart(newVal) {
      const that = this;

      if (!this.barchartConfig) {
        const container = d3.select("#barchart-box");
        if (!this.barchartWidth) {
          this.barchartWidth = parseInt(container.style("width"), 10);
          this.barchartHeight = parseInt(container.style("height"), 10);
        }
        const width = this.barchartWidth;
        const height = this.barchartHeight;
        const marginTop = 0;
        const marginRight = height / 16;
        const marginBottom = height / 9;
        const marginLeft = height / 16;
        container.select("svg").remove();
        const colorScale = d3.scaleOrdinal(this.linkType, [
          "#9AA3CC",
          "#9AA3CC",
          "#9AA3CC",
        ]);

        const tooltip = container.select("div.tooltip");

        const svg = container
          .append("svg")
          .attr("viewBox", [0, 0, width, height])
          .attr("style", "width: 100%; height:100%;")
          .style("user-select", "none");
        const rectGroup = svg.append("g").attr("class", "rect-group");
        const xAxis = svg
          .append("g")
          .attr("class", "x-axis")
          .style("font-size", "0.8rem")
          .attr("transform", `translate(0,${height - marginBottom})`);

        this.barchartConfig = {};
        this.barchartConfig.marginTop = marginTop;
        this.barchartConfig.marginRight = marginRight;
        this.barchartConfig.marginBottom = marginBottom;
        this.barchartConfig.marginLeft = marginLeft;
        this.barchartConfig.container = container;
        this.barchartConfig.width = width;
        this.barchartConfig.height = height;
        this.barchartConfig.colorScale = colorScale;
        this.barchartConfig.tooltip = tooltip;

        this.barchartConfigs.set(this.focusState, this.barchartConfig);
      }
      const config = this.barchartConfig;
      const y = d3
        .scaleBand()
        .domain(this.linkType.filter((d) => this.selectedLinkType[d]))
        .range([config.marginTop, config.height - config.marginBottom])
        .padding(0.1);

      const x = d3
        .scaleLinear()
        .domain([0, d3.max(newVal, (d) => d.count)])
        .nice()
        .range([config.marginLeft, config.width - config.marginRight]);

      config.container
        .select("svg")
        .select(".rect-group")
        .selectAll("rect")
        .data(newVal, (d) => d.type)
        .join(
          (enter) => {
            enter
              .append("rect")
              .on("mouseover", mouseover)
              .on("mousemove", mousemove)
              .on("mouseleave", mouseleave)
              .transition()
              .duration(300)
              .attr("cursor", "pointer")
              .attr("fill", (d) => config.colorScale(d.type))
              .attr("x", (d) => x(0))
              .attr("y", (d) => y(d.type))
              .attr("width", (d) => x(d.count) - x(0))
              .attr("height", y.bandwidth());
          },
          (update) => {
            update
              .transition()
              .duration(300)
              .attr("cursor", "pointer")
              .attr("fill", (d) => config.colorScale(d.type))
              .attr("x", (d) => x(0))
              .attr("y", (d) => y(d.type))
              .attr("width", (d) => x(d.count) - x(0))
              .attr("height", y.bandwidth());
          },
          (exit) => {
            exit
              .attr("opacity", 1)
              .attr("pointer-events", "none")
              .transition()
              .duration(100)
              .attr("opacity", 0)
              .remove();
          }
        );
      config.container
        .select("svg")
        .select(".x-axis")
        .transition()
        .duration(300)
        .call(
          d3
            .axisBottom(x)
            .ticks(8)
            .tickSize(config.marginBottom / 4)
        )
        .select(".domain")
        .attr("stroke-opacity", 0);

      function mouseover(event, d) {
        config.tooltip.transition().duration(250).style("opacity", 1);
        d3.select(this).classed("barchart-hover-highlight", true);
      }
      function mousemove(event, d) {
        config.tooltip
          .html(`${d.type}: ${d.count}`)
          .style("left", event.x + 15 + "px")
          .style("top", event.y + "px");
      }
      function mouseleave(event, d) {
        config.tooltip.transition().duration(250).style("opacity", 0);
        d3.select(this).classed("barchart-hover-highlight", false);
      }
    },
    drawHistogram(newVal) {
      const that = this;

      if (!this.histogramConfig) {
        // initialization
        this.histogramConfig = {};
        this.histogramConfig.xTicks = {};
        this.histogramConfig.xFuncs = {};
        this.histogramConfig.brushes = new Map();

        // 获取 总insight-type 类型
        const types = Array.from(newVal.keys());

        const container = d3.select("#histogram-box");

        container.select("svg").selectChildren("g").remove();
        // barchart图的margin
        const marginLeftType = 3;
        const marginRightType = 13;
        // 获取总宽和高
        if (!this.histogramWidth) {
          this.histogramWidth = parseInt(container.style("width"), 10);
          this.histogramHeight = parseInt(container.style("height"), 10);
        }
        const width = this.histogramWidth;
        const height = this.histogramHeight;

        // 获取每个子图的高
        const subHeight = Math.floor(height / types.length);

        // slider的高
        const sliderHeight = subHeight / 5.5;
        const sliderRectHeight = subHeight / 7.4;
        // 设置每个子图的margin
        const marginTop = subHeight / 5.5;
        const marginRight = subHeight / 11;
        const marginBottom = subHeight / 7.4 + sliderHeight;
        const marginLeft = width * 0.3;
        // slider的宽
        const sliderWidth = width - marginLeft - marginRight;
        //创建tooltip
        const tooltip = container.select("div.tooltip");
        // 选择svg画布
        const svg = container
          .select("svg")
          .style("user-select", "none")
          .attr("viewBox", [0, 0, width, height]);

        // 创建左半轴的bar
        const typeColor = d3
          .scaleOrdinal()
          .domain(Object.keys(this.typeColorMapping))
          .range(Object.values(this.typeColorMapping));

        svg.append("g").attr("class", "type-bar");
        const yType = d3
          .scaleBand()
          .domain(types)
          .range([0, height])
          .padding(0.1);
        svg
          .append("g")
          .attr("transform", `translate(${marginLeft - marginRightType},0)`)
          .attr("class", "y-axis")
          .call(d3.axisRight(yType))
          .selectAll(".tick text")
          .remove();

        this.histogramConfig.container = container;
        this.histogramConfig.width = width;
        this.histogramConfig.marginLeft = marginLeft;
        this.histogramConfig.marginRight = marginRight;
        this.histogramConfig.marginTop = marginTop;
        this.histogramConfig.marginBottom = marginBottom;
        this.histogramConfig.marginLeftType = marginLeftType;
        this.histogramConfig.marginRightType = marginRightType;
        this.histogramConfig.subHeight = subHeight;
        this.histogramConfig.sliderHeight = sliderHeight;
        this.histogramConfig.sliderWidth = sliderWidth;
        this.histogramConfig.sliderRectHeight = sliderRectHeight;
        this.histogramConfig.tooltip = tooltip;
        this.histogramConfig.types = types;
        this.histogramConfig.yTypeFunc = yType;
        this.histogramConfig.typeColor = typeColor;
        this.histogramConfigs.set(this.focusState, this.histogramConfig);

        // 创建分箱器
        const bin = d3.bin().value((d) => d.score);
        //    .thresholds(d3.thresholdFreedmanDiaconis);
        // 创建右半轴的histogram
        types.forEach((type, index) => {
          const value = newVal.get(type);
          // 连续值分箱
          const bins = bin(value.scores);

          // 获取坐标轴刻度
          const all_ticks = [
            ...bins.map((bin) => bin.x0),
            bins[bins.length - 1].x1,
          ];
          this.histogramConfig.xTicks[type] = all_ticks;

          const x = d3
            .scaleLinear()
            .domain([all_ticks[0], all_ticks[all_ticks.length - 1]])
            .range([marginLeft, width - marginRight]);

          this.histogramConfig.xFuncs[type] = x;

          const y = d3
            .scaleLinear()
            .domain([0, d3.max(bins, (d) => d.length)])
            .range([subHeight - marginBottom, marginTop]);

          // 添加brush
          const brush = d3
            .brushX()
            .extent([
              [marginLeft, subHeight - sliderHeight],
              [
                marginLeft + sliderWidth,
                subHeight - sliderHeight + sliderRectHeight,
              ],
            ])
            .on("end", function (event) {
              brushended(this, event, type);
            });
          this.histogramConfig.brushes.set(type, {
            func: brush,
            position: null,
          });
          function brushended(brushContainer, event, type) {
            // 获取选择的两端的svg坐标
            const selection = event.selection;

            if (!event.sourceEvent) return;
            if (!selection) {
              // 选择为空时 （默认全选）
              that.changeTypeSelection({
                type: type,
                selection: "all",
              });
              return;
            }
            // 反解坐标，得到原值
            const [x0_selected, x1_selected] = selection.map((d) =>
              x.invert(d)
            );
            // 寻找最近的bins
            const x0 = all_ticks.reduce((acc, tick) => {
              return Math.abs(tick - x0_selected) < Math.abs(acc - x0_selected)
                ? tick
                : acc;
            }, all_ticks[0]);

            const x1 = all_ticks.reduce((acc, tick) => {
              return Math.abs(tick - x1_selected) < Math.abs(acc - x1_selected)
                ? tick
                : acc;
            }, all_ticks[0]);
            const position = x1 > x0 ? [x0, x1].map(x) : null;

            d3.select(brushContainer).transition().call(brush.move, position);

            that.histogramConfig.brushes.get(type).position = position;

            that.changeTypeSelection({
              type: type,
              selection: x1 > x0 ? [x0, x1] : "all",
            });
          }
          // 画子图
          this.drawSubHistogram(
            type,
            index,
            bins,
            y,
            this.histogramConfig,
            svg
          );
        });
      } else {
        const types = this.histogramConfig.types;
        const xTicks = this.histogramConfig.xTicks;
        // 重新根据types的顺序设置class
        this.histogramConfig.container
          .select("svg")
          .selectChildren("g.sub-graph")
          .each(function (d, index) {
            d3.select(this).attr("class", `${types[index]}-box sub-graph`);
          });
        types.forEach((type, index) => {
          const value = newVal.get(type);
          const x = this.histogramConfig.xFuncs[type];
          const svg = this.histogramConfig.container.select("svg");
          const subGraph = svg.select(`.${type}-box`);

          // get new bins
          let bins = [];
          let maxBin = null;
          if (value) {
            bins = d3
              .bin()
              .value((d) => d.score)
              .domain(x.domain())
              .thresholds(xTicks[type])(value.scores);
            // 找到最大长度的 bin
            maxBin = bins.reduce((acc, curr) =>
              curr.length > acc.length ? curr : acc
            );
          }
          // get new y
          const y = d3
            .scaleLinear()
            .domain([0, d3.max(bins, (d) => d.length)])
            .range([
              this.histogramConfig.subHeight -
                this.histogramConfig.marginBottom,
              this.histogramConfig.marginTop,
            ]);

          // 原来位置有图，调整大小/位置即可
          if (this.refreshHistogram) {
            if (subGraph.empty()) {
              this.drawSubHistogram(
                type,
                index,
                bins,
                y,
                this.histogramConfig,
                svg
              );
            } else {
              subGraph.attr(
                "transform",
                `translate(0,${index * this.histogramConfig.subHeight})`
              );

              const all_ticks = xTicks[type];
              const selected = this.scoreSelectionMap.get(type).selected;
              // 刷新小x轴
              const xAxis = subGraph.select("g.x-axis");
              xAxis.selectAll("*").remove();
              xAxis
                .attr(
                  "transform",
                  `translate(0,${
                    this.histogramConfig.subHeight -
                    this.histogramConfig.marginBottom
                  })`
                )
                .call(d3.axisBottom(x).tickValues(all_ticks).tickSizeInner(3))
                .call((g) => g.attr("font-size", "0.8rem"));

              subGraph.select("g.sub-title").select("text").text(type);
              subGraph
                .select("g.sub-title")
                .select("use")
                .datum({
                  selected: selected,
                  type: type,
                })
                .classed("histogram-type-unselected", (d) => {
                  return !d.selected;
                });
              // 矩形框重定位 / 重造型
              subGraph
                .select("rect.slider-rect")
                .attr("height", this.histogramConfig.sliderRectHeight)
                .attr(
                  "y",
                  this.histogramConfig.subHeight -
                    this.histogramConfig.sliderHeight
                );

              // brush 刷选框
              subGraph.selectChildren(".brush-line").remove();
              all_ticks.forEach((d, index) => {
                if (index !== 0)
                  subGraph
                    .append("line")
                    .attr("class", "brush-line")
                    .attr("x1", x(d))
                    .attr("x2", x(d))
                    .attr(
                      "y1",
                      this.histogramConfig.subHeight -
                        this.histogramConfig.sliderHeight
                    )
                    .attr(
                      "y2",
                      this.histogramConfig.subHeight -
                        this.histogramConfig.sliderHeight +
                        this.histogramConfig.sliderRectHeight
                    )
                    .attr("stroke", "#fff");
              });
              const brushContainer = subGraph.select("g.brush");
              const brush = this.histogramConfig.brushes.get(type).func;

              brushContainer.selectAll("*").remove();
              brushContainer.call(brush);
              brushContainer.call(
                brush.move,
                this.histogramConfig.brushes.get(type).position
              );
            }
          }

          subGraph
            .select(".max-value")
            .selectChildren("text")
            .data(maxBin ? [maxBin] : [])
            .join(
              (enter) => {
                enter
                  .append("text")
                  .attr("class", "max-value")
                  .attr("x", (d) => x(d.x0) + (x(d.x1) - x(d.x0)) / 2)
                  .attr("y", (d) => y(d.length) + that.rootFontSize)
                  .attr("text-anchor", "middle")
                  .attr("fill", "#fff")
                  .attr("font-size", "1rem")
                  .text((d) => d.length);
              },
              (update) =>
                update
                  .attr("x", (d) => x(d.x0) + (x(d.x1) - x(d.x0)) / 2)
                  .attr("y", (d) => y(d.length) + that.rootFontSize)
                  .text((d) => d.length),
              (exit) => {
                exit.remove();
              }
            );

          subGraph
            .select(".rect-group")
            .selectAll("rect")
            .data(bins, (d, index) => {
              return index;
            })
            .join(
              (enter) => {
                enter
                  .append("rect")
                  .attr("y", y(0))
                  .attr("x", x(xTicks[type][0]))
                  .attr("height", 0)
                  .on("mouseover", mouseover)
                  .on("mousemove", mousemove)
                  .on("mouseleave", mouseleave)
                  .transition()
                  .duration(300)
                  .attr("x", (d) => {
                    if (d.x0 === d.x1) {
                      return this.histogramConfig.marginLeft;
                    } else {
                      return x(d.x0) + 1;
                    }
                  })
                  .attr("width", (d) => {
                    const rectWidth = x(d.x1) - x(d.x0);
                    if (rectWidth === 0) {
                      return (
                        this.histogramConfig.width -
                        this.histogramConfig.marginLeft -
                        this.histogramConfig.marginRight
                      );
                    } else {
                      return rectWidth - 1;
                    }
                  })
                  .attr("y", (d) => y(d.length))
                  .attr("height", (d) => y(0) - y(d.length));
              },
              (update) => {
                update
                  .transition()
                  .duration(300)
                  .attr("x", (d) => {
                    if (d.x0 === d.x1) {
                      return this.histogramConfig.marginLeft;
                    } else {
                      return x(d.x0) + 1;
                    }
                  })
                  .attr("width", (d) => {
                    const rectWidth = x(d.x1) - x(d.x0);
                    if (rectWidth === 0) {
                      return (
                        this.histogramConfig.width -
                        this.histogramConfig.marginLeft -
                        this.histogramConfig.marginRight
                      );
                    } else {
                      return rectWidth - 1;
                    }
                  })
                  .attr("y", (d) => y(d.length))
                  .attr("height", (d) => y(0) - y(d.length));
              },
              (exit) => {
                exit
                  .attr("opacity", 1)
                  .attr("pointer-events", "none")
                  .transition()
                  .duration(100)
                  .attr("opacity", 0)
                  .remove();
              }
            );
        });
        if (this.refreshHistogram) this.refreshHistogram = false;
      }

      const yType = this.histogramConfig.yTypeFunc;
      const xType = d3
        .scaleLinear()
        .domain([0, d3.max(Array.from(newVal.values()), (d) => d.count)])
        .nice()
        .range([
          this.histogramConfig.marginLeftType,
          this.histogramConfig.marginLeft -
            this.histogramConfig.marginRightType,
        ]);

      this.histogramConfig.container
        .select("svg")
        .select(".type-bar")
        .selectAll("rect")
        .data(Array.from(newVal.entries()), (d) => d[0])
        .join(
          (enter) => {
            enter
              .append("rect")
              .on("mouseover", mouseover)
              .on("mousemove", function (event, d) {
                that.histogramConfig.tooltip
                  .html(`${d[1].count}`)
                  .style("left", event.x + 15 + "px")
                  .style("top", event.y + "px");
              })
              .on("mouseleave", mouseleave)
              .attr("y", (d) => yType(d[0]))
              .attr("height", yType.bandwidth())
              .attr(
                "x",
                (d) =>
                  this.histogramConfig.marginLeft -
                  this.histogramConfig.marginRightType +
                  this.histogramConfig.marginLeftType -
                  xType(d[1].count)
              )
              .transition()
              .duration(300)
              .attr("cursor", "pointer")
              .attr("fill", (d) => this.histogramConfig.typeColor(d[0]))

              .attr("width", (d) => xType(d[1].count) - xType(0));
          },
          (update) => {
            update
              .transition()
              .duration(300)
              .attr("fill", (d) => this.histogramConfig.typeColor(d[0]))

              .attr(
                "x",
                (d) =>
                  this.histogramConfig.marginLeft -
                  this.histogramConfig.marginRightType +
                  this.histogramConfig.marginLeftType -
                  xType(d[1].count)
              )
              .attr("y", (d) => yType(d[0]))
              .attr("width", (d) => xType(d[1].count) - xType(0))
              .attr("height", yType.bandwidth());
          },
          (exit) => {
            exit
              .attr("opacity", 1)
              .attr("pointer-events", "none")
              .transition()
              .duration(100)
              .attr("opacity", 0)
              .remove();
          }
        );

      function mouseover(event, d) {
        that.histogramConfig.tooltip
          .transition()
          .duration(250)
          .style("opacity", 1);
        d3.select(this).classed("barchart-hover-highlight", true);
      }
      function mousemove(event, d) {
        that.histogramConfig.tooltip
          .html(`${d.length}`)
          .style("left", event.x + 15 + "px")
          .style("top", event.y + "px");
      }
      function mouseleave(event, d) {
        that.histogramConfig.tooltip
          .transition()
          .duration(250)
          .style("opacity", 0);
        d3.select(this).classed("barchart-hover-highlight", false);
      }
    },

    drawSubHistogram(type, index, bins, y, histogramConfig, svg) {
      const that = this;
      const all_ticks = histogramConfig.xTicks[type];
      const x = histogramConfig.xFuncs[type];
      const brush = histogramConfig.brushes.get(type).func;

      // 创建当前种类子图的g
      const g = svg
        .append("g")
        .attr("class", `${type}-box sub-graph`)
        .attr("transform", `translate(0,${index * histogramConfig.subHeight})`);

      const subTitle = g.append("g").attr("class", "sub-title");
      subTitle
        .append("text")
        .attr("class", "type-text")
        .text(type)
        .attr("x", histogramConfig.marginLeft)
        .attr("y", 0 + 1.2 * that.rootFontSize)
        .attr("text-anchor", "start")
        .attr("fill", "#555")
        .attr("font-size", "1.2rem");
      subTitle
        .append("use")
        .datum({
          selected: true,
          type: type,
        })
        .attr("href", "#defs-check-insight")
        .attr(
          "transform",
          `translate(${
            histogramConfig.width - histogramConfig.marginRight - 15
          },0)`
        )
        .attr("width", "1.5rem")
        .attr("height", "1.5rem")
        .attr("cursor", "pointer")
        .classed("histogram-type-selected", true)
        .on("mouseover", function () {
          d3.select(this).classed("histogram-type-hovered", true);
        })
        .on("mouseout", function (event, d) {
          if (!d.selected)
            d3.select(this)
              .classed("histogram-type-unselected", true)
              .classed("histogram-type-hovered", false);
          else {
            d3.select(this)
              .classed("histogram-type-unselected", false)
              .classed("histogram-type-hovered", false);
          }
        })
        .on("click", function (event, d) {
          d.selected = !d.selected;
          if (!d.selected)
            d3.select(this).classed("histogram-type-unselected", true);
          else {
            d3.select(this).classed("histogram-type-unselected", false);
          }
          that.changeTypeSelected({
            type: d.type,
            selected: d.selected,
          });
        });
      // slider矩形框
      const sliderRect = g
        .append("rect")
        .attr("class", "slider-rect")
        .attr("x", histogramConfig.marginLeft)
        .attr("y", histogramConfig.subHeight - histogramConfig.sliderHeight)
        .attr("width", histogramConfig.sliderWidth)
        .attr("height", histogramConfig.sliderRectHeight)
        .attr("fill", "#D5DAEC")
        .attr("stroke", "#fff");
      // 添加slider的背景线
      all_ticks.forEach((d, index) => {
        if (index !== 0)
          g.append("line")
            .attr("class", "brush-line")
            .attr("x1", x(d))
            .attr("x2", x(d))
            .attr(
              "y1",
              histogramConfig.subHeight - histogramConfig.sliderHeight
            )
            .attr(
              "y2",
              histogramConfig.subHeight -
                histogramConfig.sliderHeight +
                histogramConfig.sliderRectHeight
            )
            .attr("stroke", "#fff");
      });

      // 添加brush
      g.append("g").attr("class", "brush").call(brush);

      // 直方图矩形框
      g.append("g")
        .attr("fill", "#858eb5")
        .attr("class", "rect-group")
        .style("cursor", "pointer")
        .selectAll("rect")
        .data(bins, (d, index) => index)
        .join("rect")
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)
        .attr("x", (d) => {
          if (d.x0 === d.x1) {
            return histogramConfig.marginLeft;
          } else {
            return x(d.x0) + 1;
          }
        })
        .attr("width", (d) => {
          const rectWidth = x(d.x1) - x(d.x0);
          if (rectWidth === 0) {
            return (
              histogramConfig.width -
              histogramConfig.marginLeft -
              histogramConfig.marginRight
            );
          } else {
            return rectWidth - 1;
          }
        })
        .attr("y", (d) => y(d.length))
        .attr("height", (d) => y(0) - y(d.length));

      // 找到最大长度的 bin
      let maxBin = bins.reduce((acc, curr) =>
        curr.length > acc.length ? curr : acc
      );

      // 在最高矩形上添加文本
      g.append("g")
        .attr("class", "max-value")
        .selectChildren("text")
        .data([maxBin])
        .join("text")
        .attr("x", (d) => x(d.x0) + (x(d.x1) - x(d.x0)) / 2)
        .attr("y", (d) => y(d.length) + that.rootFontSize)
        .attr("text-anchor", "middle")
        .attr("fill", "#fff")
        .attr("font-size", "1rem")
        .text((d) => d.length);
      // x轴
      g.append("g")
        .attr("class", "x-axis")
        .attr(
          "transform",
          `translate(0,${
            histogramConfig.subHeight - histogramConfig.marginBottom
          })`
        )
        .call(d3.axisBottom(x).tickValues(all_ticks).tickSizeInner(3))
        .call((g) => g.attr("font-size", "0.8rem"));
      function mouseover(event, d) {
        histogramConfig.tooltip.transition().duration(250).style("opacity", 1);
        d3.select(this).classed("barchart-hover-highlight", true);
      }
      function mousemove(event, d) {
        histogramConfig.tooltip
          .html(`${d.length}`)
          .style("left", event.x + 15 + "px")
          .style("top", event.y + "px");
      }
      function mouseleave(event, d) {
        histogramConfig.tooltip.transition().duration(250).style("opacity", 0);
        d3.select(this).classed("barchart-hover-highlight", false);
      }
    },
    filterByScocre(scoreSelectionMap, originLinks, originNodes) {
      // 根据 score selection 筛选出新的selectedNodeData
      const selectedNodeData = originNodes.filter((node) => {
        let select = false;
        //  const newInsightIndex = node.insightIndex;
        for (let insight of node["insight-list"]) {
          const type = insight["insight-type"];
          const score = insight["insight-score"];
          const selection = scoreSelectionMap.get(type).selection;
          const selected = scoreSelectionMap.get(type).selected;
          if (selected) {
            if (
              selection === "all" ||
              (score >= selection[0] && score < selection[1])
            ) {
              select = true;
              break;
            }
          }
        }

        return select;
      });

      const idMap = new Set();
      selectedNodeData.forEach((node) => {
        idMap.add(node.id);
      });
      const filteredLinks = originLinks.filter(
        (d) => idMap.has(d.source) && idMap.has(d.target)
      );
      return [filteredLinks, selectedNodeData];
    },
  },
  watch: {
    focusState(newVal) {
      if (newVal) {
        if (this.stateList.includes(newVal)) {
          this.barchartConfig = this.barchartConfigs.get(newVal);
          this.histogramConfig = this.histogramConfigs.get(newVal);
          this.selectedLinkType = this.selectedLinkTypes.get(newVal);
          this.refreshHistogram = true;

          // swich state
        } else {
          this.barchartConfig = null;
          this.histogramConfig = null;
          this.selectedLinkType = {
            siblings: true,
            "parent-child": true,
            "same-name": true,
          };

          // initialize
          this.stateList.push(newVal);
          this.selectedLinkTypes.set(newVal, this.selectedLinkType);

          this.groupByLinkType(this.totalData.links);
          this.groupByNodeType({
            data: this.totalData.nodes,
          });
        }
      }
    },
    linkGroup(newVal) {
      if (newVal) {
        this.drawBarchart(newVal);
      }
    },
    nodeGroup(newVal) {
      if (newVal) {
        this.drawHistogram(newVal);
      }
    },
    scoreSelectionMap: {
      deep: true,
      handler(newVal) {
        const that = this;
        if (newVal) {
          const filteredNodes = that.filteredNodes
            ? that.filteredNodes
            : that.totalData.nodes;
          const selectedLinks = that.filterdLinks
            ? that.filterdLinks
            : that.totalData.links;

          const [filteredLinks, selectedNodeData] = this.filterByScocre(
            newVal,
            selectedLinks,
            filteredNodes
          );
          this.graphDataUpdate(filteredLinks, selectedNodeData);
        }
      },
    },
    selectedLinkType: {
      deep: true,
      handler(newVal) {
        this.selectedLinkTypes.set(this.focusState, newVal);
        const that = this;
        // 作为主选项，每次选择获取全局数据
        const totalLinks = that.totalData.links;
        const totalNodes = that.totalData.nodes;

        const selectedLinkData = totalLinks.filter((d) => newVal[d.type]);

        const selectedId = new Set();
        selectedLinkData.forEach((link) => {
          const sourceId = link.source;
          const targetId = link.target;
          selectedId.add(sourceId);
          selectedId.add(targetId);
        });

        const unSelectedId = new Set();
        const unSelectedLinkData = totalLinks.filter((d) => !newVal[d.type]);

        unSelectedLinkData.forEach((link) => {
          const sourceId = link.source;
          const targetId = link.target;

          unSelectedId.add(sourceId);
          unSelectedId.add(targetId);
        });

        const unSelectedIdFixed = new Set(
          [...unSelectedId].filter((x) => !selectedId.has(x))
        );

        const filteredNodes = totalNodes.filter(
          (d) => !unSelectedIdFixed.has(d.id)
        );
        that.filteredNodes = filteredNodes;
        that.filterdLinks = selectedLinkData;

        const [links, nodes] = this.filterByScocre(
          this.scoreSelectionMap,
          selectedLinkData,
          filteredNodes
        );
        this.graphDataUpdate(links, nodes);
      },
    },
  },
};
</script>

<style scoped>
.statistics-graph-box {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: column;
  gap: 0.5vw;

  background-color: #fff;
}
.barchart-container {
  height: 25vh;
  width: 100%;
  background-color: #fff;
  transition: border-color 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  gap: 0.3vw;
}
.histogram-container {
  width: 100%;
  height: fit-content;
  margin-bottom: 0.3vw;
  background-color: #fff;
  transition: border-color 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  gap: 0.7vw;
}
#histogram-box {
  width: 100%;
  height: 135vh;
}
.link-filter-box {
  display: flex;
  width: 100%;
  justify-content: center;
  gap: 4%;
  flex-grow: 0;
  user-select: none;
}
.link-filter {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
#barchart-box {
  flex-grow: 1;
}

.histogram-container:hover,
.barchart-container:hover {
  box-shadow: 0.1rem 0.4rem 0.6rem 0.1rem rgba(0, 0, 0, 0.26);
}

.title {
  font-weight: bold;
  font-size: 1.6rem;
  text-align: center;
  color: #545b77;
  margin: 0.2vw 0;
  margin-top: 0.6vw;
  flex-grow: 0;
}

.check-icon {
  cursor: pointer;
  width: 1.5rem;
  height: 1.5rem;

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
  background-color: #858eb5;
  fill: #fff;
}
</style>

<style lang="less">
.barchart-hover-highlight {
  filter: brightness(110%);

  transition: filter 0.2s;
}

.histogram-type-selected {
  color: #858eb5;
  fill: #fff;
}
.histogram-type-unselected {
  color: transparent;
  fill: #545b77;
}
.histogram-type-hovered {
  color: #545b77;
  fill: #fff;
}
</style>
