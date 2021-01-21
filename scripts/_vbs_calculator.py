"""
Calculates monthly machine waste and VBS credits.
Uses information from each machines waste log entries and the corresponding 
click rates for the equipment to calculate the total black and white and 
color waste for the month as well as the credit amounts for the Variable 
Billing System.
"""


import colorama
from disp.asciiart import display_art

from calcs.add import add_loop

# Initialize colorama and set it to auto reset the colors
colorama.init(autoreset=True)

CYAN = colorama.Fore.LIGHTCYAN_EX
MAGENTA = colorama.Fore.LIGHTMAGENTA_EX


def display_title():
    """
    Display ASCII art and title
    """

    display_art()
    print('[ VBS Calculator ]'.center(49))
    print('Uses waste logs to calculate total'.center(49))
    print('BW/Color Waste, and Credits for VBS'.center(49))
    print('', '=' * 49, '\n')


def get_waste(data_set):
    """
    Get entries from user input and calculate totals.

    Args:
        data_set (dict): Totals for all calculated values

    Returns:
        dict: Totals for all calculated values
    """

    print('\n Enter each line for all Pro 8210s Waste.')
    data_set['8210s BW'] = add_loop()
    print('\n Enter each line for all Pro 7100s Black & White Waste.')
    data_set['7100s BW'] = add_loop()
    print('\n Enter each line for all Pro 7100s Color Waste.')
    data_set['7100s Color'] = add_loop()

    # Calculate total waste and add to data set
    data_set['Total BW'] = data_set['8210s BW'] + data_set['7100s BW']
    data_set['Total Color'] = data_set['7100s Color']

    return data_set


def get_credits(data_set):
    """
    Calculate VBS credit amounts.

    Args:
        data_set (dict): Totals for all calculated values

    Returns:
        dict: Totals for all calculated values
    """

    # Add credit totals to data set
    data_set['8210s BW Credit'] = data_set['8210s BW'] * .0019
    data_set['7100s BW Credit'] = data_set['7100s BW'] * .0095
    data_set['7100s Color Credit'] = data_set['7100s Color'] * .04

    return data_set


def display_totals(data_set):
    """
    Display totals to the console.

    Args:
        data_set (dict): Totals for all calculated values
    """

    # display totals and credits (rounded to 4 decimal places)
    display_art()
    print('', '=' * 49)
    print(f"{CYAN} Total Black and White Waste:\t{data_set['Total BW']:5}")
    print(f"{CYAN} Total Color Waste:\t\t{data_set['Total Color']:5}")
    print('', '-' * 49)
    print(f"{MAGENTA} Total 8210s Waste: {data_set['8210s BW']:10}", end='\t')
    print(f"Credit: ${round(data_set['8210s BW Credit'], 4):7}")
    print(f"{MAGENTA} Total 7100s BW Waste: {data_set['7100s BW']:7}", end='\t')
    print(f"Credit: ${round(data_set['7100s BW Credit'], 4):7}")
    print(f"{MAGENTA} Total 7100s Color Waste: {data_set['7100s Color']:4}", end='\t')
    print(f"Credit: ${round(data_set['7100s Color Credit'], 4):7}")
    print('', '=' * 49)


def vbs_main():
    """
    Calculates monthly machine waste and VBS credits.
    Uses information from each machines waste log entries and the corresponding 
    click rates for the equipment to calculate the total black and white and 
    color waste for the month as well as the credit amounts for the Variable 
    Billing System.
    """

    data_set = {}

    display_title()
    data_set = get_waste(data_set)
    data_set = get_credits(data_set)
    display_totals(data_set)

    # keep console open
    input('\n Press ENTER to return...')
