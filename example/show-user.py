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

def gotUser(u):
    print "Got a user: %s" % u

twitter.Twitter(sys.argv[1], sys.argv[2]).show_user(sys.argv[3]).addCallback(
    gotUser).addBoth(lambda x: reactor.stop())

reactor.run()
