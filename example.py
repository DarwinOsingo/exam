{
    "page": 1,
    "total_pages": 3,
    "data": [
        {
            "Title": "The Dark Knight",
            "Year": 2008,
            "imdbID": "tt0468569"
        },
        {
            "Title": "Iron Man",
            "Year": 2008,
            "imdbID": "tt0371746"
        }
    ]
}
import requests

def getMoviesByYear(year):
    URL = F"https://jsonmock.hackerrank.com/api/movies?Year={year}&page={page}"
    response= requests.get(URL).json()
    total_pages=int(response['total_pages'])+1
    movies = []
    for page in range(1,total_pages):
        info = requests.get(F"https://jsonmock.hackerrank.com/api/movies?Year={year}&page={page}").json()
        release = info['data']
        for movie in release:
            if year == movie['Year']:
                 movies.append( movie['Title'])
    return sorted(movies)
            


            




if __name__ == '__main__':
    year = int(input())
    result = getMoviesByYear(year)
    for title in result:
        print(title)