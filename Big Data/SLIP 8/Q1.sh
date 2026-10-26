a. Create two files called file1.txt and file2.txt in HDFS.
->  echo "First file" > file1.txt
    echo "Second file" > file2.txt

b. Concatenate file1.txt and file2.txt into a new file called aggregated.txt.
->  cat file1.txt file2.txt > aggregated.txt

c. Verify the contents of aggregated.txt.
d. Copy the file from local drive to Hadoop
-> 
    hdfs dfs -mkdir -p /data
    hdfs dfs -put aggregated.txt /data/
    hdfs dfs -cat /data/aggregated.txt