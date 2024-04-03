#!/usr/bin/python3
""" 100-lfu_cache
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict, Counter


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - a caching system that prioritizes least frequently used items
      - if multiple items have the same frequency, LRU is used for eviction
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_count = Counter()

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
        self.access_count[key] += 1

        # Eviction logic
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_candidates = [
                    key for key, _ in self.cache_data.items()
                        if self.access_count[key] == min(
                            self.access_count.values()
                            )]
            if len(lfu_candidates) > 1:
                discarded_item = next(iter(self.cache_data))
            else:
                discarded_item = lfu_candidates[0]
            del self.cache_data[discarded_item]
            del self.access_count[discarded_item]
            print(f"DISCARD: {discarded_item}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            elf.access_count[key] += 1
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
