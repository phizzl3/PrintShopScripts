"""
A simple script for numbering nUp tickets for the print shop.
"""


def numbering_main() -> None:
    """
    Gets numbering sequences for nUp ticket numbering.
    Gets the total number of tickets requested along with now many will fit on a 
    sheet (n_up) as well as the starting ticket number and prints the ticket 
    number groupings to the console.
    """
    print('[ Ticket Numbering Assist ]'.center(40))

    # Get ticket, sheet and numbering info
    total_requested = int(input('\n How many tickets do you need in total?: '))
    n_up = int(input(' How many tickets will fit on a sheet?: '))
    starting_number = int(input(' What number should we start with?: '))

    # Do math & round up if needed
    total_sheets = total_requested // n_up
    final_tickets = total_requested
    if total_requested % n_up > 0:
        total_sheets += 1
        final_tickets = total_sheets * n_up

    # Print totals to the console
    print('\n Final totals...')
    print(f' Total tickets Printed: {final_tickets}')
    print(f' Tickets per sheet: {n_up}')
    print(f' Total Sheets needed: {total_sheets}\n')
    print(' Here are your numbers...\n')

    # Get ending ticket number and set initial display number
    ending_number = starting_number + total_sheets - 1
    display_number = 1

    # Display to console
    for i in range(n_up):
        print(
            f' #{display_number:2}: Starting Number - {starting_number:4} | Ending Number - {ending_number:4}')
        starting_number = ending_number + 1
        ending_number = starting_number + total_sheets - 1
        display_number += 1

    input('\n Press ENTER to return...')


if __name__ == '__main__':
    numbering_main()
