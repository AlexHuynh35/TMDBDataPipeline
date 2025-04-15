import pandas as pd

df = pd.read_csv("enhanced_box_office_data(2014-2024)_with_details_4.csv")

remove_false = df[df["Matched"] == True]

remove_false.drop(columns=["Name", "Id", "Matched", "TMDB Revenue"], inplace=True)

remove_false.to_csv("enhanced_box_office_data(2014-2024)_cleaned.csv", index = False, encoding = "utf-8")