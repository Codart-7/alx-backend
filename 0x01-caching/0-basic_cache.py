#!/usr/bin/env python3
"""
Basic caching system
"""


class BasicCache(BaseCaching):
    """implementing put and get"""

    def __init__(self):
        """init"""
        super().__init__()


    def put(self, key, item):
        """to add a new item to the cache"""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
