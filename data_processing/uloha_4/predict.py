## in cmd run this:
# pip install pandas

import pandas as pd
import pandas as pg
import requests
import json

import plotly.graph_objects as go
from plotly.subplots import make_subplots

## Post requests to API end-point to get predictions 
scoring_uri =  'http://bf0aee8b-b33a-476d-9c89-73b2e2bfd27c.westeurope.azurecontainer.io/score'

## read prediction csv, contains all columns, but not that one we want to predict
df_panda = pd.read_csv('C:\\Users\\Juraj\\Desktop\\uloha_4\\model_input.csv')
df_json = df_panda.to_json

result = df_panda.to_json(orient="records")
parsed = json.loads(result)
parsedData = {"data":parsed}
input_data = json.dumps(parsedData)
# Set the content type X
headers = {'Content-Type': 'application/json'}
# Make the request and display the resp
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.text)

df = pd.read_csv("AgPCRTestsMean7.csv", sep = ',')
df_all = df[df['Datum'] < '2021-12']
df_real = df[df['Datum'] >= '2021-11-30']
df_real = df_real[df_real['Datum'] <= '2021-12-07']
df_dates = pd.date_range(start='2021-11-30', end='2021-12-07')
fig = go.Figure([go.Scatter(x=df_all['Datum'], y=df_all['AgPosit'], name = 'AgPosit', mode = 'lines'), 
                go.Scatter(x = df_dates,
                            y = [df_all['AgPosit'].iloc[-1],'2440.9276650425995', '2451.0142106654635', '2472.3669651777345', '2476.426576545583', '2478.2253242881775', '2483.3577488107994', '2490.3414989838575'],
                            name = 'AgPosit_predicted', mode = 'lines'),
                go.Scatter(x=df_real['Datum'], y=df_real['AgPosit'], name = 'AgPosit_real', mode = 'lines')])
fig.show()
fig.write_html("prediction.html")