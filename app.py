from constants import PLAYERS
from constants import TEAMS
import random

# Placeholder for a variable I haven't defined yet, so the program still runs.
player_names = 'j'

# Gives the user the option between showing player stats or exiting the application
def first_menu_choice():
    choice_one = input("Please choose an option: ")
    if choice_one == 'a':
        second_menu_choice()
    else:
        print("Have a good day!")

def second_menu_choice():
    # Gives the user the choice between teams to show stats for
    dashes = '-' * 20
    print("\nChoose a team:\n(A) Panthers\n(B) Bandits\n(C) Warriors\n\n")
    second_choice = input("Please choose an option: ")
    
    # This will need to be formatted differently once I can properly populate the teams
    if second_choice.lower() == 'a':
        print("Team: Panthers\n", dashes, "\nTotal players: {}\nPlayers:\n{}\n".format(balance_teams(), player_names))
    elif second_choice.lower() == 'b':
        print("Team: Bandits\n", dashes, "\nTotal players: {}\nPlayers:\n{}\n".format(balance_teams(), player_names))
    elif second_choice.lower() == 'c':
        print("Team: Warriors\n", dashes, "\nTotal players: {}\nPlayers:\n{}\n".format(balance_teams(), player_names))

def clean_data():
    # Converts all the heights from constants.py into an ordered list of integers
    height_list = []
    player_height = [i['height'] for i in PLAYERS]
    for height in player_height:
        height_list.append(int(height[0:2]))
    
    # Converts all experience values from constants.py into an ordered list of boolean values
    experience_list = []
    player_experience = [i['experience'] for i in PLAYERS]
    for experience in player_experience:
        if experience == 'YES':
            experience_list.append(True)
        elif experience == 'NO':
            experience_list.append(False)
            
    # Saves all names in an ordered list
    player_names = [i['name'] for i in PLAYERS]
    
    # Saves all guardians in an ordered list
    player_guardians = [i['guardians'] for i in PLAYERS]

    # Creates a list of players
    # Index 0 is names, index 1 is their parents, index 2 is their experience, index 3 is their height
    player_list = [player_names, player_guardians, experience_list, height_list]
    return player_list

# Calculates the number of players each team should have
def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)
    return num_players_team
        
# Splits up the 18 players into the three teams, randomly
# 18 can't be a concrete number because the function should be set up so players can be added/removed
def adding_players_to_teams():
    panthers = []
    bandits = []
    warriors = []
    
    length_of_players = len(clean_data()[0])
    while len(panthers) != balance_teams():
        number = random.randint(0, length_of_players)
        panthers.append(clean_data()[0][number])
        del clean_data()[0][number]
        
adding_players_to_teams()
                            
                            

# Dunder main if-statement that isn't needed until the rest of my code runs correctly
        
#if __name__ == '__main__':
#    print('\nBASKETBALL TEAM STATS')
#    print('\n--MENU--\n')
#    print("Choices:\n(A): Display team stats\n(B): Quit")
#    balance_teams()
#    first_menu_choice()
#    clean_data()
#    print(clean_data())

    
    
    
    
    
    
    