<template>
  <button v-if="!link" :class="[mode, { inset: inset }]">
    <slot></slot>
  </button>
  <router-link v-else :to="to" :class="[mode, { inset: inset }]">
    <slot> </slot>
  </router-link>
</template>

<script>
export default {
  props: {
    mode: {
      type: String,
      required: false,
      default: null,
    },
    link: {
      type: Boolean,
      required: false,
      default: false,
    },
    to: {
      type: String,
      required: false,
      default: "/",
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
button,
a {
  /* font-size: 14px; */
  font-size: 1.1vw;
  text-decoration: none;
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(
    119.06deg,
    #3fdfac 10.71%,
    #44e1bf 60.37%,
    #46dfc3 103.14%
  );
  border: none;
  color: white;
  cursor: pointer;
}

a:hover,
a:active,
button:hover,
button:active {
  background: linear-gradient(
    119.06deg,
    #3bd0a1 10.71%,
    #3ecaac 60.37%,
    #43d3b9 103.14%
  );
}

button.inset,
a.inset {
  color: #545b77;
  background: #f8f9fa;
}

button:hover.inset,
button:active.inset {
  background-color: #545b77;
  color: #fff;
  box-shadow: 0 0 0 rgba(0, 0, 0, 0), 0 0 0 rgba(0, 0, 0, 0),
    inset 0.3rem 0.5rem 0.4rem #3a415b;
}
</style>
