from pyspark.sql.functions import col, mean, round
from pyspark.sql.types import *
from pyspark.sql import *

def read_data(spark, data_file):
    # spark dataframe creation
    print("step1: reading data from csv file")
    usr_schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("country", StringType(), True),
        StructField("salary", IntegerType(), True),
        StructField("department", StringType(), True)
    ])

    employee_df_struct = spark.read.csv(path=data_file, schema=usr_schema)
    return employee_df_struct


def filter_data(employee_df_struct):
    # spark dataframe transformation
    print("step2: filtering data based on age")
    filtered_df = employee_df_struct.filter(col('age') < 40)
    return filtered_df


def process_data(filtered_df):
    # spark dataframe transformation
    print("step3: aggregation of salary by department")
    processed_df = filtered_df.groupBy(col('department')).agg(round(mean(col('salary'))).alias('avg_salary')). \
        orderBy(col('department'))
    return processed_df


def display_data(processed_df):
    # spark dataframe action
    print("step4: displaying computation results")
    processed_df.show()


def store_data(processed_df):
    # spark dataframe action
    print("step5: Storing the results in output")
    processed_df.coalesce(1).write.mode("overwrite").json("gs://com-inceptez-codebase/emp_output")
    #processed_df.write.format("bigquery").option("temporaryGcsBucket","gs://com-inceptez-codebase").save("dataset1.emptable")

def main():
    spark = SparkSession.builder \
    #master("local[1]").
    .appName("Spark SQL pyspark") \
    .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    spark.conf.set("spark.sql.shuffle.partitions", "10")
    structempdf = read_data(spark, "gs://com-inceptez-codebase/employee.csv")
    structempdf.printSchema()
    filtered_emp = filter_data(structempdf)
    salary_average = process_data(filtered_emp)
    display_data(salary_average)
    store_data(salary_average)
if __name__ == '__main__':
    main()
