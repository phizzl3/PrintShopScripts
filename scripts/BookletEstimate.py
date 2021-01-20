"""
Quickly estimate book materials based on individual page count.
"""


class Book():
    """
    Quickly estimate book materials based on individual page count.
    """

    def __init__(self):

        # Get individual page count
        self.pages = int(input(
            "\n How many 8.5x11\" pages (including blanks) are in the original document?: "))

        # Calculate number of sheets and clicks per book
        self.sheets = self.pages / 4

        # Make sure pages is a multiple of 4 or round sheets up
        if self.pages % 4 != 0:
            self.sheets = int(self.sheets) + 1

        self.clicks = self.sheets * 2

        # Get total books needed
        self.number = int(input("\n How many books do you need in total?: "))

        # Get the total number of sheets and clicks for all books
        self.total_sheets = self.sheets * self.number
        self.total_clicks = self.clicks * self.number

    def display_totals(self):

        # Display totals to console
        print(f"\n Total Books (Finishing): {self.number}")
        print(f" Total 11x17\" Sheets: {int(self.total_sheets)}")
        print(f" Total Clicks: {int(self.total_clicks)}")

        input('\n ENTER to close and return...')


def get_book_materials():

    b1 = Book()
    b1.display_totals()


if __name__ == "__main__":
    get_book_materials()
