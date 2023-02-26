from collections import OrderedDict


class LRU_Cache:
    """
    Least Recently Used Cache Class
    """

    def __init__(self, capacity):
        self._cache = OrderedDict()
        self._capacity = capacity

    def get(self, key):
        """
        Retrieve item with a provided key.
        """
        ret_val = self._cache.get(key)
        if ret_val is not None:
            del self._cache[key]  # Delete and insert at the end
            self._cache[key] = ret_val
            return ret_val
        else:
            return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        """
        if self._capacity > 0:
            if self.get(key) == -1:
                if self._is_full():
                    self._evict()
            self._cache[key] = value

    def _is_full(self):
        return len(self._cache) >= self._capacity

    def clear(self):
        self._cache.clear()

    def _evict(self):
        """
        remove last recently item used item from the cache.
        """
        self._cache.popitem(last=False)

    def __repr__(self):
        return str(self._cache)


def test_cases():
    lru = LRU_Cache(3)
    # Test Case 3
    for i in range(3):
        lru.set(i, i)
    lru.set(4, 4)
    lru.set(5, 5)
    # Test Case 1
    assert str(lru) == "OrderedDict([(2, 2), (4, 4), (5, 5)])"
    assert lru.get(9) == -1
    assert lru._is_full() == True
    print("Test Case 1 passed.")
    # Test Case 2, only one element set multiple times
    lru = LRU_Cache(3)
    lru.set(4, 4)
    lru.set(4, 4)
    lru.set(4, 4)
    assert str(lru) == "OrderedDict([(4, 4)])"
    print("Test Case 2 passed.")
    # Test Case 3, empty cache
    lru = LRU_Cache(0)
    lru.set(1, 1)
    assert str(lru) == "OrderedDict()" and lru.get(1) == -1
    print("Test Case 3 passed.")
    # Test Case 4, cache with one element
    lru = LRU_Cache(1)
    lru.set(1, 1)
    lru.set(3, 3)
    assert str(lru) == "OrderedDict([(3, 3)])" and lru.get(1) == -1 and lru.get(3) == 3
    print("Test Case 4 passed.")

def main():
    test_cases()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
