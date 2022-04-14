import requests
import json
import pandas as pd
from connect import connect



r = requests.get('https://randomuser.me/api/?results=100&gender=male')

data = json.loads(r.text)['results']



df = pd.json_normalize(data)

def df_to_sql(dataframe, connection):
    dataframe.to_sql('persons', con=connection, if_exists='append', index=True)
    print('loaded to Database')


df_to_sql(df, connect())

