import requests
import smtplib
api_key="b4bdf7c33786630fe0c046278f094d34"
owm_endpoint="https://api.openweathermap.org/data/2.5/onecall"
my_lat=17.000538
my_lng=81.804031

my_email="saddikutivishnu2019@iiitkottayam.ac.in"
my_password="ramahyma"


parameters={
    "lat":my_lat,
    "lng":my_lng,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response=requests.get(url=owm_endpoint,params=parameters)
data=response.json()
print(data)
'''
weather_slice=data["hourly"][:12]

will_rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
        break
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email, to_addrs="kamalakarvishnu.2001@gmail.com",
                        msg=f"Subject:Rain Alert!\n\nBring an umbrella")
#print(["weather"][0]["id"])
#print(data)
'''