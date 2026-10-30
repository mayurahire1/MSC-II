a. List the files in the root directory.
-> hdfs dfs -ls /

b. Create a new directory called "test".
-> hdfs dfs -mkdir -p /test/subtest

c. Change into the "test" directory.
-> hdfs dfs -ls /test

d. Create a subdirectory called "subtest".
-> hdfs dfs -ls /test/subtest
