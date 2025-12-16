import requests

API_KEY = "pub_64cd67a7049b4ccc8daa7f93de4095a2"  

def fetch_top_headlines(country="in"):
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country={country}&language=en"

    try:
        response = requests.get(url)
        data = response.json()

        return data.get("results", [])   

    except:
        return None
