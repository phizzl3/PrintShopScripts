"""
Calculates monthly Waste & VBS.
"""

import logfile
import email_to


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


def get_waste(data_set) -> None:
    """
    Get entries from user input and calculate totals.

    Args:
        data_set (dict): Totals for all calculated values
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


def get_credits(data_set) -> None:
    """
    Calculate VBS credit amounts.

    Args:
        data_set (dict): Totals for all calculated values
    """

    # Add credit totals to data set
    data_set['8210s BW Credit'] = data_set['8210s BW'] * .0019
    data_set['7100s BW Credit'] = data_set['7100s BW'] * .0095
    data_set['7100s Color Credit'] = data_set['7100s Color'] * .04

    return data_set


def display_totals(data_set) -> None:
    """
    Display totals to the console.

    Args:
        data_set (dict): Totals for all calculated values
    """
    # Display totals and credits (rounded to 4 decimal places)
    print('', '=' * 49)
    print(f" Total Black and White Waste:\t{data_set['Total BW']:5}")
    print(f" Total Color Waste:\t\t{data_set['Total Color']:5}")
    print('', '-' * 49)
    print(f" Total 8210s Waste: {data_set['8210s BW']:10}", end='\t')
    print(f"Credit: ${round(data_set['8210s BW Credit'], 4):7}")
    print(f" Total 7100s BW Waste: {data_set['7100s BW']:7}", end='\t')
    print(f"Credit: ${round(data_set['7100s BW Credit'], 4):7}")
    print(f" Total 7100s Color Waste: {data_set['7100s Color']:4}", end='\t')
    print(f"Credit: ${round(data_set['7100s Color Credit'], 4):7}")
    print('', '=' * 49)


def vbs_main() -> None:
    """
    Calculates monthly Waste and VBS.
    """
    print('[ VBS Calculator ]'.center(40))

    data_set = {}
    get_waste(data_set)
    get_credits(data_set)
    display_totals(data_set)
    logfile.write(data_set)
    email_to.print_emails()

    input('\n Press ENTER to return...')


if __name__ == '__main__':
    vbs_main()
