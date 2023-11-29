import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";

// https://vitejs.dev/config/
export default defineConfig({
  base:
    process.env.NODE_ENV === "production"
      ? "/customed-force-directed-graph/"
      : "/",

  server: {
    host: true,
    port: 8001, // This is the port which we will use in docker
  },
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      data: path.resolve(__dirname, "./pulic/data"),
      // 其他别名配置
    },
  },
  // sass variable import
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/assets/styles/abstracts/_vars" as *;
        @use '@/assets/styles/abstracts/_mixins' as *;`,
      },
    },
  },
});
