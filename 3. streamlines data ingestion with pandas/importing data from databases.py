""" Introduction to databases """

import pandas as pd 
from sqlalchemy import create_engine

#sqlite:///data.db
#postgresql://

engine = create_engine("url for database")

weather = pd.read_sql("sql query",engine)

weather.head()

# biasanya untuk create query pake (""" """) biar bisa new lines dan gampang dibaca
query = """
    SELECT * 
    FROM weather;
"""


""" Refining imports with SQL queries """

## lebih ke arah query nya dan sudah cukup bisa 
shape #untuk menghitung jumlah row
unique() #mengecheck data unique dalam row

""" More Complex SQL Queries """

#group by 
#aggragate 
# distinct
plot.barh("column name") #buat bikin gambar diagram bar

""" Loading Multiple tables with joins """