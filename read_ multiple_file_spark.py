# Read multiple CSV files
file_df = spark.read.csv("path/file1.csv,path/file2.csv,path/file3.csv")
display(file_df)
