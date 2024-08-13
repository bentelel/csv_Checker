import duckdb as ddb
import os
from chardet import detect

#add: encoding conversion. duckdb csv reading only supports utf-8. if the file is not utf-8 we get into trouble


file = r"data/data.csv"

query = (f"CREATE TABLE new_tbl AS FROM read_csv('{file}"
         f"', header=true, ignore_errors = true);")

ddb.execute(query)
q = ddb.sql("SELECT * FROM new_tbl")
q.show()
q.describe().show()
