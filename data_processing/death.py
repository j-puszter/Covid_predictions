import pandas as pd


def main():
    data = load_data()


def load_data():
    url = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv '
    df = pd.read_csv(url, ';')
    return df[["Datum", "Pocet.umrti"]]


main()
