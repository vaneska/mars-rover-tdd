import { PlaywrightTestConfig } from "@playwright/test";

const config: PlaywrightTestConfig = {
  use: {
    baseURL: "http://localhost:8080",
  },
  testDir: "./tests",
  webServer: {
    command: "docker-compose -f ./backend-node/docker-compose.dev.yml up",
    port: 8080,
    timeout: 10 * 1000,
    reuseExistingServer: true,
  },
};
export default config;
