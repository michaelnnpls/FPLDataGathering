import pandas as pd
import json 
from bs4 import BeautifulSoup as bs
import requests



r=requests.get(url)
leeds_games=pd.read_html(r.text)[4]
r=requests.get('https://fbref.com/en/squads/60c6b05f/West-Bromwich-Albion-Stats')
wba_games=pd.read_html(r.text)[1]
r=requests.get('https://fbref.com/en/squads/fd962109/Fulham-Stats')
fulham_games=pd.read_html(r.text)[1]

r=requests.get('https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures')
pd.read_html(r.text)[0]

import re
soup=bs(r.text)
soup.find_all('td',{'data-stat':'match_report'})[0]


soup.find_all('a',{'href':re.compile('/en/matches/')})