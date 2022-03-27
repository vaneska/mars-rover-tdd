const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: "http://rover-manager-api:8081",
    port: 8000,
  },
});
