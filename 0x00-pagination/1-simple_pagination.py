#!/usr/bin/env python3
"""
1-simple_pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function paginates a dataset based on page number
    and page size.

    Args:
      page: The current page number (integer)
      page_size: The number of items per page (integer)

    Returns:
      A tuple containing:
          - start index
          - end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> List[List]:
        """
        Method that returns the appropriate page of the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]
