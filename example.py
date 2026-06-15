{
    "page": 1,
    "total_pages": 2,
    "data": [
        {
            "team1": "Barcelona",
            "team2": "Real Madrid",
            "team1goals": "3",
            "team2goals": "1"
        }
    ]
}
import requests

def getTotalGoals(team, year):
    total_goals= 0
    URL = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1"
    response = requests.get(URL).json()
    total_pages = response['total_pages']
    for page in range (1,total_pages+1):
        info = response['data']
        for match in info:
            total_goals += int(match['team1goals'])
    URL1 = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
    




   
        
    



    
    pass


if __name__ == '__main__':
    team = input()
    year = int(input())
    result = getTotalGoals(team, year)
    print(result)