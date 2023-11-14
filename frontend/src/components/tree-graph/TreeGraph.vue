<template>
  <div class="container">
    <div class="more-box" v-show="showMoreIcon">
      <svg
        class="more-icon"
        viewBox="0 0 1024 1024"
        xmlns="http://www.w3.org/2000/svg"
        @click="
          showMoreIcon = !showMoreIcon;
          showMorePanel = !showMorePanel;
          hidePanelMode = !hidePanelMode;
        "
      >
        <path
          d="M511.48 22.62c-270.42 0-489.62 218.96-489.62 489.09s219.2 489.09 489.62 489.09 489.61-218.96 489.61-489.09S781.89 22.62 511.48 22.62zM211.83 435.56c-0.11-0.19-0.11-0.49-0.23-0.71l-0.3-1.2c0-0.23-0.11-0.42-0.11-0.6l-0.3-1.32c0-0.3-0.11-0.49-0.11-0.68-0.08-0.42-0.08-0.94-0.19-1.32 0-0.3-0.12-0.53-0.12-0.83 0-0.37-0.11-0.79-0.11-1.2-0.07-0.26-0.07-0.68-0.07-1.01v0.04c0-0.3-0.11-0.6 0-1.13-0.11-0.6-0.11-1.32-0.11-2 0-0.71 0.11-1.32 0.11-2.03l0.07-0.98 0.11-1.02c0-0.41 0-0.83 0.12-1.2 0-0.3 0.11-0.53 0.11-0.83 0.01-0.43 0.08-0.86 0.19-1.28 0-0.34 0.11-0.53 0.11-0.71l0.3-1.31c0-0.23 0-0.42 0.11-0.6l0.3-1.2c0.11-0.19 0.11-0.49 0.22-0.68 0.07-0.34 0.3-0.75 0.41-1.13l0.3-0.83c0.11-0.3 0.3-0.68 0.38-0.98l0.38-0.9c0.07-0.3 0.26-0.6 0.37-0.91 0.08-0.3 0.23-0.71 0.45-1.02 0.19-0.22 0.26-0.53 0.38-0.68 0.11-0.45 0.3-0.75 0.53-1.13 0.17-0.17 0.31-0.38 0.41-0.6 0.19-0.42 0.42-0.71 0.64-1.13 0.16-0.17 0.28-0.36 0.38-0.56 0.22-0.42 0.53-0.75 0.75-1.13 0.08-0.22 0.3-0.42 0.42-0.6l0.83-1.13 0.49-0.6c0.23-0.3 0.41-0.6 0.72-0.9 0.22-0.3 0.53-0.49 0.75-0.79 0.22-0.19 0.42-0.53 0.6-0.71l1.47-1.51 99.24-96.46c16.73-16.11 43.23-16.11 59.96 0 16.57 16.1 16.57 42.14 0 58.24l-26.93 26.15h413.09c23.5 0 42.44 18.51 42.44 41.23 0 22.84-19.06 41.27-42.44 41.27H252.39c-0.6 0-1.32-0.12-2.07-0.12l-0.9-0.11-1.06-0.07c-0.42 0.01-0.84-0.02-1.24-0.11-0.3 0-0.53-0.11-0.83-0.11-0.44-0.02-0.89-0.08-1.32-0.19-0.34 0-0.53-0.11-0.76-0.11l-1.32-0.3c-0.34-0.08-0.53-0.08-0.75-0.19l-1.2-0.3c-0.23-0.11-0.56-0.11-0.76-0.23l-1.13-0.37-0.83-0.34-1.06-0.38-0.9-0.3-0.94-0.42c-0.3-0.08-0.71-0.19-1.02-0.42-0.22-0.19-0.53-0.26-0.75-0.37-0.38-0.11-0.76-0.3-1.13-0.53-0.19-0.16-0.41-0.29-0.64-0.38l-1.13-0.6c-0.19-0.16-0.41-0.29-0.64-0.37-0.38-0.23-0.72-0.53-1.13-0.76-0.23-0.08-0.41-0.3-0.6-0.37l-1.13-0.83-0.64-0.45-0.94-0.75c-0.3-0.19-0.49-0.49-0.79-0.68l-0.75-0.6c-0.49-0.53-1.02-0.91-1.55-1.43-0.53-0.49-0.94-1.02-1.43-1.5-0.22-0.19-0.42-0.49-0.6-0.72-0.23-0.3-0.57-0.49-0.75-0.79-0.23-0.3-0.53-0.6-0.72-0.91l-0.53-0.6c-0.3-0.37-0.64-0.71-0.86-1.13-0.07-0.19-0.27-0.37-0.38-0.56-0.22-0.41-0.53-0.75-0.75-1.13-0.19-0.22-0.3-0.41-0.38-0.6l-0.64-1.09-0.41-0.64c-0.11-0.37-0.3-0.68-0.53-1.05-0.19-0.22-0.3-0.52-0.41-0.75-0.07-0.3-0.3-0.68-0.41-0.98-0.08-0.3-0.3-0.6-0.42-0.9l-0.3-0.94-0.42-1.02-0.3-0.75c-0.22-0.35-0.3-0.76-0.41-1.14z m600.83 166.18l-0.07 1.02-0.11 1.02c0 0.38 0 0.79-0.11 1.2 0 0.3-0.12 0.49-0.12 0.79-0.01 0.44-0.08 0.89-0.19 1.32 0 0.3-0.11 0.49-0.11 0.68l-0.3 1.32c0 0.23 0 0.41-0.11 0.6l-0.3 1.2c-0.12 0.23-0.12 0.53-0.23 0.72-0.08 0.34-0.3 0.71-0.41 1.09-0.08 0.34-0.19 0.53-0.3 0.83l-0.38 1.02-0.37 0.9c-0.07 0.3-0.27 0.61-0.38 0.91-0.08 0.3-0.22 0.68-0.45 0.98-0.19 0.22-0.26 0.53-0.37 0.71-0.12 0.38-0.3 0.71-0.53 1.13-0.19 0.19-0.3 0.38-0.42 0.56-0.19 0.41-0.41 0.75-0.64 1.13-0.19 0.22-0.3 0.42-0.38 0.6-0.22 0.38-0.53 0.71-0.75 1.13-0.08 0.19-0.3 0.38-0.42 0.56-0.3 0.41-0.49 0.75-0.83 1.13l-0.49 0.6c-0.23 0.3-0.42 0.6-0.76 0.91-0.3 0.3-0.49 0.6-0.83 0.9-0.22 0.19-0.41 0.53-0.6 0.71l-1.47 1.51-99.28 96.46c-16.53 16.1-43.31 16.1-59.88 0s-16.57-42.14 0-58.24l26.89-26.15h-413.2c-23.46 0-42.41-18.51-42.41-41.23 0-22.84 19.06-41.27 42.41-41.27h515.68c0.6 0 1.32 0.11 2.07 0.11 0.3 0 0.6 0.11 0.94 0.11l1.02 0.08c0.42 0 0.87 0 1.24 0.11 0.3 0 0.53 0.12 0.83 0.12 0.44 0.01 0.89 0.08 1.32 0.19 0.38 0 0.57 0.11 0.76 0.11l1.32 0.3c0.37 0.07 0.56 0.07 0.75 0.19l1.24 0.3c0.23 0.12 0.53 0.12 0.76 0.23l1.13 0.37 0.79 0.34 1.06 0.38 0.94 0.3 0.9 0.41c0.34 0.08 0.75 0.19 1.02 0.42 0.22 0.19 0.57 0.26 0.75 0.37 0.42 0.12 0.76 0.3 1.13 0.53 0.19 0.16 0.41 0.29 0.64 0.38l1.13 0.6c0.23 0.19 0.41 0.3 0.64 0.38 0.38 0.22 0.72 0.53 1.13 0.75 0.19 0.08 0.42 0.3 0.64 0.38l1.13 0.83 0.61 0.45c0.3 0.22 0.64 0.45 0.94 0.75 0.3 0.19 0.53 0.49 0.79 0.68l0.75 0.6 1.55 1.43 1.47 1.51c0.23 0.19 0.42 0.49 0.6 0.71 0.23 0.3 0.53 0.49 0.71 0.79l0.76 0.91 0.49 0.6c0.34 0.38 0.64 0.71 0.86 1.13 0.08 0.19 0.3 0.38 0.38 0.56 0.22 0.42 0.53 0.75 0.75 1.13 0.17 0.17 0.31 0.38 0.41 0.6 0.19 0.42 0.42 0.71 0.64 1.09 0.19 0.22 0.26 0.42 0.38 0.64 0.11 0.38 0.3 0.68 0.53 1.05 0.19 0.22 0.3 0.53 0.41 0.75l0.42 0.98c0.11 0.3 0.3 0.6 0.38 0.9l0.37 0.94 0.38 1.02 0.34 0.75c0.19 0.35 0.31 0.73 0.37 1.13 0.11 0.19 0.11 0.49 0.23 0.71l0.3 1.2c0 0.23 0 0.41 0.11 0.61l0.3 1.32c0 0.3 0.11 0.49 0.11 0.68 0.11 0.42 0.11 0.94 0.19 1.32 0 0.3 0.12 0.53 0.12 0.83 0 0.37 0.11 0.79 0.11 1.2 0.11 0.3 0.11 0.68 0.11 0.98 0.07 0.41 0.07 0.71 0.07 1.01 0.11 0.6 0.11 1.28 0.11 2.03 0.01 0.66-0.11 1.26-0.11 1.97z"
        ></path>
      </svg>
    </div>
    <transition name="slide">
      <VegaLiteFilter
        v-if="showMorePanel"
        :insightList="selectedNode['insight-list']"
        :insightIndex="selectedNode['insightIndex']"
        class="showMorePanelBox"
        @insightIndexChange="changeInsightIndex"
        @hideMoreBox="hideMoreBox"
      ></VegaLiteFilter>
    </transition>
    <div id="tree-svg-container">
      <svg>
        <defs>
          <symbol id="defs-start" viewBox="0 0 1024 1024">
            <rect width="100%" height="100%" fill="currentcolor" rx="5%"></rect>
            <path
              d="M512.016285 65.143519a34.981021 34.981021 0 0 1 30.844532 17.783648L900.553151 702.488594a35.632436 35.632436 0 0 1-30.844531 53.448654H154.323951a35.632436 35.632436 0 0 1-30.877102-53.448654L481.171754 82.927167A34.981021 34.981021 0 0 1 512.016285 65.143519m0-65.141565a99.796878 99.796878 0 0 0-87.257126 50.35443L67.034253 669.917811a100.774001 100.774001 0 0 0 87.289698 151.161002h715.384669a100.774001 100.774001 0 0 0 87.257127-151.161002L599.273412 50.356384A99.764307 99.764307 0 0 0 512.016285 0.001954z"
            ></path>
            <path
              d="M869.70862 268.026924a35.632436 35.632436 0 0 1 30.844531 53.448655L542.860817 941.037005a35.599865 35.599865 0 0 1-61.689063 0L123.446849 321.475579a35.632436 35.632436 0 0 1 30.877102-53.448655h715.384669m0-65.141565H154.323951a100.774001 100.774001 0 0 0-87.289698 151.161002l357.724906 619.561427a100.741431 100.741431 0 0 0 174.514253 0L956.965747 354.046361a100.774001 100.774001 0 0 0-87.257127-151.161002z"
            ></path>
          </symbol>
        </defs>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      outIconSize: 45,
      // link style
      linkData: null,
      // vega-lite style
      vegaLiteHeight: 100,
      vegaLiteWidth: 150,
      iconSize: 15,
      iconOffset: 5,
      rectWidthOffset: 3,
      rectHeightOffset: 13,
      rectHeightBottomOffset: 3,
      rectR: 10,
      // vega-lite filter
      showMoreIcon: false,
      showMorePanel: false,
      hidePanelMode: false,
      selectedNode: {
        id: null,
        state: null,
        insightIndex: null,
        "insight-list": null,
      },
      nodeIdMap: null,
      durationTime: 150,
      // table interaction
      focusState: null,
      hoverIndex: {
        id: null,
        state: null,
        row: null,
        col: null,
      },
    };
  },
  computed: {
    forceData() {
      return this.$store.getters["tree/forceData"];
    },
    allTableInfo() {
      return this.$store.getters["tree/allTableInfo"];
    },
  },
  methods: {
    hideMoreBox() {
      this.hidePanelMode = true;
      this.showMorePanel = false;
      this.showMoreIcon = true;
    },
    changeInsightIndex(selectedIndex) {
      const that = this;
      const id = this.selectedNode.id;
      this.selectedNode.insightIndex = selectedIndex;
      const nodeData = this.nodeIdMap.get(id);
      nodeData.insightIndex = selectedIndex;
      const g = d3
        .select("#tree-svg-container")
        .select("svg")
        .selectChild("g.node-group")
        .selectChildren("g")
        .filter((d) => d.data.name === id);
      g.each(function () {
        const g = d3.select(this);
        g.datum().data.forceData.view.finalize();

        g.select("vega-lite-container").select(".vega-lite-graph").remove();
        g.datum().view = null;
        g.datum().img = null;
        that.drawVegaLite(g);
      });
    },
    drawVegaLite(g) {
      const that = this;

      const container = g.select(".vega-lite-container");
      const rect = g.selectChild(".rect");

      const rectTitle = g.select(".rect-title");
      const rectState = g.select(".title-state");
      const rectTitleName = g.selectChild(".title-name");
      const rectTitleDescription = g.selectChild(".title-description");
      const gData = g.datum().data.forceData;

      let yourVlSpec = JSON.parse(
        gData["insight-list"][gData.insightIndex]["vega-lite"]
      );

      // add some options
      yourVlSpec["width"] = this.vegaLiteWidth;
      yourVlSpec["height"] = this.vegaLiteHeight;
      yourVlSpec["usermeta"] = { embedOptions: { renderer: "svg" } };

      // initialization
      vegaEmbed(container.node(), yourVlSpec).then((result) => {
        const view = result.view.background("transparent");
        gData.view = view;
        const svg = container.select("svg");

        // add animation
        svg
          .attr("class", "vega-lite-graph")
          .attr("fill-opacity", 0)
          .attr("stroke-opacity", 0)
          .transition()
          .duration(175)
          .attr("fill-opacity", 1)
          .attr("stroke-opacity", 1);
        const width = svg.attr("width");
        const height = svg.attr("height");

        const titleHeight = that.iconSize + 2 * that.iconOffset;
        const rectWidth = +width + that.rectWidthOffset * 2;
        const rectHeight =
          +height + that.rectHeightOffset * 2 + titleHeight + that.iconSize;

        const translateX = rectWidth / 2;
        const translateY = rectHeight / 2;

        // add ainmation
        rect
          .attr("rx", that.rectR)
          .attr("x", 0)
          .attr("y", 0)
          .attr("width", 0)
          .attr("height", 0)
          .transition()
          .duration(150)
          .attr("x", -translateX)
          .attr("y", -translateY)
          .attr("width", rectWidth)
          .attr("height", rectHeight);

        rectTitle
          .attr("rx", that.rectR)
          .attr("x", 0)
          .attr("y", 0)
          .attr("width", 0)
          .attr("height", 0)
          .transition()
          .duration(150)
          .attr("x", -translateX)
          .attr("y", -translateY)
          .attr("width", rectWidth)
          .attr("height", titleHeight);

        rectState
          .text(function () {
            return gData.state;
          })
          .attr("x", translateX - that.iconOffset)
          .attr("y", -translateY + that.iconSize + that.iconOffset / 2)
          .attr("text-anchor", "end")
          .attr("font-size", that.iconSize - 2);

        rectTitleName

          .text(function () {
            return gData["insight-list"][gData.insightIndex]["insight-type"];
          })
          .attr("x", -translateX + that.iconOffset)
          .attr("y", -translateY + that.iconSize + that.iconOffset / 2)
          .attr("font-size", that.iconSize - 2);
        rectTitleDescription
          .text(function () {
            const rowName = gData.row;

            return `row: ${rowName}`;
          })
          .attr("font-size", "10px")
          .attr("x", -translateX + that.iconOffset)
          .attr("y", -translateY + that.iconSize + titleHeight)
          .append("tspan")
          .attr("x", -translateX + that.iconOffset)
          .attr("dy", "1.2em")
          .style("text-align", "left")
          .text(function () {
            const colName = gData.col;
            return `col: ${colName}`;
          });

        container.node().appendChild(svg.node());

        container.select("div").remove();
        container.select("details").remove();

        container.style(
          "transform",
          `translate(${-width / 2}px,${
            -height / 2 + that.rectHeightOffset + titleHeight / 2
          }px)`
        );
      });
    },
    drawTree(newVal) {
      //console.log(1);

      const that = this;
      const treeInfo = newVal;

      const svgContainer = d3.select("#tree-svg-container");
      const containerWidth = parseInt(svgContainer.style("width"), 10);
      const containerHeight = parseInt(svgContainer.style("height"), 10);
      const width = containerWidth;
      const height = containerHeight;

      const offsetX = width * 0.01;
      const offsetY = height * 0.05;

      const svg = svgContainer
        .select("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [
          -offsetX,
          -height / 2,
          width + offsetX + this.vegaLiteWidth,
          height + offsetY * 2,
        ])
        .attr("style", "width: 100%; height: 100%;")
        .attr("overflow", "visible");
      svg.selectChildren("g").remove();
      const root = d3.hierarchy(treeInfo);
      const tree = d3
        .tree()
        .nodeSize([this.vegaLiteHeight * 2, this.vegaLiteWidth * 2.2]);

      tree(root);
      const linkData = this.linkData;

      const realLinkData = [];
      root.links().forEach((d) => {
        const sourceId = d.source.data.name;
        const targetId = d.target.data.name;

        const data = linkData.find(
          (d) =>
            (d.source === sourceId && d.target === targetId) ||
            (d.source === targetId && d.target === sourceId)
        );
        if (data) {
          const type = data.type;
          realLinkData.push({ ...d, type: type });
        } else {
          realLinkData.push({ ...d, type: "root" });
        }
      });

      const link = svg
        .append("g")
        .attr("class", "link-group")
        .attr("fill", "none")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.6)
        .attr("stroke-width", 1.5)
        .selectAll()
        .data(realLinkData)
        .join("path");
      link.each(function (d) {
        const type = d.type;
        const path = d3.select(this);
        switch (type) {
          case "root":
            path.attr(
              "d",
              // 水平路径，颠倒
              d3
                .linkHorizontal()
                .x((d) => d.y)
                .y((d) => d.x)
            );
            break;
          case "siblings":
            // 普通实线
            path
              .attr(
                "d",
                // 水平路径，颠倒
                d3
                  .linkHorizontal()
                  .x((d) => d.y)
                  .y((d) => d.x)
              )
              .attr("stroke-width", 5);
            break;
          case "state":
            path
              .attr(
                "d",
                // 水平路径，颠倒
                d3
                  .linkHorizontal()
                  .x((d) => d.y)
                  .y((d) => d.x)
              )
              .style("stroke-dasharray", "20,5");
            // .attr("stroke-opacity", "0.8");
            break;
          case "parent-child":
            // 锥形线
            path
              .attr("fill", "#aaa")
              .attr("stroke", "none")
              .attr("d", function (d) {
                let point1 = [];
                let point2 = [];
                const name1 = d.source.data.name;
                const name2 = d.target.data.name;
                if (name1.length < name2.length) {
                  point1 = [d.source.y, d.source.x];
                  point2 = [d.target.y, d.target.x];
                } else {
                  point1 = [d.target.y, d.target.x];
                  point2 = [d.source.y, d.source.x];
                }

                const widthAtStart = 30;
                const widthAtEnd = 1;

                const angle = Math.atan2(
                  point2[1] - point1[1],
                  point2[0] - point1[0]
                );

                const p1 = [
                  point1[0] + widthAtStart * Math.sin(angle),
                  point1[1] - widthAtStart * Math.cos(angle),
                ];

                const p2 = [
                  point1[0] - widthAtStart * Math.sin(angle),
                  point1[1] + widthAtStart * Math.cos(angle),
                ];

                const p3 = [
                  point2[0] - widthAtEnd * Math.sin(angle),
                  point2[1] + widthAtEnd * Math.cos(angle),
                ];

                const p4 = [
                  point2[0] + widthAtEnd * Math.sin(angle),
                  point2[1] - widthAtEnd * Math.cos(angle),
                ];

                return `M${p1} L${p2} L${p3} L${p4} Z`;
              });
            break;
          case "same-name":
            // s-a: 虚线
            path
              .attr(
                "d",
                // 水平路径，颠倒
                d3
                  .linkHorizontal()
                  .x((d) => d.y)
                  .y((d) => d.x)
              )
              .attr("stroke-width", 5)
              .style("stroke-dasharray", "10,5");
            break;
        }
      });

      const nodeG = svg.append("g").attr("class", "node-group");

      const containerGroup = nodeG
        .selectAll()
        .data(root.descendants())
        .join("g")
        .attr("transform", (d) => `translate(${d.y},${d.x})`);

      containerGroup
        .filter((d) => d.data.name === "root")
        .append("use")
        .attr("href", "#defs-start")
        .attr("width", this.outIconSize)
        .attr("height", this.outIconSize)
        .attr(
          "transform",
          `translate(${-this.outIconSize / 2},${-this.outIconSize / 2})`
        )
        .attr("color", "#999")
        .attr("fill", "#fff");

      containerGroup
        .filter((d) => d.data.name !== "root")
        .append("rect")
        .attr("class", "rect vega-lite-border")
        .attr("fill", "#fff")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5)
        .attr("cursor", "pointer")
        .on("mouseover", function () {
          const g = d3.select(this.parentNode);
          const gData = g.datum().data.forceData;

          d3.select(this).classed("center-highlight", true);
          g.select(".rect-title").classed("center-highlight", true);
          that.hoverIndex = {
            id: gData.id,
            state: gData.state,
            col: gData.col,
            row: gData.row,
          };
        })
        .on("mouseout", function () {
          const g = d3.select(this.parentNode);
          const gData = g.datum().data.forceData;
          if (that.selectedNode.id !== g.datum().data.name) {
            d3.select(this).classed("center-highlight", false);
            g.select(".rect-title").classed("center-highlight", false);
          }

          that.hoverIndex = {
            id: null,
            state: gData.state,
            col: null,
            row: null,
          };
        })
        .on("click", function () {
          const gData = d3.select(this.parentNode).datum().data.forceData;

          that.selectedNode = {
            id: gData.id,
            state: gData.state,
            insightIndex: gData.insightIndex,
            "insight-list": gData["insight-list"],
            col: gData.col,
            row: gData.row,
          };
        });

      const titleGroup = containerGroup
        .filter((d) => d.data.name !== "root")
        .append("rect")
        .attr("class", "rect-title")
        .attr("fill", "#e9ecef")
        .attr("stroke", "#ccc")
        .attr("stroke-width", 1.5)
        .attr("pointer-events", "none");

      const nameGroup = containerGroup
        .filter((d) => d.data.name !== "root")
        .append("text")
        .attr("class", "title-text title-name")
        .attr("pointer-events", "none")
        .style("user-select", "none")
        .attr("fill", "#555")
        .attr("font-weight", 600);

      const stateGroup = containerGroup
        .filter((d) => d.data.name !== "root")
        .append("text")
        .attr("class", "title-text title-state")
        .attr("pointer-events", "none")
        .style("user-select", "none")
        .attr("fill", "#555")
        .attr("font-weight", 600);

      const descriptionGroup = containerGroup
        .filter((d) => d.data.name !== "root")
        .append("text")

        .attr("class", "title-text title-description")
        .attr("pointer-events", "none")
        .attr("fill", "#555")
        .style("user-select", "none");

      const vegaLiteContainerGroup = containerGroup
        .filter((d) => d.data.name !== "root")
        .append("g")
        .attr("class", "vega-lite-container");

      containerGroup.each(function () {
        const g = d3.select(this);
        if (g.datum().data.name !== "root") that.drawVegaLite(g);
      });

      // node
      //   .append("text")
      //   .attr("dy", "0.31em")
      //   .attr("x", (d) => (d.children ? -6 : 6))
      //   .attr("text-anchor", (d) => (d.children ? "end" : "start"))
      //   .text((d) => d.data.name)
      //   .clone(true)
      //   .lower()
      //   .attr("stroke", "white");
      const zoomFunction = d3
        .zoom()
        .scaleExtent([0.1, 8])
        .on("zoom", function (event) {
          svg.attr("transform", event.transform);
        });

      svgContainer.call(zoomFunction);
    },
  },
  watch: {
    hoverIndex(newVal) {
      if (this.focusState) {
        if (newVal.state === this.focusState) {
          this.$store.dispatch("table/convertCheckSelection", {
            mode: "hovered",
            data: newVal.id
              ? new Map().set(newVal.id, {
                  col: newVal.col,
                  row: newVal.row,
                })
              : null,
          });
        } else {
          this.$store.dispatch("table/convertCrossStateHoverSelection", {
            data: newVal.id
              ? {
                  id: newVal.id,
                  col: newVal.col,
                  row: newVal.row,
                }
              : null,
          });
        }
      }
    },
    selectedNode(newVal, oldVal) {
      const nodeGroup = d3
        .select("#tree-svg-container")
        .select("svg")
        .select("g.node-group")
        .selectChildren("g");
      // 边框高亮
      if (oldVal) {
        const id = oldVal.id;
        nodeGroup
          .filter((d) => d.data.name === id)
          .selectChildren(".vega-lite-border, .rect-title")
          .classed("center-highlight", false);
      }
      if (newVal) {
        this.focusState = newVal.state;
        const id = newVal.id;
        nodeGroup
          .filter((d) => d.data.name === id)
          .selectChildren(".vega-lite-border, .rect-title")
          .classed("center-highlight", true);
      }

      if (newVal.id !== oldVal.id) {
        if (newVal.state !== oldVal.state) {
          this.$store.dispatch(
            "table/loadHeadData",
            this.allTableInfo[newVal.state]
          );
        }
        this.$store.dispatch("table/convertCheckSelection", {
          mode: "clicked",
          data: new Map().set(newVal.id, {
            col: newVal.col,
            row: newVal.row,
          }),
        });
        if (newVal["insight-list"].length > 1) {
          if (this.hidePanelMode) {
            if (this.showMoreIcon) {
              this.showMoreIcon = false;

              this.$nextTick(() => {
                setTimeout(() => {
                  this.showMoreIcon = true;
                }, 150);
              });
            } else {
              this.showMoreIcon = true;
            }
          } else {
            if (this.showMorePanel) {
              this.showMorePanel = false;

              this.$nextTick(() => {
                setTimeout(() => {
                  this.showMorePanel = true;
                }, 150);
              });
            } else {
              this.showMorePanel = true;
            }
          }
        } else {
          this.showMorePanel = false;
          this.showMoreIcon = false;
        }
      }
    },
  },
  mounted() {
    this.nodeIdMap = this.forceData.nodeIdMap;
    this.linkData = this.forceData.linkData;
    this.drawTree(this.forceData.tree);
  },
};
</script>

<style scoped>
.container {
  position: relative;
}
.container,
#tree-svg-container {
  width: 100%;
  height: 100%;
}
.showMorePanelBox {
  position: absolute;
  top: 0;
  right: 0;
}
.more-icon {
  fill: #545b77;
  cursor: pointer;
  width: 25px;
  height: 25px;
}

.more-box {
  position: fixed;
  top: 7%;
  right: 1%;
}
</style>
<!-- Animation -->
<style scoped>
.slide-enter-active {
  transition: all 70ms ease-out;
}

.slide-leave-active {
  transition: all 70ms ease-in;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(200px); /* 初始状态和最终状态 */
}

.slide-enter-to,
.slide-leave-from {
  transform: translateX(0); /* 平移隐藏 */
}
</style>
