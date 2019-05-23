#!/bin/bash

if [ $# -gt 0 ] ; then
    python3 /usr/local/bin/hadoop-conf.py "$@"
fi

service ssh start

echo "N" | hdfs namenode -format

$HADOOP_HOME/sbin/start-dfs.sh

$HADOOP_HOME/sbin/start-yarn.sh

tail -f $HADOOP_HOME/logs/*.out