
# coding: utf-8

# In[2]:

import requests
response = requests.get("https://api.forecast.io/forecast/XXXXXXXX/43.360259,-5.844758")
data_aviles = response.json()


# In[3]:

def get_temperature(t):
    temperature = t['currently']['temperature']
    return temperature


# In[4]:

def get_summary(s):
    summary = s['currently']['summary'].lower()
    return summary


# In[5]:

def get_temp_feeling(t):
    data = t['daily']['data']
    for item in data:
        temp_feeling = item['temperatureMin']
        if temp_feeling < 60:
            return "cold"
        elif temp_feeling > 60:
            return "moderate"
        elif temp_feeling < 75:
            return "warm"
        elif temp_feeling > 75:
            return "hot"


# In[6]:

def get_high_temp(t):
    data = t['daily']['data']
    for item in data:
        high_temp = item['temperatureMin']
        return high_temp


# In[7]:

def get_low_temp(t):
    data = t['daily']['data']
    for item in data:
        low_temp = item['temperatureMax']
        return low_temp


# In[8]:

def get_rain(t):
    data = t['daily']['data']
    for item in data:
        rain = item['precipType']
        if (rain == "rain") or (rain == "snow") or (rain == "sleet"):
            return "Grab your umbrella!"
        else:
            return "No need for umbrella today."


# In[9]:

def get_data(d):
    return "Right now it is " + str(get_temperature(d)) + " degrees out in Avilés and " + get_summary(d) + ". Today will be " + get_temp_feeling(d) + " with a high of " + str(get_high_temp(d)) + " and a low of " + str(get_low_temp(d)) + ". " + get_rain(d) + "."

get_data(data_aviles)


# In[10]:

import time
def send_simple_message():
    date_string = time.strftime("%B %-d %Y")
    return requests.post(
        "https://api.mailgun.net/v3/xxxxxxxxxx.mailgun.org/messages",
        auth=("api", "key-xxxxxxxxxxxxxxxxxx"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxxxxxxxxxx.mailgun.org>",
              "to": "Olaya Argueso <arguesoperezolaya@gmail.com>",
              "subject": "8AM Weather forecast" + date_string,
              "text": get_data(data_aviles)})
    
send_simple_message()
# In[ ]:

# CRONTAB JOB: 0 8 * * * python3 homework-10-argueso-API-servers.py


