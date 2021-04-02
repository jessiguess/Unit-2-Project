import constants
    # Use Dunder Main to ensure calculations, callable functions, and blocks of logic do not run    automatically
    # if __name__ == '__main__':
    
    
print('\nBASKETBALL TEAM STATS')
print('\n--MENU--')


def clean_data():
    # Reads player data from PLAYERS constant in constant.py
    # Clean data without changing constants
    # - Use data to iterate and read from to create new collection
    # Save data to a new collection (List? Tuple?)
    # Data to clean:
        # Height as an integer
        # Experience as a boolean value (True or False)
        # (Lists with nested dictionaries)

def balance_teams():
    # Teams (Panthers, Bandits, Warriors) should have an even number of players
    # num_players_team = len(PLAYERS) / len(TEAMS)

def main_menu_options():
    print("""
Your choices are:\n
  A) Display Team Stats
  B) Quit
  """)
    main_menu_choice = input("Enter an option:  ")
    if main_menu_choice.lower() == 'a':


main_menu_options()
