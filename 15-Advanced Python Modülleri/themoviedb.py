# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu api yi uygulamanızada kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi


import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "3adcf592521a355a6c8e811b82ea5101"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçim: ")

    if secim == '3':
        break
    else:
        if secim == '1':
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])

        if secim == '2':
            keyword = input('KeyWord: ')
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])
            
    