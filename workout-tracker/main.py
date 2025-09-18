import requests
import datetime as dt


APPID = "c95504d2"
APIKEY = "aa58fbbbd4993e99bcf8ee36055a30cf"
sheety_URL = "https://api.sheety.co/62826ef239a8bb6845beb7bd7e16a825/workoutsTracking/workouts"

auth_params = {
    "x-app-id": APPID,
    "x-app-key": APIKEY
}

data = dt.datetime.now()

userquery = input("tell what you did today: ")


paramenters = {
    "query" : userquery
}


response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', json=paramenters,headers=auth_params)

qr = response.json()
workoutname = qr["exercises"][0]["name"]
workouttime = qr["exercises"][0]['duration_min']
cal_burnt = qr["exercises"][0]['nf_calories']


sheety_params ={"workout": {
    "date": data.strftime("%d/%m/%Y"),
    "time": data.strftime("%H:%M:%S"),
    "exercise": workoutname,
    "duration":workouttime,
    "calories":cal_burnt
}}

requests.post(url=sheety_URL,json=sheety_params)




