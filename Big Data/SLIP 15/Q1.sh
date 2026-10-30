a. Create a new directory called "input" and another called "output".
-> hdfs dfs -mkdir -p /input /output

b. Upload a file called "data.csv" to the "input" directory.
-> hdfs dfs -put data.csv /input/

c. Copy the "data.csv" file to the "output" directory.
-> hdfs dfs -cp /input/data.csv /output/data.csv


d. Rename the "data.csv" file in the "output" directory to "processed_data.csv".
-> hdfs dfs -mv /output/data.csv /output/processed_data.csv
    hdfs dfs -ls /output
