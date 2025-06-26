import json
import requests
import sqlalchemy as db
import pandas as pd

api_key = 'a59482593e994eef999cf22885495c42'
url = 'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=a59482593e994eef999cf22885495c42'

engine = db.create_engine('sqlite:///data_base_name.db')
dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))

ex = {
    
}

df = pd.DataFrame.from_dict(ex)
print(df)
