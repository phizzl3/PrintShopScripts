#!/usr/bin/env python3
"""
Uses monthly Mail Logs to calculate all Mail totals.
"""


def add_loop() -> int:
    """
    A simple addition loop, stops on '0' and returns the sum.

    Returns:
        int: Sum of all entries.
    """
    total = []
    print(' Enter "0" when done...')
    while not total or total[-1]:
        total.append(int(input(' Add: ')))

    return sum(total)


def compile_info(mail_info) -> None:
    """
    Compiles info for display or use.

    Args:
        mail_info (dict): Dictionary containing materials and totals.
    """    
    # get postage usage totals
    print('\n *Postage Usage*')
    meter_start = float(input("\n Enter the BEGINNING METER BALANCE: "))

    print(' Enter each POSTAGE ADDED amount.')
    postage_added = add_loop()

    meter_end = float(
        input(' Enter the ENDING METER BALANCE for the Month: '))

    # Get mail_info totals
    print('\n *Mail Volumes*')
    for item in mail_info:
        print(f'\n Enter each day\'s total from the {item} column.')
        mail_info[item] = add_loop()

    # Add postage usage to dictionary
    mail_info['Cost of Outbound Mail'] = meter_start + postage_added - meter_end
   

def display_info(mail_info) -> None:
    """
    Display compiled info to the console.

    Args:
        mail_info (dict): Dictionary containing materials and totals.
    """
    print('=' * 42)
    # loop through the list/values
    for item in mail_info:
        print(f' {item:25} = {mail_info[item]:8}')
    print('=' * 42)

    # Keep console open
    input('\n Press ENTER to return...')


def mail_main(disp=True) -> dict:
    """
    Uses monthly Mail Logs to calculate all Mail totals for the MOR.

    Uses the columns from the completed monthly Mail Logs to calculate 
    the totals for the MOR.

    Args: disp (bool, optional) True or False value to determine if 
                the title info should display.
    """
    if disp:
        print('[ Mail Logs Calculator ]'.center(40))

    # Set initial values for dict items
    mail_info = {
        'Outbound Mail': 0,
        'Inbound Mail': 0,
        'Returned Mail': 0,
        'Outbound Accountable Mail': 0,
        'Inbound Accountable Mail': 0
    }

    # Get the totals via user input
    compile_info(mail_info)

    if disp:
        # display the totals to the console
        display_info(mail_info)

    return mail_info


if __name__ == "__main__":
    mail_main(disp=True)
