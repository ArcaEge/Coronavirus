import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)

all = requests.get('https://coronavirus-19-api.herokuapp.com/all')
countries = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
a = countries.json()
# name = []
# cases = []
# deaths = []
# recovered = []
# active = []
# critical = []
# for i in a:
#     fname = i['country']
#     name.append(fname)
#     fcases = i['cases']
#     cases.append(fcases)
#     fdeaths = i['deaths']
#     deaths.append(fdeaths)
#     frecovered = i['recovered']
#     recovered.append(frecovered)
#     factive = i['active']
#     active.append(factive)
#     fcritical = i['critical']
#     critical.append(fcritical)


cases_all = all.json()['cases']
deaths_all = all.json()['deaths']
recovered_all = all.json()['recovered']


@app.route('/')
def home():
    return render_template('index.html', cases=cases_all, deaths=deaths_all, recovered=recovered_all)


@app.route('/worldwide')
def world():
    return render_template('worldwide.html', cases=cases_all, deaths=deaths_all, recovered=recovered_all)


@app.route('/countries')
def country():
    return render_template('countries.html', a=a)


@app.route('/countries/<string:name_of_country>')
def country_details(name_of_country):
    b = 0
    for i in countries.json():
        if (i['country'] == name_of_country):
             b = i
    # if b == 0:
    #     return redirect('/countries')
    # else:
    return render_template('country.html', b=b)


if __name__ == '__main__':
    app.run()
