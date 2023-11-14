<template>
  <div id="table-container"></div>
</template>
<script>
export default {
  data() {
    return {
      rowName: null,
      colName: null,
      rowDepth: null,
      colDepth: null,
      rowNum: null,
      colNum: null,
      rowDict: null,
      colDict: null,

      durationTime: 150,
    };
  },
  methods: {
    resetData(data) {
      const that = this;
      const container = d3.select("#table-container");

      const preTable = container.selectChild("table.mini-table");

      if (!preTable.empty()) {
        preTable
          .style("opacity", 1)
          .transition()
          .duration(this.durationTime * 1.5)
          .style("opacity", 0)
          .on("end", function () {
            d3.select(this).remove();

            if (data) {
              that.rowNum = data.rowNum;
              that.colNum = data.colNum;
              that.rowDepth = data.rowDepth;
              that.colDepth = data.colDepth;

              that.createTable();
              that.addHighlightBorder(that.checkedArea, true, false);
              that.addHighlightBorder(that.clickedArea, true, true);
            }
          });
      } else {
        if (data) {
          that.rowNum = data.rowNum;
          that.colNum = data.colNum;
          that.rowDepth = data.rowDepth;
          that.colDepth = data.colDepth;

          that.createTable();
          that.addHighlightBorder(that.checkedArea, true, false);
          that.addHighlightBorder(that.clickedArea, true, true);
        }
      }
    },
    createTable() {
      const that = this;
      const container = d3.select("#table-container");

      let tooltip = container.selectChild("div.tooltip");
      if (tooltip.empty()) {
        tooltip = container
          .append("div")
          .attr("class", "tooltip")
          .style("opacity", 0);
      } else {
        tooltip.style("opacity", 0);
      }

      const table = container
        .append("table")
        .attr("class", "mini-table")

        .style("user-select", "none");

      table
        .style("opacity", 0)
        .transition()
        .duration(this.durationTime * 1.5)
        .style("opacity", 1);

      const width = parseInt(container.style("width"), 10);
      const height = parseInt(container.style("height"), 10);

      const cellWidth = width / (this.colNum + this.rowDepth);
      const cellHeight = height / (this.rowNum + this.colDepth);

      // Create table headers
      const thead = table.append("thead");
      for (let i = 0; i < this.colDepth; i++) {
        thead.append("tr");
      }

      const tbody = table.append("tbody");

      thead
        .select("tr")
        .append("th")
        .attr("colspan", this.rowDepth)
        .attr("rowspan", this.colDepth)
        .attr("width", cellWidth)
        .attr("height", cellHeight);

      this.tableData.cols.forEach((colCell) => {
        addTopCell(colCell, thead, 1, tooltip);
      });

      const tr = tbody.append("tr");
      this.tableData.rows.forEach((rowCell) => {
        addLeftCell(rowCell);
      });
      // add heatValues
      const heatValues = this.heatValues;
      const color = d3
        .scaleSequential(d3.interpolateReds)
        .domain([0, d3.max(heatValues.flat()) + 1]);
      tbody
        .selectAll("td")
        .data(heatValues.flat())
        .style("background-color", (d) => {
          let rgb = d3.rgb(color(d)).brighter(0.2);
          return `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, 0.6)`;
        });

      table
        .selectAll("th")
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave);

      function mouseover(event, d) {
        if (d) {
          tooltip.transition().duration(300).style("opacity", 1);

          d3.select(this).classed("cell-border-tooltip-highlight", true);
        }
      }
      function mousemove(event, d) {
        if (d) {
          tooltip
            .html(d.name)
            .style("left", event.x + "px")
            .style("top", event.y - 30 + "px");
        }
      }
      function mouseleave(event, d) {
        if (d) {
          tooltip.transition().duration(300).style("opacity", 0);

          d3.select(this).classed("cell-border-tooltip-highlight", false);
        }
      }

      function addLeftCell(cell) {
        const tr = tbody.selectAll("tr").filter(function (d, i, nodes) {
          return i === nodes.length - 1;
        });
        tr.append("th")
          .data([cell])
          .attr("rowspan", cell.rowSpan[1] - cell.rowSpan[0] + 1)
          .attr("width", cellWidth)
          .attr("height", cellHeight);
        if (cell.children) {
          cell.children.forEach((cell) => {
            addLeftCell(cell);
          });
        } else {
          for (let i = 0; i < that.colNum; i++) {
            tr.append("td").attr("width", cellWidth).attr("height", cellHeight);
          }
          tbody.append("tr");
        }
      }

      function addTopCell(cell, thead, depth) {
        const tr = thead.select(`tr:nth-child(${depth})`);
        tr.append("th")
          .data([cell])
          .attr("colspan", cell.colSpan[1] - cell.colSpan[0] + 1)
          .attr("width", cellWidth)
          .attr("height", cellHeight);
        if (cell.children) {
          cell.children.forEach((cell) => {
            addTopCell(cell, thead, depth + 1);
          });
        }
      }
    },

    addHighlightBackground(checkedArea, mode) {
      if (checkedArea) {
        const tbody = d3
          .select("#table-container")
          .select("table")
          .select("tbody");
        for (let [key, value] of checkedArea) {
          const rowSpan = value.rowSpan;
          const colSpan = value.colSpan;
          const trGroup = tbody.selectChildren("tr").filter(function (d, i) {
            return i >= rowSpan[0] && i <= rowSpan[1];
          });
          trGroup
            .selectChildren("td")
            .filter(function (d, i) {
              return i >= colSpan[0] && i <= colSpan[1];
            })
            .classed("cell-background-highlight", mode);
        }
      }
    },
    addHighlightBorder(checkedArea, mode, clicked) {
      const cssSuffix = clicked ? "-clicked" : "";
      if (checkedArea) {
        const tbody = d3
          .select("#table-container")
          .select("table")
          .select("tbody");
        for (let [key, value] of checkedArea) {
          const rowSpan = value.rowSpan;
          const colSpan = value.colSpan;
          const trGroup = tbody.selectChildren("tr").filter(function (d, i) {
            return i >= rowSpan[0] && i <= rowSpan[1];
          });
          const tdGroup = trGroup.selectChildren("td").filter(function (d, i) {
            return i >= colSpan[0] && i <= colSpan[1];
          });

          addHorizontalBorder(colSpan, tdGroup);
          addVerticalBorder(colSpan, rowSpan, trGroup);
        }
      }

      function addHorizontalBorder(colSpan, tdGroup) {
        const colWidth = colSpan[1] - colSpan[0];

        tdGroup.each(function (d, i) {
          // 'this' is the current group
          if (i == 0)
            d3.select(this).classed(
              "cell-border-left-highlight" + cssSuffix,
              mode
            );
          if (i === colWidth)
            d3.select(this).classed(
              "cell-border-right-highlight" + cssSuffix,
              mode
            );
        });
      }
      function addVerticalBorder(colSpan, rowSpan, trGroup) {
        const rowWidth = rowSpan[1] - rowSpan[0];

        trGroup.each(function (d, i) {
          if (i == 0) {
            d3.select(this)
              .selectAll("td")
              .filter(function (d, i) {
                return i >= colSpan[0] && i <= colSpan[1];
              })
              .classed("cell-border-top-highlight" + cssSuffix, mode);
          }
          if (i === rowWidth) {
            d3.select(this)
              .selectAll("td")
              .filter(function (d, i) {
                return i >= colSpan[0] && i <= colSpan[1];
              })
              .classed("cell-border-bottom-highlight" + cssSuffix, mode);
          }
        });
      }
    },
  },
  computed: {
    tableData() {
      return this.$store.getters["table/tableData"];
    },
    checkedArea() {
      return this.$store.getters["table/checkedArea"];
    },
    hoveredArea() {
      return this.$store.getters["table/hoveredArea"];
    },
    clickedArea() {
      return this.$store.getters["table/clickedArea"];
    },
    heatValues() {
      return this.$store.getters["table/heatValues"];
    },
    crossStateHoverArea() {
      return this.$store.getters["table/crossStateHoverArea"];
    },
  },
  watch: {
    tableData(newVal) {
      this.resetData(newVal);
    },
    clickedArea: {
      handler(newVal, oldVal) {
        this.addHighlightBorder(oldVal, false, true);
        this.addHighlightBorder(newVal, true, true);
      },
      deep: true,
    },
    checkedArea: {
      handler(newVal, oldVal) {
        this.addHighlightBorder(oldVal, false, false);
        this.addHighlightBorder(newVal, true, false);
      },
      deep: true,
    },
    hoveredArea: {
      handler(newVal, oldVal) {
        if (oldVal) this.addHighlightBackground(oldVal, false);
        if (newVal) this.addHighlightBackground(newVal, true);
      },
      deep: true,
    },

    crossStateHoverArea(newVal, oldVal) {
      const that = this;
      if (oldVal) {
        const rowSpans = oldVal.rowSpans;
        const colSpans = oldVal.colSpans;

        addCorssStateHighlight(rowSpans, colSpans, false);
      }
      if (newVal) {
        const rowSpans = newVal.rowSpans;
        const colSpans = newVal.colSpans;
        addCorssStateHighlight(rowSpans, colSpans, true);
      }

      function addCorssStateHighlight(rowSpans, colSpans, mode) {
        const checkedArea = new Map();
        if (colSpans.length === 1) {
          rowSpans.forEach((rowSpan, index) => {
            checkedArea.set(index, {
              rowSpan: rowSpan,
              colSpan: colSpans[0],
            });
          });
        } else {
          colSpans.forEach((colSpan, index) => {
            checkedArea.set(index, {
              rowSpan: rowSpans[0],
              colSpan: colSpan,
            });
          });
        }

        that.addHighlightBackground(checkedArea, mode);
      }
    },
  },
  mounted() {
    this.resetData(this.tableData);
  },
};
</script>
<style scoped>
#table-container {
  width: 100%;
  height: 100%;
}
</style>
<style lang="less">
table.mini-table {
  border-collapse: collapse;
  // border-spacing: 0;
  // border-collapse: separate;
  border: 0.5px solid #545b77;
}

