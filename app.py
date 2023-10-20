"""
Daniel Gregorio
Riot Games Leaderboard app
"""
import os

import flask
import requests

# making our flask app
app = flask.Flask(__name__)
# route for home page
@app.route('/',  methods=['GET'])
def index():
    return flask.render_template('index.html')
# route for valorant leaderboard page
@app.route('/valLeaders',  methods=['GET'])
def valLeaders():
    # getting information from api and storing it in valorant variable
    valorant = requests.get(f"https://na.api.riotgames.com/val/ranked/v1/leaderboards/by-act/{os.environ.get('ACT_ID')}?size=100&startIndex=0&api_key={os.environ.get('API_KEY')}")
    # creating a list where players will be stored 
    players = []
    for i in range(100):
        # try except block for the table creation
        try:
            # API returns dictionary. players takes dictionary values and puts 
            # it in a list containing player gamertag, rank rating(rr), and number of wins 
            players.append((i+1, valorant.json()['players'][i]['gameName'], 
            valorant.json()['players'][i]['rankedRating'], valorant.json()['players'][i]['numberOfWins']))
        except:
            # data was unable to load so the file failed
            print("Invalid Data")
    return flask.render_template('valLeaders.html', players=players)
# route for league leaderboard page
@app.route('/lolLeaders',  methods=['GET'])
def lolLeaders():
    # getting information from api and storing it in valorant variable
    league = requests.get(f"https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1&api_key={os.environ.get('API_KEY')}")
    # creating a list where players will be stored 
    players = []
    for i in range(100):
        # try except block for the table creation
        try:
            # API returns dictionary. players takes dictionary values and puts 
            # it in a list containing player gamertag, league points(lp), and number of wins 
            players.append((i+1, league.json()[i]['summonerName'], 
            league.json()[i]['leaguePoints'], league.json()[i]['wins']))
        except:
            # data was unable to load so the file failed
            print("Invalid Data")
    return flask.render_template('lolLeaders.html', players=players)
# main 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)