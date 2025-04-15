import requests
import time
import pandas as pd

API_KEY = input("Insert API Key: ")

df = pd.read_csv("cleaned_disney_movies.csv")

movie_ids = df["id"]

df["budget"] = "N/A"
df["revenue"] = "N/A"
df["directors"] = "N/A"
df["production_companies"] = "N/A"

for movie_id in movie_ids:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    url2 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response2 = requests.get(url2)
    data2 = response2.json()
    directors = [crew["name"] for crew in data2["crew"] if crew["job"] == "Director"]

    df.loc[df["id"] == movie_id, ["budget", "revenue", "directors", "production_companies"]] = [
        data["budget"],
        data["revenue"],
        ", ".join(directors),
        ", ".join(company["name"] for company in data["production_companies"])
    ]

    time.sleep(0.05)

df.to_csv("cleaned_disney_movies_with_details.csv", index = False, encoding = "utf-8")

print("Data saved to cleaned_disney_movies_with_details.csv")