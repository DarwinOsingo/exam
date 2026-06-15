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

    URL = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
    URL1 = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
    response_team1 = requests.get(URL).json
    total_pages = response_team1['total_pages']
    for pages in range(1,total_pages+1):
        data = response_team1['data']
        team1= data['team1']
        team1goals= data['team1goals']
        return team1
    response_team2 = requests.get(URL1).json
    for pages in range(1,total_pages+1):
        data = response_team2['data']
        team2= data['team2']
        team2goals = data['team2goals']

        return team2
    return team1,team2

    
        
    


    response_team2 = requests.get(URL1).json

    
    pass


if __name__ == '__main__':
    team = input()
    year = int(input())
    result = getTotalGoals(team, year)
    print(result)