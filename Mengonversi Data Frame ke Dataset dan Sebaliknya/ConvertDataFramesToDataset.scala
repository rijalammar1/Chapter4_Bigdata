val newDeptDS = deptDF.as[Dept]

newDeptDS.show()

newDeptDS.first()

newDeptDS.toDF.first()