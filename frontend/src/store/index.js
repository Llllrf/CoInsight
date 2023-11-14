import { createStore } from "vuex";
import forceModule from "./modules/force";
import tableModule from "./modules/table";
import treeModule from "./modules/tree";
const store = createStore({
  modules: {
    force: forceModule,
    table: tableModule,
    tree: treeModule,
  },
});

export default store;
