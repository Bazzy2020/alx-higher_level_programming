#!/usr/bin/python3
"""
Contains definitionfor the class MyList that ingerits from list.
"""

class MyList(list):
    """definition for the class MyList that ingerits from list.
    """
    def print_sorted(self):
        """Prints list elements(int) in ascending order"""

        sortedlist = sorted(self)
        print(sortedlist)
