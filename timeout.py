#!/usr/bin/python3

"""
Mechanism to timeout if a function takes too much time
"""

import random
import signal
import time
from functools import wraps


class TimeoutException(Exception):
    pass


def sig_handler(signum, frame):
    raise TimeoutException()


def timeout(delay):
    def timeout_sec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.setitimer(signal.ITIMER_REAL, delay)
            return func(*args, **kwargs)
        return wrapper
    return timeout_sec


@timeout(5)
def my_function():
    x = random.randint(1, 10)
    print('Will sleep for {} seconds'.format(x))
    time.sleep(x)


def main():
    signal.signal(signal.SIGALRM, sig_handler)
    while True:
        try:
            my_function()
            print('    Function finished.')
        except TimeoutException:
            print('    Function too long. Interrupting.')




if __name__ == '__main__':
    main()
