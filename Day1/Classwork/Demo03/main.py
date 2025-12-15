
import requests
api_key="0c40acd8c58105a459c1c46ce2d02cef"
city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
print("status:", response.status_code)
weather = response.json()
# print(weather)
print("Temperature: ", weather["main"]["temp"])
print("Humidity: ", weather["main"]["humidity"])
print("Wind Speed: ", weather["wind"]["speed"])
