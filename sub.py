#!/usr/bin/env python

import redis

# redis connection init
r = redis.Redis()
# init pubsub
ps = r.pubsub()
# tell pubsub to listen to a channel
ps.subscribe('zonk1024')
# iterate over the listen generator object
for m in ps.listen():
    # print the message data
    print m['data']
    # print the message object
    print m
