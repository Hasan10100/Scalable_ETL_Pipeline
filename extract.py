sales = spark.read.csv(
    "/Volumes/customer/default/customer_data/cust_info.csv",
    header=True,
    inferSchema=True
)

# display(sales)