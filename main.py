from bs4 import BeautifulSoup
import requests

import pandas as pd

def imdb_movies_250():

    html_text = requests.get('https://digimoviez.com/top-250-movies/').text

    soup = BeautifulSoup(html_text, 'lxml')

    
    loop_item_lists = soup.find_all('div', class_='loop_item_list')

    movies = []
    
    for loop_item in loop_item_lists:
        meta_list = loop_item.find('div', class_='meta_loop_list')
        item_metas = meta_list.find_all('div', class_='item_meta')

        temp = []
        
        for item in item_metas:
            title = loop_item.find('h2', class_='title_h2').text.lstrip()
            date_published = loop_item.find('span', class_='res_item').text
            
            temp.append(title)
            temp.append(date_published)

            label = item.find('span', class_='lab_item')
            if label and 'ژانر :' in label.text:

                genre = label.find_next_sibling(text=True).strip()
                # title = loop_item.find('h2', class_='title_h2').find('a').text.strip()
                # print('عنوان:', title)
                temp.append(genre)
                break
            if label and 'رده سنی :' in label.text:
                age = label.find_next_sibling(text=True).strip()
                temp.append(age)

            if label and 'زمان :' in label.text:
                
                movie_time = label.find_next_sibling(text=True).strip()
                temp.append(movie_time)
        
        
        movies.append(temp)


        print('م******************************************************************م')
        print(movies)
        
def imdb_series_250():
    
    html_text = requests.get('https://digimoviez.com/top-250-tv-series/').text

    soup = BeautifulSoup(html_text, 'lxml')

    
    loop_item_lists = soup.find_all('div', class_='loop_item_list')

    
    for loop_item in loop_item_lists:
        meta_list = loop_item.find('div', class_='meta_loop_list')
        item_metas = meta_list.find_all('div', class_='item_meta')

        for item in item_metas:
            title = loop_item.find('h2', class_='title_h2').text.lstrip()
            date_published = loop_item.find('span', class_='res_item').text

            label = item.find('span', class_='lab_item')
            if label and 'ژانر :' in label.text:

                genre = label.find_next_sibling(text=True).strip()
                # title = loop_item.find('h2', class_='title_h2').find('a').text.strip()
                # print('عنوان:', title)
                print('ژانر:', genre)
                break
            if label and 'رده سنی :' in label.text:
                age = label.find_next_sibling(text=True).strip()
                print('رده سنی:', age)

            if label and 'زمان :' in label.text:
                print('نام اثر: ', title)
                print('سال انتشار: ', date_published)
                movie_time = label.find_next_sibling(text=True).strip()
                print('زمان:', movie_time)


        print('م******************************************************************م')
        print()
    

if __name__ == '__main__':
    print('please select one:\nmovies or series :')
    selection = input()
    
    if selection == 'movies':
        imdb_movies_250()
    
    elif selection == 'series': 
        imdb_series_250()
        
    else:
        print('Bye')