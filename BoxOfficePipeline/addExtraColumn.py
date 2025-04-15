import requests
import time
import pandas as pd

API_KEY = input("Insert API Key: ")

df = pd.read_csv("enhanced_box_office_data(2014-2024)_with_details.csv")

movies = df["Release Group"]

df["Id"] = "N/A"
df["Name"] = "N/A"

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

    df.loc[df["Release Group"] == movie, ["Id", "Name"]] = [
        movie_id,
        data["title"]
    ]

    time.sleep(0.05)

df.to_csv("enhanced_box_office_data(2014-2024)_with_details_2.csv", index = False, encoding = "utf-8")

print("enhanced_box_office_data(2014-2024)_with_details_2.csv")