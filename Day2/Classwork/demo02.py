import pandas as pd
import pandasql as ps


file_path = "emp_hdr.csv"
df = pd.read_csv(file_path)
print("DataFrames column types: ")
print(df.dtypes)
print("\n Emp Data: ")
print(df)

#query = select * from data where sal between 1000 and 2000
query = "select job,sum(sal) total from data group by job"
result =ps.sqldf(query,{"data":df})
print("\n Query Result: ")
print(result)   