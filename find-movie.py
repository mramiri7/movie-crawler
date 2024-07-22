import requests
from bs4 import BeautifulSoup

import pandas as pd




for i in range(2):
    
    
    url = f'https://nightmovie.co/movies?order=6&movie-page={i}'
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    mainhome = soup.find('div', class_='mainHome')
    articles = mainhome.find_all('article')
    
    movies = []
    
    for article in articles:
        
        movie = []
        
        movie_name = article.find('a').text[:-6]
        
        whole_name = article.find('a').text
        split_text = whole_name.split('(')
        year_with_paren = split_text[1]
        year = year_with_paren.replace(')', '')
        
        
        
        ul = article.find('ul', class_='moviedetails')
        country = ul.find('div', class_='countries').text

        geners = ul.find('div', class_='genres').text
        movie_time = ul.find('div', class_='duration').text

        actors = ul.find('div', class_='actors').text

        all_li = ul.find_all('li')
        director = all_li[-1].find('a').text
        
        movie.append(movie_name)
        movie.append(year)
        movie.append(country)
        movie.append(geners)
        movie.append(movie_time)
        movie.append(actors)
        movie.append(director)

        movies.append(movie)
        
df = pd.DataFrame(movies, columns=['name', 'year', 'country', 'genres', 'movie_time', 'actors', 'director'])
    
df.to_csv('movies.csv', index=False)

print("CSV file has been created successfully.")
