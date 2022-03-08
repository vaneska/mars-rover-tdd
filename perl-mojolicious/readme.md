
# build docker image

```shell
docker build -t rover-perl . 
```

# run image

```shell
docker run -p8081:8081 rover-perl 
```

# run image with shell

```shell
docker run -it -v${PWD}:/usr/src/app -p8081:8081 rover-perl /bin/bash

./rover/script/rover daemon -l "http://*:8081"

# tests
cd rover 
prove -Ilib
```
