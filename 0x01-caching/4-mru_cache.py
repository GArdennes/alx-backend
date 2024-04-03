#!/usr/bin/python3
""" 4-mru_cache
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


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
        self.cache_data[key] = item

        # Move the accessed key to the front (mark as recently used)
        self.cache_data.move_to_end(key, last=False)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict least recently used item (at the back of OrderedDict)
            discarded_item = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discarded_item[0]}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        # Move the accessed key to the front (mark as recently used)
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
