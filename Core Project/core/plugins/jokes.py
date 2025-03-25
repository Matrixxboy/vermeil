import requests

def tell_joke():
    try:
        repsonse = requests.get('https://official-joke-api.appspot.com/random_joke',headers={'cache-control': 'no-cache'})
        
        if repsonse.status_code == 200:
            joke_data = repsonse.json()
            setup = joke_data.get("setup","No joke found.")
            punchline = joke_data.get("punchline","")
            
            return f"{setup} ... {punchline}"
        else:
            print("Error: Unable to fetch a joke.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except KeyError:
        print("Error: Invalid response format.")
        
if __name__ == "__main__":
    tell_joke()
