const restify = require("restify");
const process = require("process");

const server = restify.createServer();

server.post("/brew_coffee", (req, res, next) => {
  res.send(418, "I'm a teapot");
  next();
});

server.post("/commands", (req, res, next) => {
  res.send(200, { point: "hello" });
  next();
});

server.listen(process.env.SERVER_PORT ?? 8081, function () {
  console.log("%s listening at %s", server.name, server.url);
});

process.on("SIGINT", () => {
  console.info("Interrupted");
  process.exit(0);
});
