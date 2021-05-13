# 1
# import requests
# import json
#
# key = 'ecb65c5b4cab1e093e9b71fdd6020bbe'
# lat = 55.5
# lon = 100
# cnt = 50
# payload = {'appid': key, 'lat': lat, 'lon': lon, 'units': 'metric', 'cnt': cnt}
# r = requests.get('http://api.openweathermap.org/data/2.5/find', params=payload)
# print(r.status_code)
# print(r.url)
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.text)
#
# # 2
#
# res = r.json()
# print(json.dumps(res, indent=4))
#
# with open('weatherData.json', 'w') as f:
#     json.dump(res, f, indent=4)
#
# # 4
#
# import sqlite3
#
# conn = sqlite3.connect('weather_db.sqlite')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS weather
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#              country VARCHAR(15),
#              temperature NUMBER,
#              feels_like NUMBER,
#              humidity NUMBER,
#              weather_description VARCHAR(30)
#              )''')  # ცხრილში იწერება გრძედის 55.5 და განედის 100 გეოგრაფიულ კოორდინატებში მოქცეული 50 ქვეყნის შესახებ ინფორმაცია. კონკრეტულად
# # ინახება ქვეყნის სახელი, მიმდინარე ტემპერატურა, როგორ აღიქმება ხლა ეს ტემპერატურა რეალურად, ტენიანობის მაჩვენბელი და ამინდის სიტყვიერი აღწერა
#
# # 3
# all_rows = []
# for each in res["list"]:
#     country = each["name"]
#     temp = each['main']['temp']
#     feels_like = each["main"]["feels_like"]
#     humidity = each["main"]["humidity"]
#     weather_description = each["weather"][0]["description"]
#     row = (country, temp, feels_like, humidity, weather_description)
#     all_rows.append(row)
#
# c.executemany('INSERT INTO weather(country, temperature, feels_like, humidity, weather_description) VALUES (?,?,?,?,?)',
#               all_rows)
#
# conn.commit()
# conn.close()
