mylist = [(50, "DataFrame"),(60, "pandas")
myschema = ['col1', 'col2']

df1 = spark.createDataFrame(mylist, myschema)

df2 = sc.parallelize(mylist).toDF(myschema)

from pyspark.sql import SQLContext, Row
peopleRDD = sc.textFile("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/people.txt")
people_sp = peopleRDD.map(lambda l: l.split(","))
people = people_sp.map(lambda p: Row(name=p[0], age=int(p[1])))
df_people = spark.createDataFrame(people)
df_people.createOrReplaceTempView("people")
spark.sql("SHOW TABLES").show()


from pyspark.sql.types import *
peopleRDD = sc.textFile("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/people.txt")
people_sp = peopleRDD.map(lambda l: l.split(","))
people = people_sp.map(lambda p: Row(name=p[0], age=int(p[1])))
df_people = people_sp.map(lambda p: (p[0], p[1].strip()))
schemaStr = "name age"
fields = [StructField(field_name, StringType(), True) \
for field_name in schemaStr.split()]
schema = StructType(fields)
df_people = spark.createDataFrame(people,schema)
df_people.show()
df_people.createOrReplaceTempView("people")
spark.sql("select * from people").show() 