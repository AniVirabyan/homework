import requests
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
evaluations = []
for i in range(10):     
    joke_data = get_joke()
    
    if joke_data:
        setup = joke_data['setup']
        punchline = joke_data['punchline']
        
        print("\nJoke " + str(i+1) + " from  10:")
        try:
            evaluation = int(input("Rate the joke : "))
            if 1 <= evaluation <= 10:
                evaluations.append(evaluation)
            else:
                print("from 1 to 10")
        except ValueError:
            print("Number Only")
    



