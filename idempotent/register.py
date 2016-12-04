import gflags
import sys

FLAGS = gflags.FLAGS

gflags.DEFINE_string(
    'register',
    None,
    ('Register a new account for an email address'))

gflags.DEFINE_string(
    'invalidate',
    None,
    ('Invalidate and reissue a new API key'))

gflags.register_validator(
    'register',
    lambda x:x or (not x and not FLAGS.key),
    "Don't provide a `--key` when regsitering")

gflags.register_validator(
    'invalidate',
    lambda x:not x or (x and FLAGS.key),
    "You must provide a `--key` when invalidating a key")

def register():
    if "yes" != raw_input("Enter yes if you accept the terms of service at http://get-idempotence.com/tos.html").lower():
        print "Sorry, for have to accept the TOS to use this application"
        sys.exit(0)
    requests.post("http://idempotence.heroku.com/register", data = {'email': email})
    print "Great, your API key is on its way."

def invalidate():
    requests.post("http://idempotence.heroku.com/invalidate", data = {'email': email, 'key': key})
    print "Great, your new API key is on its way."
    
