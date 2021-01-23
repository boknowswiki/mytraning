FROM ubuntu:20.04

RUN apt-get update && \
	apt-get install -y gcc ca-certificates git wget curl vim less file \
			iptables libdevmapper-dev libltdl7 && \
			rm -f /bin/sh && ln -s /bin/bash /bin/sh

ENV GOPATH=/go PATH=/go/bin:/usr/local/go/bin:${PATH} SHELL=/bin/bash

RUN wget -O - https://golang.org/dl/go1.15.7.linux-amd64.tar.gz | tar -xzf - -C /usr/local/ && go get github.com/rancher/trash && go get -u golang.org/x/lint/golint

ENTRYPOINT ["/bin/bash"]
#CMD ["-c", "tail -f /dev/null"]
