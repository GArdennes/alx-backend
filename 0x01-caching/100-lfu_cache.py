#!/usr/bin/python3
""" 100-lfu_cache
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


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
        self.access_count = []

    def __reorder_items(self, mru_key):
        """ Reorders the items in the cache based on mru
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, key_freq in enumerate(self.access_count):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.access_count[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.access_count[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.access_count.pop(mru_pos)
        self.access_count.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.access_count[-1]
                self.cache_data.pop(lfu_key)
                self.access_count.pop()
                print(f"DISCARD: {lfu_key}")
            self.cache_data[key] = item
            ins_index = len(self.access_count)
            for i, access_count in enumerate(self.access_count):
                if access_count[1] == 0:
                    ins_index = i
                    break
            self.access_count.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
