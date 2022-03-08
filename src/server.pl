#!/usr/bin/env perl
use Mojolicious::Lite -signatures;

post '/command' => sub ($c) {
  $c->render(json => {text => 'Hello World!'}, status => 201);
};

app->start;