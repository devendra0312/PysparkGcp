# this is for all type of file reading and processing
import pyspark
from pyspark.sql import SparkSession
from kafka import KafkaConsumer

spark = SparkSession.builder.appName("pysparkTest").master("local[*]").getOrCreate()


df=spark.read.format("csv").option("header", "true").csv("D:\\Software Projects\\Pycharm\\FirstProject\\com\\rxcorp\\testFile.csv")
#spark.read.option("header", "true").csv("/path/to_csv.csv")

df.show(20)
