import importlib
import functools
import time
import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def print_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = round_up(end_time - start_time, 3)
        print(f"{func.__name__}, time: {run_time}, result: {result}")

    return wrapper


def main():
    for x in range(1, 17):
        question = importlib.import_module(str(x))
        print(f"Question: {x}")
        input = question.read()
        p1 = print_output(question.p1)
        p2 = print_output(question.p2)

        p1(input)
        p2(input)


if __name__ == "__main__":
    main()
