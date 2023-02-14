import time


def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        print(f"cache = {cache}")
        key = str(args) + str(kwargs)
        if key in cache:
            print("cache hit")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache
def expensive_function(n):
    # some expensive computations
    res = 0
    for i in range(n):
        time.sleep(0.01)
        res+=1
    return res


def main():
    expensive_function(100)
    expensive_function(100)
    expensive_function(200)
    expensive_function(500)
    expensive_function(500)
if __name__ == '__main__':
    main()