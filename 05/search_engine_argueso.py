# Make a non-IPython Notebook that automates browsing for top tracks
#Prompts for an artist
#you pu t it in, displays the results, asks which one you want (numbered)
#you enter a number
#It displays their top tracks, then their MOST popular album and their least popular album. if they only have one album it
#says that they only have one album.

import requests

artist = input("Which artist do you like? ")
# Retrieving all the artists that match the user's input
for item in artist:
    artist_url = "https://api.spotify.com/v1/search?q=" + artist + "&type=artist"
    response = requests.get(artist_url)
    data = response.json()
    artist_data = data['artists']['items']
# Adding those matches to a list and numbering them
artist_number = 0
artist_list = []
artist_list_id = []
for item in artist_data:
    artist_name = item['name']
    artist_number = artist_number + 1
    print(artist_number, artist_name)
    artist_list.append(artist_name)
" ".join(artist_list)

chosen_artist = input("Which one do you mean? Enter number to see the artist's top tracks: ")
# Getting the exact artist the user has chosen (numbered)
for item in chosen_artist:
    # Matching the number the user is entering with an artist in the list
    item = artist_list[int(item) - 1]
    # Getting that artist's information
    artist_url = "https://api.spotify.com/v1/search?q=" + item + "&type=artist"
    response = requests.get(artist_url)
    data = response.json()
    artist_data = data['artists']['items']
    print(artist_data)
    # Retrieving the artist's id to fetch their top tracks
    # I could not solve the problem of avoiding Spotify API to give all the tracks
    # for every single artist with a similar name to the one I was looking for

    #for item in artist_data:
        #artist_id = item['id']
        #artist_top_tracks_url = "https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks?country=US"
        #response = requests.get(artist_top_tracks_url)
        #top_tracks_data = response.json()
        #top_tracks = top_tracks_data['tracks']
        #for track in top_tracks:
            #track_name = track['name']
            #print(track_name)
