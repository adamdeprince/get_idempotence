import sys
import gflags
import requests

FLAGS = gflags.FLAGS

gflags.DEFINE_string(
    'register',
    None,
    'Register a new account for an email address')

gflags.DEFINE_string(
    'invalidate',
    None,
    'Invalidate and reissue a new API key')

gflags.register_validator(
    'register',
    lambda x:x or (not x and not FLAGS.key),
    "Don't provide a `--key` when regsitering")

gflags.register_validator(
    'invalidate',
    lambda x:not x or (x and FLAGS.key),
    "You must provide a `--key` when invalidating a key")

gflags.DEFINE_string(
    'api',
    'https://idempotence.herokuapp.com/',
    'The root url to connect to.  Change this when testing')

def register():
    if "yes" != raw_input(
            ("Enter yes if you accept the terms of service at http://get-idempotence.com/tos.html\n"
             "and agree to time from time receive email mails from announcing product, serice\n"
             "and tos changes.\n")).lower():
        print "Sorry, you have to accept the TOS to use this application"
        return 0
    print FLAGS.email
    resp = requests.post(FLAGS.api + "register", data=dict(email=FLAGS.register))
    if resp.status_code < 400:
        print "Great, your API key is on its way."
        return 0
    else:
        print "Opps, there was an error: ", resp.status_code
        print resp.text
        return 1
        

def invalidate():
    requests.post("http://idempotence.heroku.com/invalidate", data = {'email': email, 'key': key})
    print "Great, your new API key is on its way."
    
