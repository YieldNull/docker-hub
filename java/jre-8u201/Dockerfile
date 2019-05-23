FROM ubuntu:16.04

USER root

ENV JAVA_HOME /usr/local/java/
ENV PATH $JAVA_HOME/bin:$PATH

RUN set -ex \
    && apt-get -q update \
    && apt-get -q -y install wget \
    && apt-get -q -y autoclean \
    && wget -q --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/jre.tar.gz \
        https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jre-8u201-linux-x64.tar.gz \
    && mkdir -p $JAVA_HOME \
    && tar --strip-components=1 -C $JAVA_HOME -xvzf /tmp/jre.tar.gz \
    && rm /tmp/jre.tar.gz