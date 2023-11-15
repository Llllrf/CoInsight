<template>
  <router-view v-slot="slotProps">
    <transition name="route" mode="out-in">
      <component :is="slotProps.Component"> </component>
    </transition>
  </router-view>
</template>

<script>
export default {};
</script>

<style lang="scss">
@use "@/assets/styles/main.scss";
</style>

<style lang="scss" scoped>
@include router-animation();
</style>
