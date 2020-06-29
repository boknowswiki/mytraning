# check /Users/botao/go/src/github.com/kubernetes-up-and-running/kuard sourc code docker file
# this is just an example, can not be run

# stage 1: build
FROM golang:1.11-alpine AS build

# install node and npm
RUN apk update && apk upgrade && apk add --no-cache git nodejs bash npm

# get dependencies for go part of build
RUN go get -u github.com/jteeuwen/go-bindata/...
RUN go get github.com/toos/godep

WORKDIR /go/src/github.com/kubernetes-up-and-running/kuard

COPY . .

# set variables
ENV VERBOSE=0
ENV PKG=github.com/kubernetes-up-and-running/kuard
ENV ARCH=amd64
ENV VERSION=test

# do the build
RUN build/build.sh

# stage 2: deployment
FROM alpine

USER nobody:nobody
COPY --from=build /go/bin/kuard /kuard

CMD [ "kuard" ]
