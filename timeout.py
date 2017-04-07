#!/usr/bin/python3

"""
Mechanism to timeout if a function takes too much time
"""

import random
import signal
import time

TOO_LONG = 8

class TimeoutException(Exception):
    pass


def sig_handler(signum, frame):
    raise TimeoutException()


def my_function():
    x = random.randint(1, 10)
    print('Will sleep for {} seconds'.format(x))
    time.sleep(x)


def main():
    signal.signal(signal.SIGALRM, sig_handler)
    while True:
        signal.setitimer(signal.ITIMER_REAL, TOO_LONG)
        try:
            my_function()
            print('    Function finished.')
        except TimeoutException:
            print('    Function too long. Interrupting.')




if __name__ == '__main__':
    main()
