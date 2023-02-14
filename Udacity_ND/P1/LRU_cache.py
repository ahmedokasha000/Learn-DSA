from collections import OrderedDict


class LRU_Cache:

    def __init__(self, capacity):
        self._cache = OrderedDict()
        self._capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        ret_val = self._cache.get(key)
        if ret_val is not None:
            del self._cache[key]
            self._cache[key] = ret_val
            return ret_val
        else: 
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.get(key) == -1:
            if self._is_full():
                self._evict()
        self._cache[key] = value

    def _is_full(self):
        return len(self._cache) >= self._capacity

    def clear(self):
        self._cache.clear()

    def _evict(self):
        self._cache.popitem(last=False)

    def __repr__(self):
        return str(self._cache)

def main():
    lru = LRU_Cache(2)
    print(f"lru = {lru}")
    lru.set(1, 1);
    lru.set(2, 2);
    print(f"lru = {lru.get(1)}")
    print(f"lru = {lru}")
    lru.set(3, 3);
    print(f"lru = {lru.get(2)}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
