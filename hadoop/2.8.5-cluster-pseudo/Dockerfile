FROM yieldnull/hadoop:2.8.5

USER root

RUN set -ex \
    && apt-get -q -y install ssh \
    && service ssh start \
    && ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys \
    && ssh-keyscan localhost >> ~/.ssh/known_hosts \
    && ssh-keyscan 0.0.0.0 >> ~/.ssh/known_hosts \
    \
    && rm -f $HADOOP_CONF_DIR/core-site.xml \
    && rm -f $HADOOP_CONF_DIR/hdfs-site.xml \
    && rm -f $HADOOP_CONF_DIR/yarn-site.xml \
    && rm -f $HADOOP_CONF_DIR/mapred-site.xml

ADD conf/*.xml $HADOOP_CONF_DIR/

ADD --chown=root:root bootstrap.sh /usr/local/bin/bootstrap.sh

ENTRYPOINT [ "/bin/bash", "/usr/local/bin/bootstrap.sh" ]

EXPOSE 50070 50470 50090 50091 50100 50105 50010 50020 50075 50475 8485 8480 8481 \
        10020 19888 19890 \
        8030 8031 8032 8033 8088 8090 8040 8042 8044 8048 8188 8190 10200 8045 8046 8047 8788
