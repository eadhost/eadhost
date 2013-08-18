#
#
# listen on an https connection for posts from github and add entries to an amazon SQS queue
#
# http://stackoverflow.com/a/14550821/1763984
# http://boto.s3.amazonaws.com/sqs_tut.html
# http://flask.pocoo.org/snippets/111/
# http://flask.pocoo.org/snippets/8/

# https://help.github.com/articles/what-ip-addresses-does-github-use-that-i-should-whitelist#service-hook-ip-addresses
# "We highly recommend that you don't white list IPs for Service Hooks. Instead, setup HTTPS and basic authentication to verify incoming requests."


from flask import Flask, request
import json
from OpenSSL import SSL

import boto
# conn = boto.connect_sqs() 
