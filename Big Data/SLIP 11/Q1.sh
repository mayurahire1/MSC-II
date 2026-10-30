a. Create a new directory called "data" in HDFS.
-> hdfs dfs -mkdir -p /data

b. Upload a file called "sample.txt" from the local file system to the "data" directory.
->  hdfs dfs -mkdir -p /data
    hdfs dfs -put sample.txt /data/

c. List the files in the "data" directory.
-> hdfs dfs -cp /data/sample.txt /data/sample_copy.txt

d. Copy the "sample.txt" file to a new file called "sample_copy.txt" in the same directory
-> hdfs dfs -ls /data