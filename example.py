#Given a movie title, return its imdbRating. If the movie is not found return -1.
# Input:  title = "Inception"
# Output: 8.8

# Input:  title = "xyzabc"
# Output: -1
{
    "page": 1,
    "total_pages": 1,
    "total": 1,
    "data": [
        {
            "Title": "Inception",
            "Year": 2010,
            "imdbID": "tt1375666",
            "imdbRating": 8.8
        }
    ]
}
import requests

def getMovieRating(title):
   

    url=f"https://jsonmock.hackerrank.com/api/movies/search?Title={title}&page={1}"
    library = requests.get(url).json
    data = library['data']
    for key in data:
        if title == key['Title']:
            return key['imdbRating']
    
    return -1
   
 
    pass


if __name__ == '__main__':
    title = input()
    result = getMovieRating(title)
    print(result)