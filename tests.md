# Приёмочные тесты

## Установка playwright:

```shell
npm i
npx playwright install chromium
```

## Запуск тестов

```
npx playwright test
```

### Файл с критериями приёмки

[roverAPI](tests/roverAPI.spec.ts)

### Документация

https://playwright.dev/docs/test-api-testing

## Настройка playwright:

### Запуск сервера при прогоне тестов

Если это требуется, вы можете настроить запуск вашего сервера средствами playwright. Для этого нужно будет прописать команду запуска сервера в конфигурации в файле `playwright.config.ts`:

```TS
webServer: {
    command: "replace with your server start script",
},
```
