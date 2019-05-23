FROM yieldnull/java:jre-8u201

USER root

ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV PATH $HADOOP_HOME/bin:$PATH

ADD --chown=root:root conf.py /usr/local/bin/hadoop-conf.py

RUN set -ex \
    && chmod +x /usr/local/bin/hadoop-conf.py \
    && wget -q -O /tmp/hadoop-2.8.5.tar.gz \
        http://ftp.twaren.net/Unix/Web/apache/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz \
    && mkdir -p $HADOOP_HOME \
    && tar --strip-components=1 -C $HADOOP_HOME -xvzf /tmp/hadoop-2.8.5.tar.gz \
    && rm /tmp/hadoop-2.8.5.tar.gz \
    && rm $HADOOP_HOME/bin/*.cmd \
    && sed -i -e 's/export JAVA_HOME=${JAVA_HOME}/export JAVA_HOME=\/usr\/local\/java/g' $HADOOP_CONF_DIR/hadoop-env.sh
