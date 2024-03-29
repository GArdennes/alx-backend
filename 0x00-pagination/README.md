# 0x00. Pagination
## Learning Objectives
1. How to paginate a dataset with simple page and page_size parameters.
2. How to paginate a dataset with hypermedia metadata
3. How to paginate in a deletion-resilient manner


## Learning
To paginate a dataset with a Python method. We define a function called paginate which takes the dataset, a page number, and page size as arguments. It performs the following steps:
1. Validate the page number
2. Calculate the total number of items and total pages.
3. Handles cases where the requested page is beyond available pages
4. Calculate the start and end index for slicing the data for the current page.
5. Slices the data and returns it along with metadata like page number, page size, and total pages.

The example below demonstrates the method.
```
def paginate(data, page_number, page_size):
  """
  This function paginates a dataset based on page number and page size.

  Args:
      data: The dataset to be paginated (list, tuple, etc.)
      page_number: The current page number (integer)
      page_size: The number of items per page (integer)

  Returns:
      A dictionary containing:
          - page: The current page number (integer)
          - page_size: The number of items per page (integer)
          - data: The paginated data for the current page (list)
          - total_pages: The total number of pages (integer)
  """

  # Check for invalid page numbers
  if page_number < 1:
    raise ValueError("Page number must be greater than or equal to 1")

  # Get the total number of items
  total_items = len(data)

  # Calculate total number of pages (using ceiling division)
  total_pages = math.ceil(total_items / page_size)

  # Handle cases where requested page is beyond available pages
  if page_number > total_pages:
    page_number = total_pages

  # Calculate start and end index for slicing the data
  start_index = (page_number - 1) * page_size
  end_index = min(start_index + page_size, total_items)

  # Slice the data to get the current page data
  paginated_data = data[start_index:end_index]

  # Return the paginated data and metadata
  return {
      "page": page_number,
      "page_size": page_size,
      "data": paginated_data,
      "total_pages": total_pages
  }

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
page_number = 2
page_size = 3

paginated_data = paginate(data, page_number, page_size)

print(f"Page: {paginated_data['page']}")
print(f"Page Size: {paginated_data['page_size']}")
print(f"Data: {paginated_data['data']}")
print(f"Total Pages: {paginated_data['total_pages']}")
```

To paginate with hypermedia metadata, we define a paginate_with_hypermedia function that retrieves data from a base URL and uses links in the response to navigate to subsequent pages as an example. Here is a breakdown of the steps involved:
1. It initializes an empty list to store all retrieved data
2. It defines a loop that continues as long as a current_url exists.
3. Inside the loop, it fetches data from the current URL using requests.
4. It extracts the data from the response
5. It calls a helper function parse_links_from_header to extract links from the Link header in the response.
6. It checks for a next link in the extracted links dictionary
7. If the next link exists, it updates the current_url to navigate to the next page. Otherwise, the loop ends.
8. The loop continues until all pages are retrieved and the data is added to the all_data list.

Here is the code implementation:
```
import requests

def paginate_with_hypermedia(base_url):
  """
  This function paginates a dataset using hypermedia links in responses.

  Args:
      base_url: The base URL of the API endpoint.

  Returns:
      A list containing all the data across paginated responses.
  """

  all_data = []
  current_url = base_url

  while current_url:
    # Fetch data from the current URL
    response = requests.get(current_url)
    response.raise_for_status()  # Raise exception for non-2xx status codes

    # Extract data from the response (modify based on your API format)
    data = response.json()["data"]
    all_data.extend(data)

    # Extract links from the response headers (modify based on your API)
    links = parse_links_from_header(response.headers.get("Link", ""))

    # Check for "next" link to navigate to the next page
    current_url = links.get("next")

  return all_data

# Function to parse links from the "Link" header (implementation detail)
def parse_links_from_header(link_header):
  """
  This function parses links from the "Link" header (implementation detail).

  Args:
      link_header: The "Link" header value from the response.

  Returns:
      A dictionary containing extracted link relations (e.g., "next", "prev").
  """

  links = {}
  for link in link_header.split(","):
    rel, url = link.strip().split(";", 1)
    links[rel[1:-1]] = url.strip()[1:-1]  # Remove quotes from URL
  return links

# Example usage (assuming your API uses the "Link" header with "next" relation)
base_url = "https://api.example.com/data"
all_data = paginate_with_hypermedia(base_url)

print(f"Total data retrieved: {len(all_data)}")
```

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python`
- A readme file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle
- The length of your files will be tested using wc
- All your modules should have a documentation
- All your functions should have a documentation
- A documentation is not a simple word, it is a real sentence explaining what the purpose of the module, class or method is
- All your functions and coroutines must be type-annotated.
- Setup a file `Popular_Baby_Names.csv`


## Tasks
### 0. Simple helper function
Write a function named `index_range` that takes two integer arguments `page` and `page_size`.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

### 1. Simple pagination
Copy index_range from the previous task and the following class into your code
```
import csv
import math
from typing import List


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass
```
Implement a method named `get_page` that takes two integer arguments page with default value 1 and page_size with default value 10.
- You have to use the Popular_Baby_Names.csv file
- Use assert to verify that both arguments are integers greater than 10.
- Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset.
- If the input arguments are out of range for the dataset, an empty list should be returned.


### 2. Hypermedia pagination
Replicate code from the previous task.
Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, `None` if no next page
- `prev_page`: number of the previous page, `None` if no previous page
- `total_pages`: the total number of pages in the dataset as an integer
Make sure to reuse `get_page` in your implementation.
You can use the `math` module if necessary.


### 3. Deletion-resilient hypermedia pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from datasets when changing page.

Start `3-hypermedia_del_pagination.py` with this code
```
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
            pass
```
Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with a default value of 10.

The method should return a dictionary with the following key-value pairs:
- `index`: The current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with `page_size` 20, and no data was removed from the dataset, the current index should be 60.
- `next_index`: The next index to query with. That should be the index of the first item after the last item on the current page.
- `page_size`: the current page size
- `data`: the actual page of the dataset

**Requirements**:
- User `assert` to verify that `index` is in a valid range
- If the user queries index 0, `page_size` 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with `page_size` 10, but rows 3, 6, 7 were deleted, the user should still receive rows indexed 10 to 19 included.
