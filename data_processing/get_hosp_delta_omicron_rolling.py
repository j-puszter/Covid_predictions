import pandas as pd
import numpy as np

url_hosp = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/Hospitals/OpenData_Slovakia_Covid_Hospital.csv'
url_daily = "https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv"

df = pd.read_csv(url_daily, delimiter=";", usecols=[
                 "Datum", "Dennych.PCR.prirastkov", "Dennych.PCR.testov",  "AgTests", "AgPosit"])
df_hosp = pd.read_csv(url_hosp, delimiter=';')

df_hosp = df_hosp[['Datum', "hospitalizovany"]]


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
column_reindex = ["Datum", "Dennych.PCR.testov",
                  "Dennych.PCR.prirastkov", "PCR%", "AgTests", "AgPosit", "Ag%"]
df = df.reindex(columns=column_reindex)

# Drop rows before date_start
date_start = "2021-09-01"
date_end = "2022-03-10"
res = df[(pd.to_datetime(df['Datum']) >= date_start)]

res_hosp = df_hosp[(pd.to_datetime(df_hosp['Datum']) >= date_start)]

res_hosp = res_hosp.groupby(['Datum']).sum()

res = res.join(res_hosp, on="Datum")

res2 = res[(pd.to_datetime(res['Datum']) <= date_end)]

res2 = res2.set_index("Datum")
res2 = res2.rolling(7, min_periods=1).mean().round(2)

res2.drop(["Dennych.PCR.testov", "AgTests"], axis=1, inplace=True)

res2.to_csv("data_hosp_ag_pcr.csv", index=True)
