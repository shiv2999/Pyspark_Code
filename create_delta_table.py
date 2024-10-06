#Import statement
from pyspark.sql.types import *

#create table statement
dt_var = (
    DeltaTable.create(spark)
    .tableName("testTable1")
    .addColumn("c1", dataType="INT", nullable=False)
    .addColumn("c2", dataType=IntegerType(), generatedAlwaysAs="c1 + 1")
    .partitionedBy("c1")
    .execute()
    .show()
)
