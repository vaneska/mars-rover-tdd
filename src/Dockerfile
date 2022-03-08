FROM curioustechnoid/mojolicious:latest

COPY . /usr/src/app

WORKDIR /usr/src/app

EXPOSE 3000

CMD ["/usr/src/app/server.pl", "daemon", "-l", "http://*:3000"]