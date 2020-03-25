import requests
from flask import Flask, render_template, redirect
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

all = requests.get('https://coronavirus-19-api.herokuapp.com/all')
countries = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
a = countries.json()


cases_all = all.json()['cases']
deaths_all = all.json()['deaths']
recovered_all = all.json()['recovered']


def post_data():
    all = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    cases_all = all.json()['cases']
    deaths_all = all.json()['deaths']
    recovered_all = all.json()['recovered']
    requests.post('https://api.thingspeak.com/update?api_key=Y9VNTK6O6MF0ZAEB&field1={}&field2={}&field3={}'.format(str(cases_all), str(recovered_all), str(deaths_all)))


@app.route('/')
def home():
    cases_formatted = '{:,d}'.format(cases_all)
    deaths_formatted = '{:,d}'.format(deaths_all)
    recovered_formatted = '{:,d}'.format(recovered_all)
    return render_template('index.html', cases=cases_formatted, deaths=deaths_formatted, recovered=recovered_formatted)

@app.route('/worldwide')
def world():
    cases_formatted = '{:,d}'.format(cases_all)
    deaths_formatted = '{:,d}'.format(deaths_all)
    recovered_formatted = '{:,d}'.format(recovered_all)
    return render_template('worldwide.html', cases=cases_formatted, deaths=deaths_formatted, recovered=recovered_formatted)


@app.route('/countries')
def country():
    return render_template('countries.html', a=a)


@app.route('/countries/<string:name_of_country>')
def country_details(name_of_country):
    b = 0
    for i in countries.json():
        if (i['country'] == name_of_country):
            b = i
    if b == 0:
        return redirect('/countries')
    else:
        return render_template('country.html', b=b)


scheduler = BackgroundScheduler()
job = scheduler.add_job(post_data, 'interval', minutes=1440)
scheduler.start()
if __name__ == '__main__':
    app.run()
