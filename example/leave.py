#!/usr/bin/env python
"""

Copyright (c) 2008  Dustin Sallings <dustin@spy.net>
"""

import os
import sys

sys.path.append(os.path.join(sys.path[0], '..', 'lib'))
sys.path.append('lib')

from twisted.internet import reactor, protocol, defer, task

from twitty import twitter

def cb(answer):
    def f(x):
        print answer
    return f

twitter.Twitter(sys.argv[1], sys.argv[2]).leave(sys.argv[3]).addCallback(
    cb("worked")).addErrback(cb("didn't work")).addBoth(
    lambda x: reactor.stop())

reactor.run()
