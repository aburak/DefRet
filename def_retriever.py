#!/usr/bin/env python
# coding: utf-8

# created by Ali Burak - last update 15/01/2018

import requests
import json
import sys

save_flag = 0
path = "/home/aburak/"

# check the number of arguments
if len(sys.argv) < 2 and len(sys.argv) > 3:
    sys.exit('Wrong number of arguments!')

# check if the call involves parameter stating "save"
if len(sys.argv) == 3:
    save_flag = 1
    

# variables
word_id = sys.argv[1] # word to look up the definition in dictionary
app_id = '' # app id of Oxford Dictionary
app_key = '' # app key of Oxford Dictionary
base_url = 'https://od-api.oxforddictionaries.com/api/v1/'
source_lang = 'en' # language choice


url = base_url + 'entries/' + source_lang + '/' +  word_id.lower() 
r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

# check the response
if r.status_code == 404:
    print 'Word ' + word_id + ' is not found!'
    sys.exit(0)

if r.status_code == 500:
    print 'Internal Error: An error occured while processing data'
    sys.exit(0)

if r.status_code != 200:
    print 'Unknown error!'
    sys.exit(0)


try:
    j_data = json.loads(json.dumps(r.json()))
    t = j_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definition = ''
    nl_def = ''
    for i in xrange(len(t)):
	definition +=  str(i+1) + ". " + t[i]['definitions'][0] + '\t'
	nl_def += str(i+1) + ". " + t[i]['definitions'][0] + '\n'
    if save_flag == 1:
        with open( path + "words.txt", "a") as myfile:
            myfile.write(word_id + "\t")
            myfile.write(definition + "\n")
    
    print "Word:\n" + word_id + "\nDefinition:\n" + nl_def
except:
    print sys.exc_info()[0]




