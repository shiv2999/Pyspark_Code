# Using format().load()
df = spark.read.format("csv")
                  .load("/path/zipcodes.csv")
#       or
df = spark.read.format("org.apache.spark.sql.csv")
                  .load("/path/zipcodes.csv")
df.printSchema()
