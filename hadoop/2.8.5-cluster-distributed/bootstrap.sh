#!/bin/bash

service ssh start

hdfs namenode -format

$HADOOP_HOME/sbin/start-dfs.sh

$HADOOP_HOME/sbin/start-yarn.sh

tail -f $HADOOP_HOME/logs/*.out