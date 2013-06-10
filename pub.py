#!/usr/bin/env python

import redis
from sys import argv

# redis connection init
r = redis.Redis()
if len(argv) > 1:
    for a in argv[1:]:
        # all it takes to post to a channel
        r.publish('zonk1024', a)
