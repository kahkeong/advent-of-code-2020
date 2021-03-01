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
    for x in range(1, 26):
        print(f"Question: {x}")
        try:
            question = importlib.import_module(str(x))
            input = question.read()
            try:
                p1 = print_output(question.p1)
                p1(input)
            except:
                print("p1, not implemented")

            try:
                p2 = print_output(question.p2)
                p2(input)
            except:
                print("p2, not implemented")

        except:
            print("p1, not implemented")
            print("p2, not implemented")

        print("")


if __name__ == "__main__":
    main()
