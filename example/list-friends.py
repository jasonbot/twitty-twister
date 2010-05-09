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

def gotUser(user):
    print "User:  %s (%s)" % (user.name, user.screen_name)

def gotPage(next, prev):
    print "end of page: next:%s prev:%s" % (next, prev)

def error(e):
    print "ERROR: %s" % (e)
    reactor.stop()

un=None
if len(sys.argv) > 3:
    un=sys.argv[3]

params={}
if len(sys.argv) > 4:
    params = {'cursor':sys.argv[4]}

twitter.Twitter(sys.argv[1], sys.argv[2]).list_friends(gotUser, un, params, page_delegate=gotPage).addCallbacks(
    lambda x: reactor.stop(), error)

reactor.run()
