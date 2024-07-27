import requests
from bs4 import BeautifulSoup

import pandas as pd


def all_movies():

    pages = int(input('How many pages you want to search?\n'))
    
    print('searching all movies...')
    
    movies = []
    
    for i in range(1, pages+1):

        print(i)
        url = f'https://nightmovie.co/movies?order=6&movie-page={i}'
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')

        mainhome = soup.find('div', class_='mainHome')
        articles = mainhome.find_all('article')

        

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
            
def all_series():

    pages = int(input('How many pages you want to search?\n'))
    
    print('searching all series...')
    
    my_list = []
    
    for i in range(1, pages+1):

        print(i)
        url = f'https://nightmovie.co/tvshow?tvshow-page={i}'
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')

        traverse_list = soup.find('ul', class_='tvserieslist')
        series_div = traverse_list.find_all('div', class_='tvpadding')


        for series in series_div:

            serie = []

            serie_name = series.find('div', class_='tvmainlink').text[:-8]
            
            year_with_paren = series.find('div', class_='tvmainlink').text[-8:]
            year_with_paren2 = year_with_paren.replace('–)', '')
            year = year_with_paren2.replace('(', '')
            
            detail_ul = series.find('ul', class_='tvdetails')
            duration = detail_ul.find('div', class_='tvduration').text
            
            geners = detail_ul.find('div', class_='genres').text
            
            seasons = detail_ul.find('div', class_='updtime').text
            
            all_li_in_detail_ul = list(detail_ul.descendants)
            status = all_li_in_detail_ul[-27].text[7:]
            
            quality = detail_ul.find('div', class_='qualitynames').text
            
            channel = detail_ul.find('strong', class_='channel').text
            
            broadcast_time = detail_ul.find('li', class_='det45').text[5:].strip()
            
            serie.append(serie_name)
            serie.append(year)
            serie.append(duration)
            serie.append(geners)
            serie.append(seasons)
            serie.append(status)
            serie.append(quality)
            serie.append(channel)
            serie.append(broadcast_time)
            
            
            
            my_list.append(serie)
          
            

    df = pd.DataFrame(my_list, columns=['name', 'year', 'duration', 'genres', 'seasons', 'status', 'quality', 'channel', 'broadcast_time'])

    df.to_csv(f'./files/series {pages}.csv', index=False)

    print("CSV file has been created successfully.")
    
    
if __name__ == '__main__':
    
    all_series()
