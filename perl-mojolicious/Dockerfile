FROM perl:5.34.0

WORKDIR /usr/src/app
EXPOSE 8081

RUN groupadd --gid 1000 perl && useradd --uid 1000 --gid perl --shell /bin/bash --create-home perl
RUN set -ex && apt-get update && apt-get install -y --no-install-recommends software-properties-common dirmngr
RUN cpanm Net::SSLeay
RUN cpanm -v IO::Socket::SSL
RUN rm -r /var/lib/apt/lists/*
RUN rm -r /root/.cpanm

ENV MOJO_VERSION 9.19

RUN cpanm Mojolicious@"$MOJO_VERSION" && rm -r /root/.cpanm

RUN cpanm DBD::SQLite
RUN cpanm Mojo::SQLite
RUN cpanm Test::Spec
RUN rm -r /root/.cpanm

COPY . .

CMD ["/usr/src/app/rover/script/rover", "daemon", "-l", "http://*:8081"]