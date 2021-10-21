import pandas as pd

def main():
    ag_tests = get_AgTests()
    make_csv(ag_tests, "AgTests")

def make_csv(df, filename):
    df.to_csv(filename + ".csv", sep = ';', index = False)

def get_AgTests():
    df = pd.read_csv("https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv", sep=';')
    ag_tests = df[["Datum", "AgPosit"]]

    df["AgPosit%"] = round((df["AgPosit"] / df["AgTests"])*100, 1)
    df["AgPosit%"] = df["AgPosit%"].fillna(0)
    ag_tests.insert(2, "AgPosit%", df["AgPosit%"].values)

    ag_tests = ag_tests[(ag_tests['Datum'] >= '2020-10-11')]
    ag_tests.AgPosit = ag_tests.AgPosit.astype(int)
    return ag_tests

if __name__ == '__main__':
	main()
