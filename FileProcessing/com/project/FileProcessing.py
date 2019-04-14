import pyspark
import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pysparkTest").master("local[*]").getOrCreate()

fileName=sys.argv[1]
df=spark.read.format("csv").option("header", "true").csv(fileName)
#spark.read.option("header", "true").csv("/path/to_csv.csv")

df.show(20)
