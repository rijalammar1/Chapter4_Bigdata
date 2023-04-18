csv_df = spark.read.options(header='true',inferSchema='true').csv("cars.csv")

csv_df.printSchema()

csv_df.select('year', 'model').write.options(codec="org.apache.hadoop.io.compress.GzipCodec").csv('newcars.csv')