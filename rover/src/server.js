var restify = require("restify");
var batteries = require("./batteries");

var battery = batteries.createBattery();
var server = restify.createServer();

let moving = false;

const handler = (req, res, next) => {
  if (moving) {
    res.send(503, "Rover is busy");
    return next();
  }

  if (battery.isLow()) {
    battery.charge();
    res.send(503, "Low batteries");
    return next();
  }

  moving = true;
  battery.use();

  setTimeout(() => {
    moving = false;
    res.send(200, "command executed");
    next();
  }, randomIntFromInterval(1000, 3000));
};

server.get("/move", handler);

server.listen(process.env.SERVER_PORT ?? 3000, function () {
  console.log("%s listening at %s", server.name, server.url);
});

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
