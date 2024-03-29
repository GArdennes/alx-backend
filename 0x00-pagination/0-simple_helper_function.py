#!/usr/bin/env python3
"""
0-simple_helper_function
"""
from typing import Tuple


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
    if page < 1:
        raise ValueError(
                "Page number must be greater than or equal to 1"
                )
    start = (page - 1) * page_size
    end = start + page_size
    return (start_index, end_index)
