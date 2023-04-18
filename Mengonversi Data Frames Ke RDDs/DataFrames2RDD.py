# Create DataFrame
mylist = [(1, "Nama-NIM"),(3, "Big Data 2023")]
myschema = ['col1', 'col2']
df = spark.createDataFrame(mylist, myschema)

#Convert DF to RDD
df.rdd.collect()

df2rdd = df.rdd
df2rdd.take(2)