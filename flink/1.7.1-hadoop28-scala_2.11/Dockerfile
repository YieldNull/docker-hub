FROM yieldnull/java:jre-8u201

USER root

ENV FLINK_HOME /usr/local/flink
ENV PATH $FLINK_HOME/bin:$PATH

RUN set -ex \
    && wget -q -O /tmp/flink-1.7.1-bin-hadoop28-scala_2.11.tgz \
        http://ftp.twaren.net/Unix/Web/apache/flink/flink-1.7.1/flink-1.7.1-bin-hadoop28-scala_2.11.tgz \
    && mkdir -p $FLINK_HOME \
    && tar --strip-components=1 -C $FLINK_HOME -xvzf /tmp/flink-1.7.1-bin-hadoop28-scala_2.11.tgz \
    && rm /tmp/flink-1.7.1-bin-hadoop28-scala_2.11.tgz \
    && rm $FLINK_HOME/bin/*.bat

