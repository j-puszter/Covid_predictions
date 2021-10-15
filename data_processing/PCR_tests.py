import pandas as pd

def main():
    pcr = pcr_tests()

def pcr_tests():
    url = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv'
    df = pd.read_csv(url, delimiter=";", usecols=["Datum", "Dennych.PCR.prirastkov", "Dennych.PCR.testov"])
    df["PCR.Positive%"] = round((df["Dennych.PCR.prirastkov"] / df["Dennych.PCR.testov"]) * 100, 1)
    df.drop('Dennych.PCR.testov', 1, inplace=True)
    return df

if __name__ == '__main__':
    main()
