df_txt = spark.read.text("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/people.txt")

df_txt.show()

df_txt
