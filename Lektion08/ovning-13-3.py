import requests


# Definiera en funktion för att hämta data från API:et
def get_artists_data():
    """Hämtar data från artister-API:et.

    Returns:
        En lista med artister.
    """

    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    r = requests.get(url)
    artists = r.json()

    return artists['artists']


# Definiera en funktion för att skriva ut en lista med artister
def print_artists_list(artists):
    """Skriver ut en lista med artister.

    Args:
        artists: En lista med artister.
    """

    print('--- ARTIST DB ---')
    for artist in artists:
        print(artist['name'])
    print('-----------------')


# Definiera en funktion för att få ID för en specifik artist
def get_artist_id(artists, artist_name):
    """Hämtar ID för en specifik artist.

    Args:
        artists: En lista med artister.
        artist_name: Namnet på artisten vars ID ska hämtas.

    Returns:
        ID för den specifika artisten.
    """

    for artist in artists:
        if artist_name == artist['name']:
            return artist['id']

    raise ValueError('Artisten saknas!')


# Definiera en funktion för att hämta information om en specifik artist
def get_artist_info(artist_id):
    """Hämtar information om en specifik artist.

    Args:
        artist_id: ID för artisten vars information ska hämtas.

    Returns:
        En dictionary med information om artisten.
    """

    url = F"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    r = requests.get(url)
    artist_info = r.json()

    return artist_info['artist']


# Hämta data om artister
artists = get_artists_data()

# Skriv ut en lista med artister
print_artists_list(artists)

# Fråga användaren vilken artist de vill ha information om
artist_name = input('Select artist: ')
artist_name = artist_name.title()

# Hämta ID för den specifika artisten
try:
    artist_id = get_artist_id(artists, artist_name)
except ValueError as e:
    print(e)
    exit(1)

# Hämta information om den specifika artisten
artist_info = get_artist_info(artist_id)

# Skriv ut information om artisten
print('Genres:', ', '.join(artist_info['genres']))
print('Years active:', ', '.join(artist_info['years_active']))
print('Members:', ', '.join(artist_info['members']))
