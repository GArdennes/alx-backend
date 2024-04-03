#!/usr/bin/python3
""" 2-lifo_cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
        - a caching system with a LIFO (Last-In, First-Out) eviction policy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for key, _ in reversed(list(self.cache_data.items())):
                print(f"DISCARD: {key}")
                del self.cache_data[key]
                break

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
