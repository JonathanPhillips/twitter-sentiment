Twitter Sentiment Analyzer for fantasy football research | Python, Natural Language Processing, Pandas
* def_generate_tweets will search tweets about specific players from a list of "Analysts" that are populated in config.py
* NLTK is used to produce a positive, negative, or neutral sentiment utilizing punkt and vader
* The searched players are gathered from 2019 data (included in the repo)
* Requirements.txt included as well

FYI, there is a 512 character search query limit for the Essential/Elevated Twitter API so you will need to consider that when adding more Analysts.  
One way around that would be to break up the query into multiple queries.
You will need an .env file with your Twitter API keys.
