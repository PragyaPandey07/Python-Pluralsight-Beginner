movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Godzilla": "3:00pm",
    "Home Alone": "2:30pm",
    "Up": "4:00pm",
    "Migration": "7:00 pm"
}

print("We are currently showing: \n")
for key in movies :
    print(key)

movie_choice = input("Which movie would you like to watch? \n")

if movies.get(movie_choice) == None :
    print("Currently not streaming", movie_choice)
else :
    print("Streaming", movie_choice, "at", movies[movie_choice], "!!") 