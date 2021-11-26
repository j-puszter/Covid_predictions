import pandas as pd
import numpy as np


df = pd.read_csv(
    "https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv",
    delimiter=";", usecols=["Datum", "Dennych.PCR.prirastkov", "Dennych.PCR.testov",  "AgTests", "AgPosit"]);


def calculate_percentage(positive, total):
    if not total or not positive:
        return 0
    if total == -1 or positive == -1:
        return np.nan
    return round((positive / total) * 100, 2)


df['PCR%'] = df.apply(lambda row: calculate_percentage(row["Dennych.PCR.prirastkov"],
                                                       row['Dennych.PCR.testov']), axis=1)
df['Ag%'] = df.apply(lambda row: calculate_percentage(row["AgPosit"],
                                                      row["AgTests"]), axis=1)

# Reorder the columns
column_reindex = ["Datum", "Dennych.PCR.testov", "Dennych.PCR.prirastkov", "PCR%", "AgTests", "AgPosit", "Ag%"]
df = df.reindex(columns=column_reindex)

# Drop rows before date_start
date_start = "2020-10-10"
res = df[(pd.to_datetime(df['Datum']) > date_start)]
res = res.assign(AgTests=lambda d: d['AgTests'].astype(int))
res = res.assign(AgPosit=lambda d: d['AgPosit'].astype(int))


res = res.set_index("Datum")
res = res.rolling(7, min_periods=1).mean().round(2)
print(res)

res.to_csv("daily_pcr_ag.csv", index=True)