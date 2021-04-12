from constants import PLAYERS
from constants import TEAMS
import random
master_list = PLAYERS.copy()


def clean_data():
    index = 0
    
    # Converts all the experience values to boolean values
    for item in master_list:
        if master_list[index]['experience'] == 'YES':
            master_list[index]['experience'] = True
        else:
            master_list[index]['experience'] = False
            
        # Converts all the heights into integers
        master_list[index]['height'] = int(master_list[index]['height'][0:2])
        
        # Changes the guardian values of more than 1 parent into a list of both parents separated by a comma
        guardians = master_list[index]['guardians']
        master_list[index]['guardians'] = guardians.split(" and ")
        
        index += 1
        
    # Saves them to the master_list dictionary
    return master_list
  

# Returns the number of players each team should have
def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)
    return num_players_team
        

# Creates 2 new lists, one for experienced players and the other for inexperienced players
# Assigns 3 random experienced players and 3 random inexperienced players to each team
# Returns the new team lists
def teams_unpacker():
    clean_data()
    
    panthers = []
    bandits = []
    
    experienced_players = [] 
    inexperienced_players = []
    
    half_team = int(number_of_players / 2)
    
    index = 0
    for player in master_list:
        if master_list[index]['experience'] == True:
            experienced_players.append(player)
        elif master_list[index]['experience'] == False:
            inexperienced_players.append(player)
        index += 1

    while len(panthers) != half_team:
        number = random.randint(0, len(experienced_players) - 1)
        panthers.append(experienced_players[number])
        del experienced_players[number]
    while len(panthers) != number_of_players:
        number = random.randint(0, len(inexperienced_players) - 1)
        panthers.append(inexperienced_players[number])
        del inexperienced_players[number]
    
    while len(bandits) != half_team:
        number = random.randint(0, len(experienced_players) - 1)
        bandits.append(experienced_players[number])
        del experienced_players[number]
    while len(bandits) != number_of_players:
        number = random.randint(0, len(inexperienced_players) - 1)
        bandits.append(inexperienced_players[number])
        del inexperienced_players[number]
        
    warriors = experienced_players + inexperienced_players
    
    return (panthers, bandits, warriors)


# Calculates the average height for each team
def team_heights(team_name):
    height = [i['height'] for i in team_name]
    total = 0
    for ele in range(0, len(height)):
        total = total + height[ele] 
    average_height = total / number_of_players
    return int(average_height)


# Formats what stats print when a team is selected
# Team name, number of players, number of inexperienced and experienced, names of all players, names of all player guardians
def team_stats(team, team_name, team_names, team_guardians):
    dashes = '-' * 12
    print("\nTeam: {}\n".format(team), dashes, "\nTotal players: {}".format(number_of_players))
    print("Total experienced: {}".format(int(number_of_players / 2)))
    print("Total inexperienced: {}".format(int(number_of_players / 2)))
    print("Average height: {}\n".format(team_heights(team_name)))
    print("Players:")
    print(*team_names, sep = ", ")
    
    print("\nGuardians:")
    index = 0
    team_guardians_list = []
    for item in team_guardians:
        if len(team_guardians[index]) == 2:
            team_guardians_list.append(team_guardians[index][0])
            team_guardians_list.append(team_guardians[index][1])
        else:
            team_guardians_list.append(team_guardians[index][0])
        index += 1
    print(*team_guardians_list, sep = ", ")
        
# Lets the user decide between showing stats and quitting, while catching errors
def first_menu():
    while True:
        try:
            first_menu_choice = int(input(">>> "))
            if first_menu_choice > 2 or first_menu_choice < 1:
                raise ValueError()
        except ValueError:
            print("Please choose the number 1 or 2.")
        else:
            return first_menu_choice
            break
        
        
# Lets the user choose which team to show stats for, while catching errors
def second_menu():
    while True:
        try:
            second_menu_choice = int(input(">>> "))
            if second_menu_choice > 3 or second_menu_choice < 1:
                raise ValueError()
        except ValueError:
            print("Please choose the number 1, 2 or 3.")
        else:
            return second_menu_choice
            break
        
# Allows the user to restart the tool, if desired, while catching errors
def restart_program():
    while True:
        try:
            restart = int(input("\n(1) Return to Main Menu \n(2) Exit \nPlease choose an option: "))
            if restart > 2 or restart < 1:
                raise ValueError
        except ValueError:
            print("\nPlease choose the number 1 or 2.")
        else:
            return restart
            break
        
        
while __name__ == '__main__':
    dashes = '-' * 41
    number_of_players = int(balance_teams())
    panthers, bandits, warriors = teams_unpacker()
    
    panther_names = [i['name'] for i in panthers]
    bandit_names = [i['name'] for i in bandits]
    warrior_names = [i['name'] for i in warriors]
    
    panther_guardians = [i['guardians'] for i in panthers]
    bandit_guardians = [i['guardians'] for i in bandits]
    warrior_guardians = [i['guardians'] for i in warriors]
    
    while True:
        print("\n***Welcome to the Basketball Stats Tool!***\n", dashes, "\n\nPlease choose an option below:\n\n(1) Display Team Stats\n(2) Quit\n")
        
        first_menu_choice = first_menu()
        if first_menu_choice == 1:
            pass
        elif first_menu_choice == 2:
            print("Have a good day!")
            break
        
        print("\nTeams:\n\n(1) Panthers\n(2) Bandits\n(3) Warriors\n")
        second_menu_choice = second_menu()
        if second_menu_choice == 1:
            team_stats('Panthers', panthers, panther_names, panther_guardians)
        elif second_menu_choice == 2:
            team_stats('Bandits', bandits, bandit_names, bandit_guardians)
        elif second_menu_choice == 3:
            team_stats('Warriors', warriors, warrior_names, warrior_guardians)
            
        restart = restart_program()
        if restart == 1:
            pass
        elif restart == 2:
            print("Have a good day!")
            break
    # End program
    break