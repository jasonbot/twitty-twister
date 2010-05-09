#!/usr/bin/env python
"""

Copyright (c) 2008  Dustin Sallings <dustin@spy.net>
"""

import os
import sys

from twisted.internet import reactor, protocol, defer, task

<<<<<<< HEAD
from twitty import twitter
=======
from twittytwister import twitter
>>>>>>> c130d77e07bc7a1d81ef607d630e39b94614446e

def cb(answer):
    def f(x):
        print answer
    return f

twitter.Twitter(sys.argv[1], sys.argv[2]).block(sys.argv[3]).addCallback(
    cb("worked")).addErrback(cb("didn't work")).addBoth(
    lambda x: reactor.stop())

reactor.run()
