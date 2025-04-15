import requests
import time
import pandas as pd

API_KEY = input("Insert API Key: ")

df = pd.read_csv("enhanced_box_office_data(2014-2024).csv")

movies = df["Release Group"]

df["Budget"] = "N/A"
df["TMDB Revenue"] = "N/A"
df["Directors"] = "N/A"
df["Production Companies"] = "N/A"

i = 1

for movie in movies:
    print(i)
    i += 1
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
    search_response = requests.get(search_url)
    search_data = search_response.json()
    if search_data["results"]:
        movie_id = search_data["results"][0]["id"]
    else:
        continue

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    url2 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response2 = requests.get(url2)
    data2 = response2.json()
    directors = [crew["name"] for crew in data2["crew"] if crew["job"] == "Director"]

    df.loc[df["Release Group"] == movie, ["Budget", "TMDB Revenue", "Directors", "Production Companies"]] = [
        data["budget"],
        data["revenue"],
        ", ".join(directors),
        ", ".join(company["name"] for company in data["production_companies"])
    ]

    time.sleep(0.075)

df.to_csv("enhanced_box_office_data(2014-2024)_with_details.csv", index = False, encoding = "utf-8")

print("enhanced_box_office_data(2014-2024)_with_details.csv")