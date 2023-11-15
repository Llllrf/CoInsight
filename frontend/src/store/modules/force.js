import { fetchPOST, fetchGET } from "@/services/fetch";

export default {
  namespaced: true,
  state() {
    return {
      baseUrl: "http://10.1.114.103:5001",
      // baseUrl: "http://localhost:3004",

      // load state
      loading: false,
      error: {
        state: true,
        message: "",
      },
      // statistic graph data, single state
      focusState: null,
      totalData: null,
      selectedData: null,

      // statistic graph data, multi state
      scoreSelectionMaps: new Map(),

      // force graph, data loading
      allStatesData: null,
      stateLinksMap: null,
    };
  },
  getters: {
    baseUrl(state) {
      return state.baseUrl;
    },
    totalData(state) {
      return state.totalData;
    },
    selectedData(state) {
      return state.selectedData;
    },

    scoreSelectionMaps(state) {
      return state.scoreSelectionMaps;
    },
    allStatesData(state) {
      return state.allStatesData;
    },
    stateLinksMap(state) {
      return state.stateLinksMap;
    },
    loading(state) {
      return state.loading;
    },
    error(state) {
      return state.error;
    },

    focusState(state) {
      return state.focusState;
    },
  },
  mutations: {
    setTotalData(state, payload) {
      state.totalData = payload;
    },
    setSelectedData(state, payload) {
      state.selectedData = payload;
    },

    setAllStatesData(state, payload) {
      state.allStatesData = payload;
    },
    setAllStateLinksMap(state, payload) {
      state.stateLinksMap = payload;
    },
    setLoading(state, payload) {
      state.loading = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    setFocusState(state, payload) {
      state.focusState = payload;
    },
  },
  actions: {
    setStatisticGraph(context, payload) {
      const state = payload.state;
      const data = payload.data;
      // reset total data and focus state
      context.commit("setTotalData", data);
      context.commit("setFocusState", state);
    },
    uploadData(context, payload) {
      const formData = new FormData();
      formData.append("file", payload);
      const url = context.getters.baseUrl + "/upload";

      fetchPOST(url, { data: formData, type: "form" }, context);
    },

    // load force and table data
    loadData(context, payload) {
      // const file = "test_data/result_0826_S1.json";
      // const url = `data/${file}`;

      const mode = payload.mode;
      let route = null;
      switch (mode) {
        case "back":
          route = "back";
          break;
        case "forward":
          route = "state";
      }
      const targetState = payload.state;
      const url = context.getters.baseUrl + `/${route}/` + targetState;

      fetchGET(url, null, context);
    },

    handleData(context, payload) {
      console.log("sourceData:", payload);
      const data = payload;

      // get table data
      const tableData = data.table;

      context.dispatch("table/loadHeadData", tableData, { root: true });

      // 获取不同state的对应的links和nodes map
      const allStatesNodes = d3.group(data.graph.nodes, (d) => d.state);
      const allStatesLinks = getLinksByNodes(allStatesNodes, data.graph.links);
      const allStatesData = new Map();

      Array.from(allStatesNodes.keys()).forEach((state) => {
        allStatesData.set(state, {
          links: allStatesLinks.get(state),
          nodes: allStatesNodes.get(state),
        });
      });

      context.commit("setAllStatesData", allStatesData);
      const stateLinksMap = new Map();
      const stateLinks = data["state_links"];

      Object.keys(stateLinks).forEach((nodeId) => {
        const stateObj = stateLinks[nodeId];
        const stateMaps = new Map();
        Object.keys(stateObj).forEach((state) => {
          stateMaps.set(state, stateObj[state]);
        });
        stateLinksMap.set(nodeId, stateMaps);
      });

      context.commit("setAllStateLinksMap", stateLinksMap);

      function getLinksByNodes(filteredNodes, allLinks) {
        const allStatesLinks = new Map();
        Array.from(filteredNodes.keys()).forEach((state) =>
          allStatesLinks.set(state, [])
        );
        allLinks.forEach((link) => {
          for (let [state, nodes] of filteredNodes.entries()) {
            if (
              nodes.find((d) => d.id === link.source) &&
              nodes.find((d) => d.id === link.target)
            ) {
              allStatesLinks.get(state).push(link);
              break;
            }
          }
        });
        return allStatesLinks;
      }
    },
  },
};
