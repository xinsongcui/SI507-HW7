from flask import Flask, render_template
from secrets import api_key
import requests
from requests import api

app = Flask(__name__)
query = {'api-key':api_key}
url = "https://api.nytimes.com/svc/topstories/v2/technology.json?"
response = requests.get(url, params=query)

res = [x['title'] for x in response.json()['results'][0:5]]
urls = [x['url'] for x in response.json()['results'][0:5]]

@app.route('/')
def hello_world():
    return "<h1>Welcome!</h1>"

@app.route('/name/<username>')
def hello(username):
    return render_template('name.html', name=username)

@app.route('/headlines/<username>')
def headlines(username):
    return render_template('headlines.html', headlines = res, name=username)

@app.route('/links/<username>')
def links(username):
    return render_template('links.html', links = urls, headlines = res, name=username)

# main driver function
if __name__ == '__main__':
    app.run()
