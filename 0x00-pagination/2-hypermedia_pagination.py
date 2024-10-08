#!/usr/bin/env python3
"""
Contains class with methods to create simple pagination from csv data
"""
import csv
from math import ceil
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initialize instance. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Return page of dataset. """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Return dict of pagination data."""
        data = self.get_page(page, page_size)
        pag = len(self.dataset())
        pages = ceil(pag / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': pages
        }
