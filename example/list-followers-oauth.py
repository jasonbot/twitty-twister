#!/usr/bin/env python
"""

Copyright (c) 2009  Kevin Dunglas <dunglas@gmail.com>
"""

import os
import sys

from twisted.internet import reactor

from twittytwister import twitter
import oauth

def gotUser(user):
    print "User:  %s (%s)" % (user.name, user.screen_name)

un=None
if len(sys.argv) > 5:
    un=sys.argv[5]

consumer = oauth.OAuthConsumer(sys.argv[1], sys.argv[2])
token = oauth.OAuthToken(sys.argv[3], sys.argv[4])

twitter.Twitter(consumer=consumer, token=token).list_followers(gotUser, un).addBoth(
    lambda x: reactor.stop())

reactor.run()
