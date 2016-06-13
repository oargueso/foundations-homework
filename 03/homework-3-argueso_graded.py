#graded 14/14
#Olaya Argueso Perez
#2016-05-30
#Homework 3

#LISTS
#List of seven countries and for loop to print each one
countries = ['Kenya', 'Morocco', 'Bangladesh', 'Argentina', 'Afghanistan', 'Spain', 'Greece']
for country in countries:
    print(country)

#Sort them permanently and display the first element
sorted_countries = sorted(countries)
print(sorted_countries[0])

#Display second-to-last
countries_lenght = len(sorted_countries)
second_to_last_position = countries_lenght - 2
second_to_last = sorted_countries[second_to_last_position]

#TA-STEPHAN: Nice! Though you could also sipmle do
#sorted_countries[-2]
print(second_to_last)

#Delete one element using its name
sorted_countries.remove('Bangladesh')

#For loop (¿He entendido bien lo que quería?)
for country in sorted_countries:
    print(country)

#DICTIONARIES
#Dictionary called 'tree'
tree = {'name': 'Major Oak', 'species': 'Pedunculate oak', 'age': 800, 'location_name': 'Sherwood Forest', 'latitude': 53.2026808559, 'longitude': -1.07032305204}
print(tree['name'], "is a", tree['age'], "years old tree that is in" , tree['location_name'])

#Location regarding NYC
if tree['latitude'] < 40.7128:
    print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC")
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC")

#Age of user and tree (solution 1)
user_age = input("How old are you?")
if int(user_age) > tree['age']:
    print("You are", int(user_age) - tree['age'], "years older than", tree['name'])
elif int(user_age) < tree['age']:
    print(tree['name'], "was", tree['age'] - int(user_age), "years old when you were born")

#Age of user and tree (solution 2)
user_age = input("How old are you?")
if int(user_age) > tree['age']:
    print("You are", int(user_age) - tree['age'], "years older than", tree['name'])
else:
    print(tree['name'], "was", tree['age'] - int(user_age), "years old when you were born")


#LIST OF DICTIONARIES
#I take for granted Santiago means Santiago de Chile and not Santiago de Compostela (Spain) ;)
moscow = {'name': 'Moscow', 'latitude':55.751244, 'longitude':37.618423}
tehran = {'name': 'Tehran', 'latitude':35.715298, 'longitude':51.4215100}
falkland_islands = {'name': 'Falkland Islands', 'latitude':-52.094273, 'longitude':-59.0000000}
seoul = {'name': 'Seoul', 'latitude':37.532600, 'longitude':127.024612}
santiago_de_chile = {'name': 'Santiago de Chile', 'latitude':-33.447487, 'longitude':-70.673676}

countries = [moscow, tehran, falkland_islands, seoul, santiago_de_chile]

#Loop 1
for country in countries:
    if country['latitude'] < 0:
        print(country['name'], "is below the equator")
    elif country['latitude'] > 0:
        print(country['name'], "is above the equator")
    if country['name'] == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic Zone")

#Loop 2
for country in countries:
    if country['latitude'] < tree['latitude']:
        print(country['name'], "is south to", tree['name'])
    elif country['latitude'] > tree['latitude']:
        print(country['name'], "is north to", tree['name'])
