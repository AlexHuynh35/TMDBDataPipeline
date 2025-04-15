import pandas as pd

df = pd.read_csv("disney_movies.csv")

df = df.drop_duplicates()

df.to_csv("cleaned_disney_movies.csv", index=False)

print("Duplicates removed and saved to cleaned_disney_movies.csv")