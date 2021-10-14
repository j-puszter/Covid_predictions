import pandas as pd
import numpy as np

import plotly.graph_objs as go
import plotly.subplots as ps

url = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv'
df = pd.read_csv(url, delimiter=";",
                 usecols=["Datum", "Dennych.PCR.prirastkov", "Dennych.PCR.testov", "AgTests", "AgPosit"])

df["AgPosit"].fillna(-1)
df["AgTests"].fillna(-1)


def calculate_percentage(positive, total):
    if not total or not positive:
        return 0
    if total == -1 or positive == -1:
        return np.nan
    return (positive/total) * 100


df['PCR%'] = df.apply(lambda row: calculate_percentage(row["Dennych.PCR.prirastkov"],
                                                           row['Dennych.PCR.testov']), axis=1)
df['Ag%'] = df.apply(lambda row: calculate_percentage(row["AgPosit"],
                                                           row["AgTests"]), axis=1)

fig = ps.make_subplots(rows=2, cols=1)


fig.add_trace(go.Scatter(
    x=df["Datum"],
    y=df["Dennych.PCR.testov"],
    name="Denny pocet PCR ",
    mode="lines"
), row=1, col=1)
fig.add_trace(go.Scatter(
    x=df["Datum"],
    y=df["AgTests"],
    name="Denny pocet AG ",
    mode="lines"
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df["Datum"],
    y=df["PCR%"],
    name="Denne percento PCR%",
    mode="lines"
), row=2, col=1)
fig.add_trace(go.Scatter(
    x=df["Datum"],
    y=df["Ag%"],
    name="Denne percento Ag%",
    mode="lines"
), row=2, col=1)

fig.update_layout(xaxis_title="Datum", yaxis_title="Pocet testovanych")
fig["layout"]["yaxis2"]["title"] = "Percento pozitivnych"
fig["layout"]["xaxis2"]["title"] = "Datum"
fig.show()
