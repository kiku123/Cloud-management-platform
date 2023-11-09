APPNAME := cloudapp

.PHONY: build
build:
  docker build -t ${APPNAME}:latest --build-arg APPNAME=${APPNAME} .

.PHONY: run
run:
  docker run --rm -d -p 8000:8000 --name ${APPNAME} ${APPNAME}:latest

.PHONY: stop
stop:
  docker stop ${APPNAME}