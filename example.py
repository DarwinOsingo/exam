{
    "page": 1,
    "total_pages": 10,
    "data": [
        {
            "team1": "Barcelona",
            "team2": "Real Madrid",
            "team1goals": "1",
            "team2goals": "1"
        },
        {
            "team1": "Arsenal",
            "team2": "Chelsea",
            "team1goals": "2",
            "team2goals": "0"
        }
    ]
}
import requests

def getDrawnMatches(year):
    count = 0
    url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
    response= requests.get(url).json()
    total_pages = response['total_pages']
   
    for pages in range(1,total_pages+1):
        info = response['data']
        for matches in info:
            if int(matches['team1goals'])==int(matches['team2goals']):
                count += 1
    return count 
            
    


if __name__ == '__main__':
    year = int(input())
    result = getDrawnMatches(year)
    print(result)