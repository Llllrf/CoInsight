<template>
  <div class="container">
    <svg class="svg">
      <defs>
        <filter id="rect-shadow">
          <feDropShadow
            dx="0"
            dy="0"
            stdDeviation="2"
            flood-color="#545b77"
            flood-opacity="0.8"
          />
        </filter>
      </defs>
      <rect
        x="100"
        y="100"
        width="300"
        height="300"
        fill="#fff"
        stroke="#D5DAEC"
        filter="url(#rect-shadow)"
      ></rect>
    </svg>
  </div>
</template>
<script>
export default {
  data() {
    return {
      rowName: null,
      colName: null,
      rowDict: null,
      colDict: null,
      insightIconSize: 30,
    };
  },
  methods: {},
  computed: {},
  watch: {},
  mounted() {},
};
</script>
<style scoped>
.container {
  width: 100%;
  height: 100%;
}
#echarts-container {
  width: 100%;
  height: 100%;
}

.svg {
  width: 100%;
  height: 100%;
}
</style>
