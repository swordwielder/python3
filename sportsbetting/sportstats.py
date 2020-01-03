import os
import requests
from dotenv import load_dotenv

load_dotenv()
SPORTS = os.getenv('SPORTS')
#
# "<2fb6d1de76ca4c1ab01aae7942732615>"
sport=f'https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2014?key={SPORTS}'
