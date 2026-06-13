import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.4f} seconds")

        return result

    return wrapper


@timer
def count_to_million():
    for i in range(1_000_000):
        pass


count_to_million()