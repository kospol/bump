#!/usr/bin/env python

import requests;
import optparse
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Get the options parser
parser = optparse.OptionParser()

# Suppress the insecure request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# default values
baseurl = "https://localhost:8000/"
username = "admin"
password = "changeme"

parser.add_option('-l', '--url',
                  action="store", dest="baseurl",
                  help="the url of the server", default=baseurl)

parser.add_option('-u', '--username',
                  action="store", dest="username",
                  help="the username", default=username)

parser.add_option('-p', '--password',
                  action="store", dest="password",
                  help="the password", default=password)

options, args = parser.parse_args()

# assign the values from the options parser
baseurl = options.baseurl
username = options.username
password = options.password

# set up the urls
loginurl = baseurl + "/en-US/account/login"
bumpurl = baseurl + "/en-US/_bump"

s = requests.session()
try:
    r = s.get(loginurl, verify=False)
except requests.exceptions.ConnectionError:
    print "Connection error: is Splunk up and running? Is the url correct?"
    print "The current url is: " + baseurl
    sys.exit(0)

try:
    cval = r.cookies['cval']
except:
    print "Are you sure that's the correct url?"
    print "The current url is: " + baseurl
    sys.exit(0)

post_data = {'username': username, 'password': password, 'cval': cval}
r = s.post(loginurl, post_data, verify=False)
r = s.get(bumpurl, verify=False)
if "Forbidden" in r.text:
    print "Wrong username or password!"
    sys.exit(0)

for line in r.text.splitlines():
    if 'splunk_form_key' in line:
        formkey = re.search(r'\d+', line).group()
        break

bump_data = {"splunk_form_key": formkey}
r = s.post(bumpurl, bump_data, verify=False)

for line in r.text.splitlines():
    if 'Current version' in line:
        curVersion = re.search(r'\d+', line).group()
        break

print "bump! " + curVersion
