#!/usr/bin/env python3
"""
FIFO caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """implementing put and get"""

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """to add a new item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
              and key not in self.cache_data.keys():
                  discarded_key = list(self.cache_data.keys())[0]
                  del self.cache_data[discarded_key]
                  print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """retrieve from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
