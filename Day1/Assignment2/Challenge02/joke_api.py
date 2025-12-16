import requests
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    except:
        return None
