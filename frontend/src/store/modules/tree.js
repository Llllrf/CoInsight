export default {
  namespaced: true,
  state() {
    return {
      forceData: null,
      allTableInfo: null,

      // load state
      loading: false,
      error: {
        state: false,
        message: "",
      },
    };
  },
  getters: {
    forceData(state) {
      return state.forceData;
    },
    allTableInfo(state) {
      return state.allTableInfo;
    },
    loading(state) {
      return state.loading;
    },
    error(state) {
      return state.error;
    },
  },
  mutations: {
    setForceData(state, payload) {
      state.forceData = payload;
    },
    setAllTableInfo(state, payload) {
      state.allTableInfo = payload;
    },
    setLoading(state, payload) {
      state.loading = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
  },
  actions: {
    handleTableData(context, payload) {
      const data = payload;
      // 保存传来的所有table信息
      context.commit("setAllTableInfo", data);
    },
    loadTableInfo(context, payload) {
      const stateList = payload.stateList;
      const baseUrl = context.rootGetters["force/baseUrl"];
      const url = baseUrl + "/photo";
      context.commit("setLoading", true);

      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          stateList,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("RESPONSE ERROR");
          }
          return response.json();
        })
        .then((data) => {
          context.dispatch("handleTableData", data);
          context.commit("setError", {
            state: false,
            message: "",
          });
          context.commit("setLoading", false);
        })
        .catch((error) => {
          context.commit("setError", {
            state: true,
            message: error.message,
          });
          context.commit("setLoading", false);
          console.error("error:", error.message);
        });
    },
  },
};
