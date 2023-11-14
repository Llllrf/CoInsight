<template>
  <div :class="[mode, { inset: inset }]">
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    mode: {
      type: String,
      required: false,
      default: "card",
    },
    inset: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  border-radius: 2px;
}

.inset {
  box-shadow: inset 1px 1px 5px #4444442a, inset -1px -1px 5px #4444442a;
}

.flat {
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 2px;
}
</style>
