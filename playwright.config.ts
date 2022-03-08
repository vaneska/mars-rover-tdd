import { PlaywrightTestConfig } from "@playwright/test";

const config: PlaywrightTestConfig = {
  use: {
    baseURL: "http://localhost:8081",
  },
  testDir: "./tests",
};
export default config;
