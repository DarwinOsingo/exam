# Problem: Get Winner
# Given a year and a competition name, 
# return the name of the team that won the most matches in that
# competition that year. A win is when a team scores more goals than the other team.
#https://jsonmock.hackerrank.com/api/football_competitions?year={year}&name={competition}&page={page}
{
    "page": 1,
    "total_pages": 3,
    "data": [
        {
            "home_team": "Barcelona",
            "away_team": "Real Madrid",
            "home_team_goals": 3,
            "away_team_goals": 1
        },
        {
            "home_team": "Arsenal",
            "away_team": "Chelsea",
            "home_team_goals": 0,
            "away_team_goals": 2
        }
    ]
}
import requests

def getWinner(year, competition):
   url = f"https://jsonmock.hackerrank.com/api/football_competitions?year={year}&name={competition}&page={page}"
   response = requests.get(url).json()
   total_pages = response['total_pages']
   winner = {}
   for pages in range(1,total_pages+1):
       answer = requests.get(url).json()
       data = answer['data']
       for match in data:
           
           if match['home_team_goals']> match['away_team_goals']:
               team_name = match['home_team']
           elif match['away_team_goals'] >match['home_team_goals']:
               
               team_name=match['away_team']
           else:
               continue 
           winner[team_name]=winner.get(team_name,0)+1
   return max(winner,key=winner.get)

            
                        
             
               
        
       
  
   

    


if __name__ == '__main__':
    year = int(input())
    competition = input()
    result = getWinner(year, competition)
    print(result)