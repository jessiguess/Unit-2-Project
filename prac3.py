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
        master_list[index]['guardians'] = guardians.split("and ")
        
        index += 1
        
    # Saves them to the master_list dictionary
    return master_list
  

# Returns the number of players each team should have
def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)
    return num_players_team
        

# Splits up the players evenly into the teams, randomly
# Returns the populated teams
def teams_unpacker():
    panthers = []
    bandits = []
    clean_data()
    
    while len(panthers) != number_of_players:
        number = random.randint(0, len(master_list) - 1)
        panthers.append(master_list[number])
        del master_list[number]
        
    while len(bandits) != number_of_players:
        number = random.randint(0, len(master_list) - 1)
        bandits.append(master_list[number])
        del master_list[number]
        
    warriors = master_list
    return (panthers, bandits, warriors)


# Calculates the average height for a team
def team_heights(team_name):
    height = [i['height'] for i in team_name]
    total = 0
    for ele in range(0, len(height)):
        total = total + height[ele] 
    average_height = total / number_of_players
    return int(average_height)


def team_stats(team, team_name, team_names, team_guardians):
    dashes = '-' * 12
    print("\nTeam: {}\n".format(team), dashes, "\nTotal players: {}".format(number_of_players))
    print("Average height:{}\n".format(team_heights(team_name)))
    print("Players:")
    print(*team_names, sep = ", ")
    print("\nGuardians:")
    index = 0
    for item in team_guardians:
        print(*team_guardians[index], sep = ", ")
        index += 1
        

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
            
    break
        
        
        