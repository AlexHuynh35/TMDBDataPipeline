import requests
import pandas as pd

API_KEY = input("Insert API Key: ")

company = "Searchlight Pictures"
companies = []

url = f"https://api.themoviedb.org/3/search/company?api_key={API_KEY}&query={company}"
response = requests.get(url)
data = response.json()
max_pages = data["total_pages"]

for i in range(1, max_pages + 1):
    url = f"https://api.themoviedb.org/3/search/company?api_key={API_KEY}&query={company}&page={i}"
    response = requests.get(url)
    data = response.json()
    companies.extend(data["results"])

df = pd.DataFrame(companies)
df = df[["id", "name"]]
df.to_csv("company_id.csv", index = False, encoding = "utf-8")