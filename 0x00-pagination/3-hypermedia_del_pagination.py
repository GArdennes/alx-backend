#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            """
            Methodd that returns a dictionary with hyper pagination info
            Args:
              index: the starting index for the page
              page_size: the number of items per page

            Returns:
              A dictionary containing:
               - index: The current start index of the page
               - next_index: The next index to query with
               - page_size: The current page size
               - data: The actual page of the dataset

            Raises:
              ValueError: If the provided index is negative
            """
            if index < 0:
                raise ValueError("Index cannot be negative")
            data_length = len(self.dataset())
            total_pages = math.ceil(data_length / page_size)
            if index is None:
                page_number = 1
            else:
                page_number = min(
                        math.ceil(index / page_size),
                        total_pages
                        )
            start_index = (page_number - 1) * page_size
            end_index = min(
                    start_index + page_size,
                    data_length
                    )
            next_index = min(end_index + 1, data_length)
            assert 0 <= start_index < data_length, "Invalid"
            paginated_data = self.dataset()[start_index:end_index]
            return {
                    "index": start_index,
                    "next_index": next_index,
                    "page_size": page_size,
                    "data": paginated_data,
                    }
