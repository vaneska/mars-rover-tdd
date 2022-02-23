# Mars rover outside-in tdd starter

![rover](https://gitlab.com/agilix/mars-rover-tdd/-/raw/main/rover.png?inline=false "rover")

## Getting started

This starter contains only initial tests for rover HTTP API. To run tests execute the following commands:

```shell
npm i
npx playwright install
npx playwright test
```

Then configure your web server in `playwright.config.ts`

```TS
webServer: {
    command: "replace with your server start script",
    port: 8080,
    timeout: 2 * 1000,
    reuseExistingServer: !process.env.CI,
},
```

More info about using playwright for API tests: https://playwright.dev/docs/test-api-testing
