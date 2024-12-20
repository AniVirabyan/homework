import requests
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
def main():
    evaluations = []
    jokes=[]   
    for i in range(10):     
        joke_data = get_joke()        
        if joke_data:
            setup = joke_data['setup']
            punchline = joke_data['punchline'] 
                     
            print("\nJoke " + str(i+1) + " from  10:")
            while True:
                try:
                    evaluation = int(input("Rate the joke : "))
                    if 1 <= evaluation <= 10:
                        evaluations.append(evaluation)
                        break
                    else:
                        print("from 1 to 10")
                except ValueError:
                    print("Number Only")
    with open("jokes.txt","w") as file:
        for i in range(len(jokes)):
            file.write("joke"+str(i+1)+"\n")
            file.write("Rating"+str(evaluations[i])+"\n")
        print("All jokes and ratings have been saved to 'jokes.txt'.")
if __name__=="__main__":
    main()

            



