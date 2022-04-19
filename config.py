from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')

load_dotenv(env_path)

class Config:
    ACCESS_TOKEN_API_KEY = os.getenv('ACCESS_TOKEN_API_KEY')
    ACCESS_TOKEN_API_SECRET = os.getenv('ACCESS_TOKEN_API_SECRET')
    CONSUMER_TWITTER_API_KEY = os.getenv('CONSUMER_TWITTER_API_KEY')
    CONSUMER_TWITTER_API_SECRET = os.getenv('CONSUMER_TWITTER_API_SECRET')
    TWITTER_SEARCH_BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"
    ANALYSTS = {
        'NFL Fantasy Football': 'NFLFantasy',
        'PFF Fantasy Football': 'PFF_Fantasy',
        'FantasyPros': 'FantasyPros',
        'Bleacher Report': 'BleacherReport',
        'Danny Heifetz':'Danny_Heifetz',
        'Kyle Yates':'KyleYNFL',
        'Joe Bryant':'Football_Guys',
        'Nathan Jahnke':'PFF_NateJahnke',
        'Justin Boone':'justinboone',
        'Kyle Soppe':'KyleSoppeESPN',
        'Rob Waziak':'WazNFL',
        'Mina Kimes':'minakimes',
        'ProFootballDoc':'ProFootballDoc',
        'Andy Ruther':'AndyRuther',
        'Adam Aizer':'AdamAizer',
        'Heath Cummings':'heathcummingssr',
        'Jamey Eisenberg':'JameyEisenberg',
        'Michael Fabiano':'Michael_Fabiano',
        'Ian Rapoport':'RapSheet',
        'Field Yates':'FieldYates',
        'Adam Schefter':'AdamSchefter',
        'Matthew Berry':'MatthewBerryTMR',
        'Stephania Bell':'Stephania_ESPN',
        'Adam Levitan':'adamlevitan',
    }
