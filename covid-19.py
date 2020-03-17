import requests
import json

all = requests.get('https://coronavirus-19-api.herokuapp.com/all')
countries = requests.get('https://coronavirus-19-api.herokuapp.com/countries')


cases_all = all.json()['cases']
deaths_all = all.json()['deaths']
recovered_all = all.json()['recovered']
print(f'Cases: {cases_all} \nRecovered: {recovered_all} \nDeaths: {deaths_all}')
