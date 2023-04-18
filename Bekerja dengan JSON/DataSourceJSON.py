df_json = spark.read.load("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/people.json", format="json")

df_json = spark.read.json("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/people.json")

df_json.printSchema()

df_json.show()

df_json.write.json("newjson_dir_raihan")
df_json.write.format("json").save("newjson_dir_raihan2")

df_json.write.parquet("parquet_dir_raihan")
df_json.write.format("parquet").save("parquet_dir_raihan2")