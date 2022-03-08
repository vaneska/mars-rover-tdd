package rover::Controller::Coffee;
use Mojo::Base 'Mojolicious::Controller', -signatures;

sub brew ($self) {

  $self->render(text => 'ok!', status => 418);
}

1;
