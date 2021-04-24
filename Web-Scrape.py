import requests
import json
from bs4 import BeautifulSoup

def most_valuable_NBA(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    h3 = soup.find_all('h3')
    nba_teams = []
    for tag in h3:
        #print(tag.text)
        h4 = soup.find('h4').text
        #print(value)
        nba_teams.append((tag.text, h4[9:]))
    return nba_teams

def most_valuable_NFL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    h2 = soup.find_all('h2')
    #print(h2)
    nfl_teams = []
    for tag in h2:
        name = tag.text
        value = tag.find_next('p').text
        #print(value)
        nfl_teams.append((name, value[9:]))
    nfl_teams = nfl_teams[1:]
    nfl_teams_sorted = sorted(nfl_teams, key = lambda x: x[1]) 
    return nfl_teams_sorted[1:]

def most_valuable_NHL(url):
    nhl_teams = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows:
        name = row.find('td')
        value = name.find_next('td')
        tup = (name.text, value.text)
        nhl_teams.append(tup)
    return nhl_teams[1:0]

def most_valuable_MLB(url):
    mlb_teams = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags = soup.find_all('li')
    for tag in tags:
        name = tag.text.split(',')
        if len(name) > 1:
            mlb_teams.append((name[0], name[1]))
    print(mlb_teams.index(('New York Yankees', ' $5.250 billion')))
    return mlb_teams[2:]

        

#print(most_valuable_NBA('https://www.forbes.com/sites/kurtbadenhausen/2021/02/10/nba-team-values-2021-knicks-keep-top-spot-at-5-billion-warriors-bump-lakers-for-second-place/?sh=37469da645b7'))
#print(most_valuable_NFL('https://www.forbes.com/sites/mikeozanian/2020/09/10/the-nfls-most-valuable-teams-2020-how-much-is-your-favorite-team-worth/?sh=57f46abe2ba4'))
#print(most_valuable_NHL('https://dailyhive.com/vancouver/nhl-team-values-forbes-2019'))
#print(most_valuable_MLB('https://brobible.com/sports/article/most-valuable-mlb-teams-2021-yankees-redsox/'))



    