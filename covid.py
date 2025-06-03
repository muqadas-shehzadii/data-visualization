# import pandas as pd
import requests
from io import StringIO
import datetime
import time
import matplotlib.pyplot as plt

# ---------------- DECORATORS ----------------

def logger(func):
    def wrapper(*args, **kwargs):
        time_called = datetime.datetime.now()
        print(f"[LOG] Function '{func.__name__}' was called at {time_called}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

def cache(func):
    _cache = {}
    def wrapper(*args):
        if args in _cache:
            print(f"[CACHE] Returning cached result for {func.__name__}{args}")
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        print(f"[CACHE] Caching result for {func.__name__}{args}")
        return result
    return wrapper

# ---------------- DATA FETCHING ----------------

@cache
@timer
@logger
def fetch_covid_data():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    response = requests.get(url)

    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        print(f"[DATA] Fetched {len(df)} rows.")
        return df
    else:
        raise Exception(f"Failed to fetch data; {response.status_code}")

# ---------------- CLEANING ----------------

@logger
@timer
def clean_data(df):
    df.dropna(inplace=True)
    return df

# ---------------- FILTERING ----------------

def filter_country_data(df, country):
    return df[df['location'].str.lower() == country.lower()]

# ---------------- PLOTTING ----------------

def plot_covid_by_country(df, country):
    df = df.sort_values(by='date')
    df['date'] = pd.to_datetime(df['date'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['new_cases'], marker='o', linestyle='-')
    plt.title(f'COVID New Cases Over Time - {country.title()}')
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------------- PIPELINE ----------------

def run_pipeline(country):
    df = fetch_covid_data()
    df = clean_data(df)
    country_df = filter_country_data(df, country)
    plot_covid_by_country(country_df, country)

# ---------------- RUN ----------------

run_pipeline('Pakistan')
