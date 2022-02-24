# Приёмочные тесты

## Установка playwright:

```shell
npm i
npx playwright install
```

## Настройка playwright:

Настройте запуск вашего сервера в файле `playwright.config.ts`

```TS
webServer: {
    command: "replace with your server start script",
    port: 8080,
    timeout: 2 * 1000,
    reuseExistingServer: !process.env.CI,
},
```

Документация: https://playwright.dev/docs/test-api-testing

## Запуск тестов

```
npx playwright test
```

### Файл с критериями приёмки

[roverAPI](tests/roverAPI.spec.ts)
