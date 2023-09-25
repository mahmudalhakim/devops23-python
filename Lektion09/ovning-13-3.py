import requests


class Artist:
    """En klass för att representera en artist."""

    def __init__(self, name, id, genres, years_active, members):
        """Initierar en artist.

        Args:
            name: Namnet på artisten.
            id: ID för artisten.
            genres: Genrer som artisten spelar.
            years_active: År som artisten varit aktiv.
            members: Medlemmar i bandet.
        """

        self.name = name
        self.id = id
        self.genres = genres
        self.years_active = years_active
        self.members = members

    def __str__(self):
        """Returnerar en strängrepresentation av artisten."""
        return f"Artist(name={self.name}, id={self.id}, genres={self.genres}, years_active={self.years_active}, members={self.members})"


class ArtistRepository:
    """En klass för att hantera artister."""

    def __init__(self):
        """Initierar en artistrepo.

        Args:
            None.
        """

        self.artists = []

    def get_artists(self):
        """Hämtar alla artister.

        Returns:
            En lista med artister.
        """

        return self.artists

    def add_artist(self, artist):
        """Lägger till en artist.

        Args:
            artist: Den artist som ska läggas till.
        """

        self.artists.append(artist)

    def find_artist(self, name):
        """Hittar en artist.

        Args:
            name: Namnet på artisten som ska hittas.

        Returns:
            Artisten, om den finns.
        """

        for artist in self.artists:
            if artist.name == name:
                return artist

        raise ValueError(f"Artisten {name} finns inte.")


# Hämta data från API:et
def get_artists_data():
    """Hämtar data från artister-API:et.

    Returns:
        En lista med artister.
    """

    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    r = requests.get(url)
    artists = r.json()

    artists_list = []
    for artist in artists['artists']:
        artist_id = artist['id']
        artist = get_artist_info(artist_id)
        artists_list.append(
            Artist(artist['name'], artist_id, artist['genres'], artist['years_active'], artist['members']))

    return artists_list


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



# Huvudprogram
def main():
    """Huvudprogrammet."""

    # Hämta data om artister
    artists = get_artists_data()

    # Skapa en artistrepo
    repo = ArtistRepository()

    # Lägg till artisterna i repon
    for artist in artists:
        print(artist.name)
        repo.add_artist(artist)

    # Fråga användaren vilken artist de vill ha information om
    artist_name = input('Select artist: ')
    artist_name = artist_name.title()

    # Hitta den specifika artisten
    artist = repo.find_artist(artist_name)

    # Skriv ut information om artisten
    print('Genres:', ', '.join(artist.genres))
    print('Years active:', ', '.join(artist.years_active))
    print('Members:', ', '.join(artist.members))


if __name__ == '__main__':
    while True:
        main()
