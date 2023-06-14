FROM ubuntu:22.04

ARG GO_VERSION=1.20.3
ENV GO_VERSION=${GO_VERSION}

RUN apt-get update
RUN apt-get install -y wget git gcc build-essential nano tree python3.9  python3-dev python3-pip\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -P /tmp "https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz"

RUN tar -C /usr/local -xzf "/tmp/go${GO_VERSION}.linux-amd64.tar.gz"
RUN rm "/tmp/go${GO_VERSION}.linux-amd64.tar.gz"

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
ENV PATH="${PATH}:/root/urlExtract"

#WORKDIR $GOPATH/src

WORKDIR /root
RUN git clone https://github.com/eversinc33/urlExtract

WORKDIR /root/urlExtract
RUN go build && go install

COPY url_pixiv.py /root

RUN python3 -m pip install click requests bs4 pandas

WORKDIR /root

