#!/usr/bin/env python
"""

Copyright (c) 2009  tsing <tsing@jianqing.org>
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
    print "Got a entry from %s: %s" % (msg.author.name, msg.title)

twitter.Twitter(sys.argv[1], sys.argv[2]).public_timeline(gotEntry).addBoth(
    lambda x: reactor.stop())

reactor.run()
