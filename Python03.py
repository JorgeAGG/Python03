
#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'JorgeA'
#Importaciones.
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import twitter


#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'vWRIn7cDDPqwNg0jpz9ej8klZ'
    CONSUMER_SECRET = 'UzQznpC8o3ylUfcbYhKwV6Kt3MoDOgnSxu9Jnn3tmEbKTaHRZe'
    OAUTH_TOKEN = '7730092-BvcE6lKJs8455JE8hyEhYHKXHX5g9X05izuuU47qIX'
    OAUTH_TOKEN_SECRET = 'xGzotzBjBImJNDLAogP60jb3GVlRnp3M9jtp3QSFgJDAI'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

app = Flask(__name__)
GoogleMaps(app)

#busca los twitts
busca="Buenos dias"
twitter_api = oauth_login()
search_results = twitter_api.search.tweets(q=busca, geocode='40.4173175,-3.702233699999965,700km')
data = search_results

lista = []
for estado in data["statuses"]:
        if i["coordinates"]!= None:
            lista.append(i['coordinates']['coordinates'][1])
			lista.append(i['coordinates']['coordinates'][0])
lista = zip(lista[0::1], lista[1::2])




@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=40.3450396,
        lng=-3.6517684,
        markers=lista,
        style="height:800px;width:800px;margin:0;"
    )
    return render_template('template2.html', mymap=mymap)


if __name__ == "__main__":
    app.run(debug=True)