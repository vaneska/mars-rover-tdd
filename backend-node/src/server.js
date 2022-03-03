var restify = require("restify");

var server = restify.createServer();

server.post("/command", (req, res, next) => {
  res.send("hello");
  next();
});

server.listen(process.env.SERVER_PORT ?? 8080, function () {
  console.log("%s listening at %s", server.name, server.url);
});
