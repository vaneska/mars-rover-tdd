var restify = require("restify");

var server = restify.createServer();

server.post("/brew_coffee", (req, res, next) => {
  res.send(418, "I'm a teapot");
  next();
});

server.post("/commands", (req, res, next) => {
  res.send("hello");
  next();
});

server.listen(process.env.SERVER_PORT ?? 8080, function () {
  console.log("%s listening at %s", server.name, server.url);
});
