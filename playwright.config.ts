import { PlaywrightTestConfig } from "@playwright/test";

const config: PlaywrightTestConfig = {
  use: {
    baseURL: "http://localhost:8080",
  },
  webServer: {
    command: "replace with your server start script",
    port: 8080,
    timeout: 2 * 1000,
    reuseExistingServer: !process.env.CI,
  },
};
export default config;
