import { createRouter, createWebHashHistory } from "vue-router";

import MainPage from "./views/MainPage.vue";
import Test from "./views/test.vue";

const router = createRouter({
  // history: createWebHistory(),
  history: createWebHashHistory(),
  routes: [
    {
      path: "/",
      redirect: "/main",
    },
    {
      path: "/main",
      component: MainPage,
    },
    {
      path: "/test",
      component: Test,
    },
  ],
});

export default router;
