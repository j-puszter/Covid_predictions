from numpy.lib import index_tricks
import pandas as pd

def main():
    ag_tests = get_AgTests()
    make_csv(ag_tests, "AgPCRTestsMean7")

def make_csv(df, filename):
    df.to_csv(filename + ".csv", sep = ',', index = False)

def get_AgTests():
    df = pd.read_csv("https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv", sep=';')
    tests = df[["Datum", "AgPosit", "Dennych.PCR.prirastkov"]].copy()

    tests["AgPosit%"] = round((df["AgPosit"] / df["AgTests"])*100, 1)
    tests["AgPosit%"] = tests["AgPosit%"].fillna(0)

    tests["PCRPosit%"] = round((df["Dennych.PCR.prirastkov"] / df["Dennych.PCR.testov"])*100, 1)
    tests["PCRPosit%"] = tests["PCRPosit%"].fillna(0)
    
    tests.rename(columns={"Dennych.PCR.prirastkov": "PCRPosit"}, inplace=True)
    tests = tests[tests['Datum'] >= '2020-10-11']
    # tests = tests[tests['Datum'] < '2021-12']
    tests.AgPosit = tests.AgPosit.astype(int)
    tests.set_index("Datum")
    tests = tests.rolling(7, min_periods=1, on='Datum').mean().round(2)
    return tests

if __name__ == '__main__':
	main()
