from flask import Flask
from flask import jsonify,redirect,url_for,request,render_template
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


@app.route('/getreq',methods = ['GET','POST'])
def handling_req():
	city = request.form['city']
	s = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=e8e89ff69324ed8ff44cd33519b12a8f".format(city)
	x = requests.get(s)
	y = json.loads(x.text)['main']['temp']
	c = y-273
	return "city : %0.2f degree C"%c


@app.route('/redirect')
def red():
	return redirect(url_for('func1',city="delhi"))


@app.route('/webpage')
def webpage():
	return render_template('linkshortener.html')


@app.route('/linkshortener',methods = ['GET'])
def linkshort():
	x = request.args
	


if __name__ == '__main__':
   app.run(port=8000, debug = True)