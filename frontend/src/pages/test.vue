<template>
  <div class="container">
    <!-- <ForceDirectedGraphOld></ForceDirectedGraphOld> -->
    <BarChart></BarChart>
  </div>
</template>

<script>
import BarChart from "@/components/vega-lite-graph/BarChart.vue";
import * as echarts from "echarts";
import MiniTable from "../components/control-panel-graph/MiniTable.vue";

export default {
  components: {
    BarChart,

    MiniTable,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.container {
  height: 100%;
  width: 100%;
}
</style>
