.PHONY: all

all: build

build:
	export GOFLAGS=-mod=vendor
	CGO_ENABLED=0 go build -o ./bin/sub
