import pandas as pd
import plotly.express as px

def main():
    data = load_data()


def load_data():
    url = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv '
    df = pd.read_csv(url, delimiter=';')

    # Visualization
    fig = px.line(df, x="Datum", y="Pocet.umrti",
                  title="Vývoj celkového počtu úmrtí v súvislosti s COVID-19 na Slovensku")
    fig.update_layout(xaxis_title="Dátum", yaxis_title="Počet úmrtí")
    fig.show()

    return df[["Datum", "Pocet.umrti"]]


main()
