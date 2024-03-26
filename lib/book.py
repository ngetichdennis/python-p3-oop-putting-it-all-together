#!/usr/bin/env python3
# book.py

class Book:
    '''Class representing a book'''

    def __init__(self, title, page_count):
        '''Initialize Book with title and page_count'''
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        '''Simulate turning a page'''
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    
        