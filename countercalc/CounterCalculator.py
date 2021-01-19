#!/usr/bin/env python3
"""
Uses counter sheets to calculate clicks and sheets for production equipment.
Takes the starting counters and ending counters from the counter sheets printed 
by the machines and uses that to calculate the total numbers of color and black 
and white copies along with the number of sheets used. 
"""

from menuloop import display_menu


class Counter:

    disp = (
        ' Enter starting COLOR counter: ',
        ' Enter starting BLACK & WHITE counter: ',
        ' Enter ending COLOR counter: ',
        ' Enter ending BLACK & WHITE counter: '
    )

    def __init__(self, counter_type) -> None:

        self.counter_type = counter_type
        self.sheets = 0

        if self.counter_type == 'color' or self.counter_type == 'both':
            self.color_clr = 0
            self.color_bw = 0

        if self.counter_type == 'bw' or self.counter_type == 'both':
            self.bw = 0

    def type_choice(self):

        if self.counter_type == 'color':
            self.calculate_color()
        elif self.counter_type == 'bw':
            self.calculate_bw()
        else:
            self.calculate_color().calculate_bw()

    def calculate_color(self):

        while True:
            print('\n Pro C7100s Counters:')
            color_start = int(input(Counter.disp[0]))
            bw_start = int(input(Counter.disp[1]))
            color_end = int(input(Counter.disp[2]))
            bw_end = int(input(Counter.disp[3]))

            self.color_clr += abs(color_end - color_start)
            self.color_bw += abs(bw_end - bw_start)

            total = abs(color_end - color_start) + abs(bw_end - bw_start)

            self.calculate_sheets(total).display_totals()

            choice = input(
                ' Add more COLOR counters? (ENTER to add, 0 to Exit): ')
            if choice == '0':
                return self

    def calculate_bw(self):

        while True:
            print('\n Pro 8210s Counters:')
            bw_start = int(input(Counter.disp[1]))
            bw_end = int(input(Counter.disp[3]))

            self.bw += abs(bw_end - bw_start)

            total = abs(bw_end - bw_start)

            self.calculate_sheets(total).display_totals()

            choice = input(
                ' Add more BLACK & WHITE counters? (ENTER to add, 0 to Exit): ')
            if choice == '0':
                return self

    def calculate_sheets(self, total):

        while True:
            choice = input(' Printed 1-Sided or 2-Sided?: ')

            if choice in ('1', '2'):
                if choice == '1':
                    self.sheets += total
                else:
                    self.sheets += total/2
                return self
            print(' Try again. (Enter 1 or 2)')

    def display_totals(self):

        print('\n Totals:')
        if self.counter_type == 'color' or self.counter_type == 'both':
            print(f' Total 7100 Color: {self.color_clr}')
            print(f' Total 7100 Black & White: {self.color_bw}')

        if self.counter_type == 'bw' or self.counter_type == 'both':
            print(f' Total 8210 Black & White: {self.bw}')

        print(f' Total Sheets: {self.sheets}\n')


def main():

    print('\n Which type of counters do you have?')

    display_menu(
        ('Color', Counter('color')),
        ('Black & White', Counter('bw')),
        ('Both', Counter('both')
         )).type_choice()

    pass


if __name__ == "__main__":
    main()
