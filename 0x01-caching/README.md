# 0x01. Caching
## Learning Objectives
1. What is a caching system?
2. What does FIFO mean?
3. What does LIFO mean?
4. What does LRU mean?
5. What does MRU mean?
6. What does LFU mean?
7. What is the purpose of a caching system?
8. What are the limits of a caching system?

## Learning
In computing, a caching system acts as a high-speed storage layer that holds a subset of frequently accessed data. Its primary goal is to significantly improve data retrieval performance by minimizing the need to access the original, slower storage location. The main purpose of a caching system is to speed up data retrieval by storing a temporary copy of frequently accessed data. It acts like a middleman between the user and the slower main storage location. Here are some caching strategies. FIFO means First In First Out, LIFO means Last In First Out. LRU stands for Least Recently Used. It’s a caching strategy used to improve efficiency by prioritizing data that’s likely to be accessed again soon. Imagine a stack of papers you’re working on. With LRU, the paper you looked at most recently would be on top for easy retrieval, and the one you haven’t touched in a while would be on the bottom. MRU stands for Most Recently Used. Here, the cache prioritizes the item that was accessed most recently. Imagine a playlist on repeat - MRU would keep the most recently played songs readily available. LFU stands for Least Frequently Used. LFU prioritizes items based on how often they are accessed, not necessarily when. It evicts the item that has been used the least overall. Think of a web browser cache - LFU might keep frequently visited websites readily available while removing those you only accessed once.

Caching systems are great for speeding up data access, but they do have some limitations:
- **Cache invalidation:** A major challenge is ensuring the cached data stays consistent with the original source. If the main storage is updated, the cached copy might become outdated, leading to users seeing stale data.
- **Limited Size:** Caches have a finite amount of space. They can’t store everything, so decisions need to be made about what data to keep and for how long.
- **Overhead:** Maintaining a cache introduces some overhead. The system needs to track what’s in the cache, manage its size, and handle updates to both the cache and the main storage.
- **Security concerns:** Sensitive data stored in the cache could be a security risk if not properly secured. Cache invalidation strategies might also introduce vulnerabilities if not implemented carefully. 
- **Limited applicability:** Caching isn’t always the best solution. For data that’s constantly changing or rarely accessed, caching might not provide much benefit.

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A readme file, at the root of the folder of the project, is mandatory.
- Your code should not use the `pycodestyle` style.
- All your files must be executable.
- The length of your files will be tested using `wc`
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.
- A documentation is not a simple word, it's a real sentence explaining what’s the purpose of the module, class or method.

## Tasks
### 0. Basic dictionary
Create a class `BasicCache` that inherits from `BasicCaching` and is a caching system:

Requirements

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- This caching system doesn’t have a limit.
- The method `def put(self, key, item)` must assign to the dictionary `self.cache_data` the `item` value for the key `key`. If `key` or `item` is `None`, this method should not do anything.
- The method `def get(self, key) must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.


### 1. FIFO caching
Create a class FIFOCache that inherits from BaseCaching and is a caching system:

Requirements

- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
- The method `def put(self, key, item):` must assign to the dictionary self.cache_data the item value for the key key.
- If key or item is None, this method should not do anything.
- If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
- You must discard the first item put in cache (FIFO algorithm)
- You must print DISCARD: with the key discarded and following by a new line
- The method `def get(self, key):` must return the value in self.cache_data linked to key.
- If key is None or if the key doesn’t exist in self.cache_data, return None.


### 2. LIFO Caching
Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system.

Requirements

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- The method `def put(self, key, item):` must assign to the dictionary `self.cache_data` the `item` value for the key `key`. 
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`. You must discard the last item put in cache (LIFO algorithm). You must print `DISCARD:` with the `key` discarded and followed by a new line.
- The method `def get(self, key):` must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.


### 3. LRU Caching
Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

Requirements:

- You must use `self.cache-data` - dictionary form the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- The method `def put(self, key, item):` must assign to the dictionary `self.cache_data` the  `item` value for the key `key`.
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`. You must discard the least recently used item (LRU algorithm). You must print `DISCARD:` with the `key` discarded and followed by a new line.
- The method `def get(self, key)` must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.


### 4. MRU Caching
Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system.

Requirements:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- The method `def put(self, key, item)` must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS:`. You must discard the most recently used item (MRU algorithm). You must print `DISCARD:` with the `key` discarded and followed by a new line.
- The method `def get(self, key):` must return the value in `self.cache_data` linked to `key`.
- If `key` is `None` or if the `key` doesn’t exist in `self.cache-data`, return `None`.


### 5. LFU Caching
Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:

Requirements:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- The method `def put(self, key, item):` must assign to the dictionary `self.cache_data` the `item` value for the key `key`. 
- If `key` or `item` is `None`, this method should not do anything.
- If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS:`. You must discard the least frequency used item (LFU algorithm). If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used. You must print `DISCARD:` with the `key` discarded and followed by a new line.
- The method `def get(self, key)` must return the value in `self.cache_data` linked to `key`. 
- If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.
