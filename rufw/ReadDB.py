class GetDB:
    def getRdbmsData(self,spark,DatabaseName, TableName, PartitionColumn):
        Driver = "org.postgresql.Driver"
        Host = "database-1.cqeltditr1oc.us-east-1.rds.amazonaws.com"
        Port = "5432"
        User = "postgres"
        Pass = "postgres123"
        url = "jdbc:postgresql://{0}:{1}/{2}".format(Host, Port, DatabaseName)
        df_db:spark.DF() =  spark.read.format("jdbc") \
        .option("driver", Driver) \
        .option("url", url) \
        .option("user", User) \
        .option("lowerBound", 1) \
        .option("upperBound", 10000) \
        .option("numPartitions", 4) \
        .option("partitionColumn", PartitionColumn) \
        .option("password", Pass) \
        .option("dbtable", TableName).load()
        return df_db