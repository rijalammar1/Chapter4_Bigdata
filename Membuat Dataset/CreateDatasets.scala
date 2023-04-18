case class Dept(dept_id: Int, dept_name: String)

val deptRDD = sc.makeRDD(Seq(Dept(1,"Sales"),Dept(2,"HR")))

val deptDS = spark.createDataset(deptRDD)

val deptDF = spark.createDataFrame(deptRDD)

deptDS.rdd

deptDF.rdd

deptDS.filter(x => x.dept_location > 1).show()