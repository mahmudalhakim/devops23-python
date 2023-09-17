# Övnings 13.3
import requests

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

# Hämta en lista på artister
r = requests.get(url)
artists = r.json()

# Visa UI
print("--- ARTIST DB ---")
for artist in artists['artists']:
    print(artist['name'])
print("-----------------")

print("Select artist:")
artist_name = input("> ")
print("-----------------")

# Sök efter artisten i listan

for artist in artists['artists']:
    if artist_name == artist['name']:
        print(artist['name'])
        print('****************')

        # Hämta info om artisten
        artist_id = artist['id']
        r = requests.get(url + artist_id)
        artist_info = r.json()
        artist_info = artist_info['artist']

        print("Genres:", ', '.join(artist_info['genres']))
        print("Years active:", ', '.join(artist_info['years_active']))
        print("Members:", ', '.join(artist_info['members']))
        print("-----------------")
        break
else:
    print(f"{artist_name} is not in database")
