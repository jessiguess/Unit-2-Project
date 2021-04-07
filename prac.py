from constants import PLAYERS
from constants import TEAMS
import random

master_list = PLAYERS.copy()


def clean_data():
    # Converts all the heights into integers
    # Converts all the experience values to boolean values
    # Saves them to the master_list dictionary
    index = 0
    for item in master_list:
        if master_list[index]['experience'] == 'YES':
            master_list[index]['experience'] = True
        else:
            master_list[index]['experience'] = False
        # WHERE I'M GETTING ERROR
        master_list[index]['height'] = int(master_list[index]['height'][0:2])
        
        index += 1
    
    return master_list


# Calculates the number of players each team should have
def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)
    return num_players_team
        

# Splits up the 18 players into the three teams, randomly
def adding_players_to_teams(team):
    team = []
    while len(team) != balance_teams():
        number = random.randint(0, len(clean_data()) - 1)
        team.append(clean_data()[number])
        del clean_data()[number]
    return team
        
panthers = adding_players_to_teams('panthers')
print(panthers)




