"""
A basic script for getting subset groupings for the print shop.

Modules:
- subset_main: Short description of module1

Sample Usage:
- from subset_finishing import subset_main
"""


def subset_main():
    """
    Outputs a list of set groupings for subset finishing in the print shop.

    Gets the total number of pages for the project as well as how many pages
    should be in each subset and then outputs each subset grouping to the console.

    Sample Usage:
    - subset_main()
    """
    # Display title
    print('[ Subset Finishing Assist ]'.center(40))

    # Get total pages and number of pages per subset
    pages = int(input('\n How many total pages?: '))
    subset = int(input(' How many per subset?: '))

    # Set initial counters
    set_number = 1
    page_counter = 1

    # Loop through groups and display to console
    while page_counter <= pages:
        print(f' Set {set_number}: {page_counter} - {page_counter + subset - 1}')
        page_counter += subset
        set_number += 1

    # Pause to keep console open
    input('\n Press ENTER to close and return...')


if __name__ == "__main__":
    subset_main()
