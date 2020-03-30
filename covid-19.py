import requests
from apscheduler.schedulers.background import BackgroundScheduler


def post_data():
    all = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    cases_all = all.json()['cases']
    deaths_all = all.json()['deaths']
    recovered_all = all.json()['recovered']
    requests.post('https://api.thingspeak.com/update?api_key=Y9VNTK6O6MF0ZAEB&field1={}&field2={}&field3={}'.format(str(cases_all), str(recovered_all), str(deaths_all)))


post_data()
scheduler = BackgroundScheduler()
job = scheduler.add_job(post_data, 'interval', seconds=30)
scheduler.start()
while 1 == 1:
    pass
