export default {
  namespaced: true,
  state() {
    return {
      tableData: null,
      rowDict: null,
      colDict: null,
      checkedArea: null,
      hoveredArea: null,
      clickedArea: null,
      heatValues: null,
      // cross state highlight
      crossStateHoverArea: null,
      rowNameList: null,
      colNameList: null,
    };
  },
  getters: {
    tableData(state) {
      return state.tableData;
    },
    rowDict(state) {
      return state.rowDict;
    },
    colDict(state) {
      return state.colDict;
    },
    checkedArea(state) {
      return state.checkedArea;
    },
    hoveredArea(state) {
      return state.hoveredArea;
    },
    clickedArea(state) {
      return state.clickedArea;
    },
    heatValues(state) {
      return state.heatValues;
    },
    crossStateHoverArea(state) {
      return state.crossStateHoverArea;
    },
    rowNameList(state) {
      return state.rowNameList;
    },
    colNameList(state) {
      return state.colNameList;
    },
  },
  mutations: {
    setTableData(state, payload) {
      state.tableData = payload;
    },
    setRowDict(state, payload) {
      state.rowDict = payload;
    },
    setColDict(state, payload) {
      state.colDict = payload;
    },
    setCheckedArea(state, payload) {
      state.checkedArea = payload;
    },
    setHoveredArea(state, payload) {
      state.hoveredArea = payload;
    },
    setClickedArea(state, payload) {
      state.clickedArea = payload;
    },
    setHeatValues(state, payload) {
      state.heatValues = payload;
    },
    setCrossStateHoverArea(state, payload) {
      state.crossStateHoverArea = payload;
    },
    setRowNameList(state, payload) {
      state.rowNameList = payload;
    },
    setColNameList(state, payload) {
      state.colNameList = payload;
    },
  },

  actions: {
    convertCrossStateHoverSelection(context, payload) {
      const data = payload.data;
      let result = {};
      if (data) {
        let rowName = data.row;
        let colName = data.col;
        const id = data.id;
        result.id = id;

        const rowDict = context.getters.rowDict;
        const colDict = context.getters.colDict;
        const rowNameList = context.getters.rowNameList;
        const colNameList = context.getters.colNameList;

        [colName, rowName] = adjustName(
          rowName,
          colName,
          rowNameList,
          colNameList
        );

        let colSpan = null;
        if (colName === "_") {
          colSpan = [[0, context.getters.tableData.colNum - 1]];
        } else {
          colSpan = findCrossStateSpan(colName, colDict, "col");
        }
        result.colSpans = colSpan;

        let rowSpan = null;
        if (rowName === "_") {
          rowSpan = [[0, context.getters.tableData.rowNum - 1]];
        } else {
          rowSpan = findCrossStateSpan(rowName, rowDict, "row");
        }
        result.rowSpans = rowSpan;
      } else {
        result = null;
      }

      context.commit("setCrossStateHoverArea", result);

      function adjustName(rowName, colName, rowNameList, colNameList) {
        let adjustedColPath = null;
        let adjustedRowPath = null;
        const path2Row = [];
        const path2Col = [];
        if (colName !== "_") {
          const colPath = colName.split("_");
          adjustedColPath = colPath.filter((name) => {
            if (colNameList.has(name)) {
              return true;
            } else {
              path2Row.push(name);
              return false;
            }
          });
        }
        if (rowName !== "_") {
          const rowPath = rowName.split("_");
          adjustedRowPath = rowPath.filter((name) => {
            if (rowNameList.has(name)) {
              return true;
            } else {
              path2Col.push(name);
              return false;
            }
          });
        }
        if (path2Row.length > 0) {
          if (adjustedRowPath) {
            adjustedRowPath.push(...path2Row);
          } else {
            adjustedRowPath = [...path2Row];
          }
        }
        if (path2Col.length > 0) {
          if (adjustedColPath) {
            adjustedColPath.push(...path2Col);
          } else {
            adjustedColPath = [...path2Col];
          }
        }

        return [
          adjustedColPath ? adjustedColPath : "_",
          adjustedRowPath ? adjustedRowPath : "_",
        ];
      }

      function findCrossStateSpan(path, dict, mode) {
        //const currentName = path[0];
        const span = [];
        const dictKeySet = new Set(Array.from(Object.keys(dict)));
        const commonElement = path.filter((name) => dictKeySet.has(name));

        if (commonElement.length > 0) {
          const currentName = commonElement[0];
          const childDict = dict[currentName].children;
          const newPath = path.filter((name) => name !== currentName);

          if (newPath.length > 0) {
            if (childDict) {
              span.push(...findCrossStateSpan(newPath, childDict, mode));
            }
          } else {
            const target = mode === "row" ? "rowSpan" : "colSpan";

            return [dict[currentName][target]];
          }
        } else {
          for (const nameInfo of Object.values(dict)) {
            if (nameInfo.children) {
              span.push(...findCrossStateSpan(path, nameInfo.children, mode));
            }
          }
        }
        return span;
      }
    },
    convertCheckSelection(context, payload) {
      let result = new Map();
      const data = payload.data;
      const mode = payload.mode;

      if (data) {
        for (let [key, value] of data.entries()) {
          const rowName = value.row;
          const colName = value.col;
          const rowDict = context.getters.rowDict;
          const colDict = context.getters.colDict;

          let colSpan = null;
          if (colName === "_") {
            colSpan = [0, context.getters.tableData.colNum - 1];
          } else {
            colSpan = findSpan(colName, colDict, "col");
          }
          let rowSpan = null;
          if (rowName === "_") {
            rowSpan = [0, context.getters.tableData.rowNum - 1];
          } else {
            rowSpan = findSpan(rowName, rowDict, "row");
          }

          result.set(key, {
            rowSpan: rowSpan,
            colSpan: colSpan,
          });
        }
      } else {
        result = null;
      }

      if (mode === "checked") context.commit("setCheckedArea", result);
      else if (mode === "hovered") context.commit("setHoveredArea", result);
      else if (mode === "clicked") context.commit("setClickedArea", result);

      function findSpan(name, dict, mode) {
        const path = name.split("_");
        const target = mode === "row" ? "rowSpan" : "colSpan";
        let info = dict[path[0]];
        for (let i = 1; i < path.length; i++) {
          info = info.children[path[i]];
        }
        return info[target];
      }
    },

    loadHeadData(context, payload) {
      if (payload) {
        const data = payload.structure;

        context.commit("setTableData", data);
        context.commit("setRowDict", listToDict(data.rows));
        context.commit("setColDict", listToDict(data.cols));
        context.commit("setRowNameList", getNameList(data.rows));
        context.commit("setColNameList", getNameList(data.cols));
        context.commit("setHeatValues", payload.heat);
      } else {
        context.commit("setTableData", null);
      }
      function listToDict(list) {
        let obj = {};
        for (let item of list) {
          if ("children" in item && item.children) {
            // Don't modify the existing list, but create a new dict for children
            let childObj = listToDict(item.children);
            obj[item.name] = { ...item, children: childObj };
          } else {
            obj[item.name] = item;
          }
        }
        return obj;
      }
      function getNameList(list) {
        let nameList = new Set();
        for (const item of list) {
          nameList.add(item.name);
          if (item.children) {
            nameList = new Set([...nameList, ...getNameList(item.children)]);
          }
        }
        return nameList;
      }
    },
  },
};
