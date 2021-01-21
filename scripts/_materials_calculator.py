"""
Uses a single set to calculate copy/paper/finishing totals. 
    
Gets user inputs for number of Sets, Sheets, Color Copies, 
Black and White Copies, and Finishing for a set and uses that 
information along with the number of sets to calculate the 
total amount of materials for a given project.

Modules:
- materials_main: Main - Calls the functions for calcuation, etc

Sample Usage:
- from materials_calculator import materials_main
"""


from disp.asciiart import display_art


def materials_main():
    """
    Uses a single set to calculate copy/paper/finishing totals. 

    Gets user inputs for number of Sets, Sheets, Color Copies, 
    Black and White Copies, and Finishing for a set and uses that 
    information along with the number of sets to calculate the 
    total amount of materials for a given project.

    Sample Usage:
    - materials_main()
    """
    
    # Display ASCII art
    display_art()
    
    # display title
    print('[ Materials Per Set Calculator ]'.center(40))
    print('Uses a single set to calculate total'.center(40))
    print('Color, BW, Staple and Sheet counts'.center(40))
    print('=' * 40, '\n')
    # set initial values and dictionary for totals
    sets = 0
    totals = {
        'Sheets': 0,
        'Staples': 0,
        'Color': 0,
        'B/W': 0
    }

    # loop to get/calculate/display info
    loop = True
    while loop:
        # ask for user input of materials and assign new variables
        sets2, totals2 = get_info(sets, **totals)
        # multiply the inputs (new variables) by the sets and set new values
        sets2, totals2 = multiply(sets2, **totals2)
        # add new sets to current sets (original variables)
        sets += sets2

        # loop through the original dictionary and add new amounts to totals
        for item in totals.keys():
            totals[item] += totals2[item]

        # display current totals to console
        display(sets, **totals)

        # check for loop continuation
        loop = loop_choice()


def display(sets, **totals):
    """
    Prints Sets and Totals to the console.

    Gets the above variables and loops through them to display them
    to the console window.

    Parameters:
    - sets (int): Number of sets for the current group of materials
    - **totals (dict): Unpacked dictionary of the totals for each 
    set of materials. Ex: {Paper: 20, Color: 40}

    Sample Usage:
    - display(sets, **totals)
    """

    # Display ASCII art
    display_art()

    # header/title display for totals
    print('-' * 26)
    print('|', '   *Running Totals*   ', '|')
    print(f'| Total Sets: {sets}'.ljust(24), '|')

    # loop through the dictionary of totals and display them to console
    for item, total in totals.items():
        print(f'| Total {item}: {total}'.ljust(24), '|')
    print('-' * 26)


def get_info(sets, **totals):
    """
    Gets use input and adds values to the totals dictionary.

    Loops through the items in the totals dictionary and asks for 
    user input for each amount and adds replaces that item's amount
    in the dictionary. 

    Parameters:
    - sets (int): Number of sets for the current group of materials
    - **totals (dict): Unpacked dictionary of the totals for each 
    set of materials. Ex: {Paper: 20, Color: 40}

    Returns:
    - (int): sets - The number of sets for the current group
    - (dict): totals - The material: amount dictionary for the current group

    Sample Usage:
    - sets2, totals2 = get_info(sets, **totals)
    """

    # get user input for each item in 'totals' dictionary
    sets = int(input('\nHow many Sets?: '))

    # loop through and replace the values in the dictionary passed
    # assign to a different variable by calling function on return
    for item in totals.keys():
        totals[item] = int(input(f'How many {item} per set?: '))
    return sets, totals


def multiply(sets, **totals2):
    """
    Multiplies totals2 dictionary's values by the number of sets.

    Loops through the values in the totals2 dictionary and multiplies 
    each value by the number of sets for the group. Replaces the value 
    in the totals2 dictionary for the given item and returns the new set 
    of values. 

    Parameters:
    - sets (int): Number of sets for the current group of materials
    - **totals2 (dict): Unpacked dictionary of the modified totals for 
    each set of materials. Ex: {Paper: 20, Color: 40}

    Returns:
    - (int): sets - The number of sets for the current group
    - (dict): totals - The material: amount dictionary for the current group

    Sample Usage:
    - sets2, totals2 = multiply(sets2, **totals2)
    """

    # loop through the totals and multiply the values by the sets and return
    for item, total in totals2.items():
        totals2[item] = total * sets
    return sets, totals2


def loop_choice():
    """
    Displays a message to validate looping continuation.

    Asks if user wants to continue and sets a boolean value
    based on user input. 

    Returns:
    - (bool): True/False based on input

    Sample Usage:
    - loop = loop_choice()
    """

    # ask user if they'd like to continue and get input
    print('\nContinue adding to these totals?')
    user_choice = input('ENTER to continue or "0" to end and return: ')

    # set and return boolean based on user input
    if user_choice == '0':
        return False
    else:
        return True
