#!/usr/bin/env python
"""
Produces load on all available CPU cores
"""
import time
from multiprocessing import Pool
from multiprocessing import cpu_count
from random import randint

def load_it(x):
    # t_end = time.time() + 15
    rand = randint(10,39)
    print 'Loading for %d seconds' % rand
    t_end = time.time() + rand
    while time.time() < t_end:
        x*x

def main():
    processes = cpu_count()
    print '-' * 20
    print 'Running load on CPU'
    print 'Utilizing %d cores' % processes
    print '-' * 20
    pool = Pool(processes)
    pool.map(load_it, range(processes))

if __name__ == '__main__':
    main()