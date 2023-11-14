import "element-plus/dist/index.css";
import "./style.css";
import { createApp } from "vue";
import App from "./App.vue";

import router from "./router.js";
import store from "./store/index.js";

import BaseCard from "./components/ui/BaseCard.vue";
import BaseButton from "./components/ui/BaseButton.vue";
import * as d3 from "d3";
import vegaEmbed from "vega-embed";
import * as echarts from "echarts";
import echarts_theme from "@/assets/echarts_theme.json";

echarts.registerTheme("myTheme", echarts_theme);
// 设置全局变量
window.d3 = d3;
window.vegaEmbed = vegaEmbed;
window.echarts = echarts;

const app = createApp(App);
app.use(router);
app.use(store);
app.component("BaseCard", BaseCard);
app.component("BaseButton", BaseButton);

app.mount("#app");
