# IMDb Web Scraper and API

### Overview

This project consists of two main components: a Python web scraping script (`scraping.py`) and a FastAPI-based API (`main.py`) that serves data from the IMDb Top 100 Movies list. The web scraper collects movie data from IMDb's website and stores it in a CSV file, while the API allows users to query and retrieve movie information based on specific criteria.

### Project Structure

The project is structured as follows:

- `scraping.py`: This Python script is responsible for scraping movie data from IMDb's Top 100 Movies list and saving it to a CSV file.

- `main.py`: This file contains the FastAPI-based web API that provides endpoints for searching movies by year, name, and retrieving the top movies.

### How the Web Scraper Works

The web scraper (`scraping.py`) follows the following steps to collect movie data from IMDb:

1. Imports the necessary libraries, including requests, BeautifulSoup, and pandas.

2. Specifies the IMDb URL for the Top 100 Movies list.

3. Sets request headers to specify the preferred language.

4. Sends an HTTP GET request to the IMDb URL to retrieve the page content.

5. Parses the HTML content using BeautifulSoup.

6. Extracts movie attributes (name, year, runtime, IMDb rating, metascore, number of votes, and US gross) and stores them in lists.

7. Creates a Pandas DataFrame to organize the collected data.

8. Cleans and formats the data by extracting numerical values, converting types, and handling missing values.

9. Exports the data to a CSV file (`top_100_movies.csv`).

### Running the Application
The project relies on the following libraries:

- `requests` for sending HTTP requests.
- `BeautifulSoup` for parsing HTML content.
- `pandas` for data manipulation and storage.
- `re` for regular expression matching (used in the API).

Make sure to install these dependencies before running the scripts.

To run the application locally you can run this command in the terminal:

```bash
uvicorn main:app --reload
```

### Endpoints

The FastAPI-based API (`main.py`) provides the following endpoints:

- `/search_by_year`: Allows users to search for movies by specifying a year. It returns a list of movies from that year.

- `/search_by_name`: Enables users to search for movies by specifying a name. It returns a list of movies whose titles contain the specified name.

- `/top_movies`: Returns the entire list of top 100 movies as scraped from IMDb.

example:
- ` curl http://localhost:8000/top_movies`
- ` curl http://localhost:8000/search_by_name?name=Matrix`
- ` curl http://localhost:8000/search_by_year?year=1999`