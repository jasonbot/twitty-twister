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

def gotEntry(msg):
    print "Got a entry: ", msg.title

twitter.Twitter().search(sys.argv[1], gotEntry).addBoth(
    lambda x: reactor.stop())

reactor.run()
