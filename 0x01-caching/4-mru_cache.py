#!/usr/bin/python3
""" 4-mru_cache
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines:
        - a caching system with a MRU (Most Recently Used) eviction policy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key is not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        # Move the accessed key to the front (mark as recently used)
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
