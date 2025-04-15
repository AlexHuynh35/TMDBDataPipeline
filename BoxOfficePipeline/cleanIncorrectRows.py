import requests
import time
import pandas as pd

API_KEY = input("Insert API Key: ")

df = pd.read_csv("enhanced_box_office_data(2014-2024)_with_details_3.csv")

unmatched_rows = df[df["Matched"] == False]

def find_exact_movie(title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(search_url)

    if response.status_code == 200:
        results = response.json().get("results", [])
        exact_match = next((m for m in results if m["title"].lower() == title.lower()), None)
        return exact_match
    return None

for index, row in unmatched_rows.iterrows():
    print(index)
    movie_name = row["Release Group"]
    exact_movie = find_exact_movie(movie_name)

    if exact_movie:
        movie_id = exact_movie["id"]

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()

        url2 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
        response2 = requests.get(url2)
        data2 = response2.json()
        directors = [crew["name"] for crew in data2["crew"] if crew["job"] == "Director"]

        df.at[index, "Id"] = movie_id
        df.at[index, "Name"] = data["title"]
        df.at[index, "Budget"] = data["budget"]
        df.at[index, "TMDB Revenue"] = data["revenue"]
        df.at[index, "Directors"] = ", ".join(directors)
        df.at[index, "Production Companies"] = ", ".join(company["name"] for company in data["production_companies"])
        df.at[index, "Matched"] = True

    time.sleep(0.1)

df.to_csv("enhanced_box_office_data(2014-2024)_with_details_4.csv", index = False, encoding = "utf-8")

print("enhanced_box_office_data(2014-2024)_with_details_4.csv")