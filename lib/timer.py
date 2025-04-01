import time

def timer(func):
    name = 'wuhaolei' # property
    def wrapper(*args, **kwargs): # method
        start = time.time()
        print(f'{name}: {func.__name__} starts in: { start }')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{name}: {func.__name__} ends in: {end}')
        print(f'{name}: {func.__name__} takes: {(end - start):.5f} seconds')
        return result
    return wrapper