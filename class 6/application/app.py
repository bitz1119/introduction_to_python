from flask import Flask
from flask import jsonify,redirect,url_for,request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
   return 'abcde'

@app.route('/<xyz>/<int:cllg>')
def bittoo(xyz,cllg):
	return "hey {} this side from {}".format(xyz,cllg)


@app.route('/weather/<city>')
def func1(city):
	s = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=e8e89ff69324ed8ff44cd33519b12a8f".format(city)
	x = requests.get(s)
	y = json.loads(x.text)['main']['temp']
	c = y-273
	return "city : %0.2f degree C"%c


@app.route('/getreq',methods = ['GET'])
def handling_req():
	city = request.args['city']
	s = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=e8e89ff69324ed8ff44cd33519b12a8f".format(city)
	x = requests.get(s)
	y = json.loads(x.text)['main']['temp']
	c = y-273
	return "city : %0.2f degree C"%c


@app.route('/redirect')
def red():
	return redirect(url_for('func1',city="delhi"))


if __name__ == '__main__':
   app.run(port=8000, debug = True)