import functools
import threading
import time

class FuncTimeoutException(Exception):
    pass

def func_timeout(time):
    print(f'func_timeout exec at most {time} seconds')
    def decorator(func):
        def wrapper(*args, **kwargs):
            def payload():
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    raise e
        
            # core logic
            thread = threading.Thread(target=payload)
            thread.start()
            thread.join(timeout=time)

            if thread.is_alive():
                raise FuncTimeoutException(f'func {func.__name__} timed out after {time} seconds')

        return wrapper
    return decorator


@func_timeout(3)
def test_func_timeout():
    time.sleep(5)


if __name__ == '__main__':
    try:
        test_func_timeout()
    except Exception as e:
        print("Caught exception:", e)
