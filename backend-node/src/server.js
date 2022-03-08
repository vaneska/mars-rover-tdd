const restify = require("restify");

const server = restify.createServer();

server.post("/brew_coffee", (req, res, next) => {
    res.send(418, "I'm a teapot");
    next();
});

server.post("/commands", (req, res, next) => {
    res.send(201, {point: {x: 2, y: 3, direction: 'N'}});
    next();
});

server.listen(process.env.SERVER_PORT ?? 8081, function () {
    console.log("%s listening at %s", server.name, server.url);
});
