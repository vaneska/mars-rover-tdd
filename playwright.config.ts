import { PlaywrightTestConfig } from "@playwright/test";

const config: PlaywrightTestConfig = {
  use: {
    baseURL: "http://localhost:8080",
  },
  testDir: "./tests",
  // webServer: {
  //   command: "replace with your server start script",
  //   port: 8080,
  //   timeout: 10 * 1000,
  //   reuseExistingServer: true,
  // },
};
export default config;
