import pandas as pd
from bs4 import BeautifulSoup
import requests

def historical_data(years):
    fifa = []
    for year in years:
        fifa.append(get_matches_by_year(year))
    df_fifa = pd.concat(fifa, ignore_index=True)
    df_fifa.to_csv("fifa_results.csv", index=False)

def get_matches_by_year(yr):
    web = f'https://en.wikipedia.org/wiki/{yr}_FIFA_World_Cup'
    response = requests.get(web) #200
    content = response.text #get the content of website
    soup = BeautifulSoup(content, 'lxml') #convert into xml
    # print(soup.prettify()) #observe the document to find the pattern

    # search for a tag that has a certain CSS class, but the name of the CSS attribute
    # search by CSS class using the keyword argument class_. (class is a reserved word in python)
    matches = soup.find_all('div', class_='footballbox') #<div class='footballbox'> reacords all matches

    home = []
    away = []
    score = []
    date = []
    
    for match in matches:
        # get each match
        home.append(match.find('th', class_='fhome').get_text())
        away.append(match.find('th', class_='faway').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        date.append(match.find('div', class_='fdate').get_text())
        
    # create a dictionary to store the structured data
    dict_football = {'home': home, 'score': score, 'away': away, 'date': date}
    df_football = pd.DataFrame(dict_football)
    return df_football