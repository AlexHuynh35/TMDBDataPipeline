import requests
import datetime
import pandas as pd

API_KEY = input("Insert API Key: ")
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

today = datetime.date.today()
ten_years_ago = today.replace(year = today.year - 10)
company_ids = [2, 3, 420, 1, 25, 127929, 9383, 19366, 17037, 7521]

params = {
    "api_key": API_KEY,
    "with_companies": company_ids[0],
    "primary_release_date.gte": ten_years_ago.strftime("%Y-%m-%d"),
    "primary_release_date.lte": today.strftime("%Y-%m-%d"),
    "sort_by": "primary_release_date.desc",
    "page": 1
}

movies = []

for company_id in company_ids:
    params["with_companies"] = company_id
    params["page"] = 1
    response = requests.get(BASE_URL, params = params)
    data = response.json()
    max_pages = data["total_pages"]
    print("Collecting data for", company_id, "with", max_pages, "pages")
    for i in range(1, max_pages + 1):
        params["page"] = i
        response = requests.get(BASE_URL, params = params)
        data = response.json()
        movies.extend(data["results"])
    print("Collected data for", company_id)
    
df = pd.DataFrame(movies)
df = df[["id", "title", "release_date", "genre_ids", "vote_average", "vote_count"]]
df.to_csv("disney_movies.csv", index = False, encoding = "utf-8")

print("Data saved to disney_movies.csv")
