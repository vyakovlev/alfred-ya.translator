#!/usr/bin/python
# -*- coding: utf-8 -*-

############################################################################################################
#### Translates a piece of text or a word
#### Automatic language detection
#### Written by Vladimir Yakovlev <i@vyakovlev.com>
#### Version 0.1.1
############################################################################################################

# All this packages should be available on any fresh macOS installation
import sys
import os
import json
import httplib
import urllib
import datetime
import string

# Configuration goes here
LOCAL = "ru" # change to your native or desired language, e.g. ru = Russian (see https://tech.yandex.ru/translate/doc/dg/concepts/api-overview-docpage/)
FOREIGN = "en" # change to you desired foreign language, e.g. en = English

APIKEY = os.environ.get('APIKEY')
if APIKEY is None:
    sys.stdout.write("APIKEY is not defined (see manual)")
    sys.exit(1)

if len(sys.argv) != 2:
    sys.stdout.write("Can't translate nothing")
    sys.exit(2)

INPUT=sys.argv[1]

# get a json object from a request
def get_json(endpoint):
    conn = httplib.HTTPSConnection("translate.yandex.net","443")
    headers = {'Content-Type' : 'application/x-www-form-urlencoded', 'Accept' : '*/*'}
    params = urllib.urlencode({'text': INPUT})
    conn.request("POST","/api/v1.5/tr.json/%s&key=%s" % (endpoint, APIKEY), params, headers)

    response = conn.getresponse()

    if response.status != 200: # something nasty happened
        return None
    else:
        return json.loads(response.read()) # returns a json object for further work


############################################################################################################
#### Main Part
############################################################################################################
if __name__ == "__main__":
    src_json = get_json("detect?hint=%s,%s" % (LOCAL, FOREIGN))
    if src_json == None or 'lang' not in src_json:
        sys.stdout.write("WARNING: Can't detect language for %s" % INPUT)
        sys.exit(-1)

    # detects from/to languages key-pair
    source = src_json['lang']
    destination = FOREIGN
    if source != LOCAL:
        destination = LOCAL

    # tries to translate
    translation = get_json("translate?lang=%s-%s" % (source, destination))
    if translation == None or 'text' not in translation:
        sys.stdout.write("WARNING: Can't translate %s from %s to %s" % (INPUT, source, destination))
        sys.exit(-2)

    sys.stdout.write(translation['text'][0]) # all went good
    sys.exit(0)