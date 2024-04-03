#!/usr/bin/python3
""" 3-lru_cache
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache defines:
        - a caching system with a LRU (Least Recently Used) eviction policy
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

        # Move the accessed key to the front
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict least recently used item
            discarded_item = self.cache_data.popitem(
                    last=False
                    )
            print(f"DISCARD: {discarded_item[0]}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
