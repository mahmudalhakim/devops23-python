#  Övningsuppgift 13.3

import requests

# Hämta data från API:et
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)

# OBS! Returnerar en sträng
print(r.text)
print(type(r.text))
print(r.text[0])  # {

# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
# Returnerar en JSON
artists = r.json()
print(artists)
print(type(artists))

artists_list = artists['artists']
print(artists_list)

# UI
print('--- ARTIST DB ---')
for artist in artists_list:
    print(artist['name'])
print('-----------------')
print('Select artist:')
artist_name = input('> ')
artist_name = artist_name.title()
print('-----------------')
print(artist_name)
print('*****************')

# Hämta ID för en specifik artist
for artist in artists_list:
    if artist_name == artist['name']:
        artist_id = artist['id']
        # print(artist_id)
        break


# Hämta info om en specifik artist
try:
    url = url + artist_id
except NameError:
    print('Artist saknas!')
    exit(1)

r = requests.get(url)
artist_info = r.json()
artist_info = artist_info['artist']

print('Genres:', ', '.join(artist_info['genres']))
print('Years active:', ', '.join(artist_info['years_active']))
print('Members:', ', '.join(artist_info['members']))
