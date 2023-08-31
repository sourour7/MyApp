from fastapi import FastAPI, Query
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

app = FastAPI()

def scrape_movies():
    imdb_url = "https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv"
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    results = requests.get(imdb_url, headers=headers)
    movie_soup = BeautifulSoup(results.text, "html.parser")

    movie_details = []

    movie_div = movie_soup.find_all('div', class_='lister-item mode-advanced')
    for container in movie_div:
        name = container.h3.a.text
        year_text = container.h3.find('span', class_='lister-item-year').text
        year_match = re.search(r'\d{4}', year_text)
        year = int(year_match.group()) if year_match else None

        rating_text = container.find('div', class_='inline-block ratings-imdb-rating').strong.text
        rating = float(rating_text) if rating_text else None

        runtime_text = container.p.find('span', class_='runtime').text
        runtime_match = re.search(r'\d+', runtime_text)
        runtime = int(runtime_match.group()) if runtime_match else None

        metascore_text = container.find('span', class_='metascore').text.strip() if container.find('span', class_='metascore') else '-'
        metascore = int(metascore_text) if metascore_text != '-' else None

        gross_text = container.find('p', class_='sort-num_votes-visible').find_all('span', attrs={'name': 'nv'})[-1]['data-value'] if container.find('p', class_='sort-num_votes-visible').find_all('span', attrs={'name': 'nv'}) else '-'
        gross = int(gross_text) if gross_text != '-' else None

        votes_text = container.find('p', class_='sort-num_votes-visible').find_all('span', attrs={'name': 'nv'})[0]['data-value'] if container.find('p', class_='sort-num_votes-visible').find_all('span', attrs={'name': 'nv'}) else '-'
        votes = int(votes_text.replace(',', '')) if votes_text != '-' else None

        

        movie_details.append({
            'movie_name': name,
            'movie_year': year,
            'movie_rating': rating,
            'movie_runtime': runtime,
            'metascore': metascore,
            'gross': gross,
            'votes': votes,
            
        })

    return movie_details


@app.get("/search_by_year")
def search_by_year(year: int = Query(..., description="Année du film")):
    movies_data = scrape_movies()
    filtered_movies = [movie for movie in movies_data if movie['movie_year'] == year]
    return filtered_movies

@app.get("/search_by_name")
def search_by_name(name: str = Query(..., description="Nom du film")):
    movies_data = scrape_movies()
    filtered_movies = [movie for movie in movies_data if name.lower() in movie['movie_name'].lower()]
    return filtered_movies



@app.get("/top_movies")
def get_top_movies():
    movies_data = scrape_movies()
    
    return movies_data

