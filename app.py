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


# Displays the greeting and the first two options in the main menu
def first_menu_choice():
    print('\nBASKETBALL TEAM STATS')
    print('\n--MENU--\n')
    print("Choices:\n(1): Display team stats\n(2): Quit")
    while True:
        try:
            choice_one = int(input("Please choose an option: "))
            if choice_one > 2:
                raise ValueError()
            if choice_one < 1:
                raise ValueError()
        except ValueError:
            print("\nPlease enter the number 1 or 2.")
        else:
            if choice_one == 1:
                second_menu_choice()
                # Exits program once declining the restart option
                print("Have a nice day!")
                break
            else:
                print("Have a good day!")
                break
            

# Gives the user the choice between teams to show stats for
def second_menu_choice():
    
    print("\nTeams:\n(1) Panthers\n(2) Bandits\n(3) Warriors\n")
    while True:
        try:
            second_choice = int(input("Please choose an option: "))
            if second_choice < 1:
                raise ValueError
            elif second_choice > 3:
                raise ValueError
        except ValueError:
            print("\nPlease choose a number 1, 2 or 3.")
        else:
            dashes = '-' * 20
        
            if second_choice == 1:
                print("\nTeam: Panthers\n", dashes, "\nTotal players: {}\n".format(number_of_players), "\nPlayers:")
                print(*panther_names, sep = ", ")
                restart_program()
                break
                
            elif second_choice == 2:
                print("\nTeam: Bandits\n", dashes, "\nTotal players: {}\n".format(number_of_players), "\nPlayers:")
                print(*bandit_names, sep = ", ")
                restart_program()
                break
                
            elif second_choice == 3:
                print("\nTeam: Warriors\n", dashes, "\nTotal players: {}\n".format(number_of_players), "\nPlayers:")
                print(*warrior_names, sep = ", ")
                restart_program()
                break

                
# Prompts the user if they would like to return to the main menu or exit the program
def restart_program():
    while True:
        try:
            restart = int(input("\n(1) Main Menu \n(2) Exit \nPlease choose an option: "))
            if restart < 1:
                raise ValueError
            elif restart > 2:
                raise ValueError
        except ValueError:
            print("\nPlease enter the number 1 or 2.")
        else:
            if restart == 1:
                first_menu_choice()
            elif restart == 2:
                break


while __name__ == '__main__':
    
    number_of_players = int(balance_teams())
    panthers, bandits, warriors = teams_unpacker()
    panther_names = [i['name'] for i in panthers]
    bandit_names = [i['name'] for i in bandits]
    warrior_names = [i['name'] for i in warriors]
    first_menu_choice()
    break
    
    
    
    




