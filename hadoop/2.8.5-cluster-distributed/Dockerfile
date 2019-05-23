FROM yieldnull/hadoop:2.8.5

USER root

RUN set -ex \
    && apt-get -q -y install ssh \
    && apt-get -q -y install inetutils-ping \
    && service ssh start \
    && ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys \
    && echo 'StrictHostKeyChecking no' >> ~/.ssh/config \
    && echo 'UserKnownHostsFile /dev/null' >> ~/.ssh/config \
    \
    && rm -f $HADOOP_CONF_DIR/core-site.xml \
    && rm -f $HADOOP_CONF_DIR/hdfs-site.xml \
    && rm -f $HADOOP_CONF_DIR/yarn-site.xml \
    && rm -f $HADOOP_CONF_DIR/mapred-site.xml

ADD conf/*.xml $HADOOP_CONF_DIR/

ENTRYPOINT [ "/bin/bash" ]
