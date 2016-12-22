#!/usr/bin/env python3

import time
import hashlib
import pickle

cache = {}

def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration

def compute_key(function, args, kw):
        key = pickle.dumps((function.__name__, args, kw))
        return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # do we have it already ?
            if (key in cache and not is_obsolete(cache[key], duration)):
                print('we got a winner')
                return cache[key]['value']

            # computing
            result = function(*args, **kw)

            # storing the result
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result
        return __memoize
    return _memoize

@memoize()
def very(a, b):
    return a + b

print(very(2, 3))
print(cache)
time.sleep(5)
print(very(2, 3))
