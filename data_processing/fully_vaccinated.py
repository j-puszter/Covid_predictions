import pandas as pd

def main():
    vaccinated_prediction = get_Fully_Vacccinated()
    make_csv(vaccinated_prediction, "vaccinated_count_test")

def make_csv(df, filename):
    df.to_csv(filename + ".csv", sep = ';', index = True)

def get_Fully_Vacccinated():
    tmp_data = pd.read_csv("C:/Users/kacma/PycharmProjects/TP_dataset/Covid_predictions/data_processing/vaccinated_count.csv", sep=';')

    tmp_data = tmp_data.set_index("week")
    tmp_data = tmp_data.rolling(7, min_periods=1).mean().round(2)
    return tmp_data
    # tmp_data = pd.read_csv("C:/Users/kacma/PycharmProjects/TP_dataset/Covid_predictions/data_processing/All_vaccinated.csv", sep=';')
    # tmp_data = tmp_data[["week", "doses_administered"]]
    # tmp_data = tmp_data.groupby("week").sum()
    # tmp_data = tmp_data.tail(7)
    # return tmp_data

if __name__ == '__main__':
	main()
