'''
Given a list of tuples with the different choices and their relative
occurences, create a weighted probability generator
'''

import random
from itertools import accumulate
from bisect import bisect

services = [ ('postman', 1), ('google', 3) ]
status = [ ('success', 5), ('failure', 2), ('expired', 1) ]

# Weighted probabilities generator
# expect a list of tuples : [ ('success', 5), ('failure', 2), ('expired', 1) ]
def create_gen(weighted_choices):
    def weighted_gen():
        choices, weights = zip(*weighted_choices)
        cumdist = list(accumulate(weights))
        x = random.random() * cumdist[-1]
        while True:
            yield choices[bisect(cumdist, x)]
    return weighted_gen

status_gen = create_gen(status)
service_gen = create_gen(services)

for _ in range(20):
    print(next(status_gen), next(service_gen))
