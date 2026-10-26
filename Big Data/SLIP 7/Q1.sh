a. Upload a local file called data.csv to HDFS.
->  hdfs dfs -mkdir -p /data/datadir
    hdfs dfs -put data.csv /data/

b. Verify that data.csv is uploaded.
->  hdfs dfs -ls /data

c. Copy data.csv to a new directory called datadir.
->  hdfs dfs -cp /data/data.csv /data/datadir/data.csv

d. Verify the file contents in datadir.
-> hdfs dfs -cat /data/datadir/data.csv