table.mini-table {
  th {
    border: 0.5px solid #545b77;
  }
  td {
    // border: 1px dashed #ccc;
    // border: 0.5px solid #ccc;
    border: none;
    transition: background-color 0.3s;
  }

  th.cell-border-tooltip-highlight {
    box-shadow: inset 0 0 0 1px #555;
    background-color: #ddd;
  }
  td.cell-border-left-highlight-clicked {
    border-left: 3px dashed #636c8d;
  }
  td.cell-border-right-highlight-clicked {
    border-right: 3px dashed #636c8d;
  }

  td.cell-border-top-highlight-clicked {
    border-top: 2px dotted #636c8d;
  }
  td.cell-border-bottom-highlight-clicked {
    border-bottom: 2px dotted #636c8d;
  }

  td.cell-border-left-highlight {
    border-left: 2px solid #636c8d;
  }
  td.cell-border-right-highlight {
    border-right: 2px solid #636c8d;
  }

  td.cell-border-top-highlight {
    border-top: 2px solid #636c8d;
  }
  td.cell-border-bottom-highlight {
    border-bottom: 2px solid rgb(99, 108, 141);
  }
  td.cell-background-highlight {
    // mix-blend-mode: difference;
    // filter: sepia(1) hue-rotate(180deg) saturate(2);
    background-color: rgba(99, 108, 141, 0.2) !important;
  }
}
.tooltip {
  background-color: #fff;
  border: 2px solid #555;
  border-radius: 5px;
  padding: 5px;
  width: fit-content;
  height: fit-content;
  position: fixed;
  z-index: 10;
  user-select: none;
  pointer-events: none;
}
</style>
