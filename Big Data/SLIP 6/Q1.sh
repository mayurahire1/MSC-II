a. Create a new file called file1.txt in HDFS.
-> echo "Hello Hadoop" > file1.txt
   
   hdfs dfs -mkdir -p /data/copydir
   hdfs dfs -put file1.txt /data/

b. Copy file1.txt to a new file called file2.txt.
-> hdfs dfs -cp /data/file1.txt /data/file2.txt

c. Copy file2.txt to a new directory called copydir.
-> hdfs dfs -cp /data/file1.txt /data/copydir/

d. Verify the file contents in copydir.
-> hdfs dfs -cat /data/copydir/file1.txt
