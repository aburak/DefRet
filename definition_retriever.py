#!/usr/bin/env python
# coding: utf-8

# created by Ali Burak - last update 15/01/2018

import requests
import json
import sys

save_flag = 0
path = "/home/aburak/"
n_args = len(sys.argv)

# usage of def
if n_args == 1:
    print('Usage of def:\ndef <word> <save_flag>')
    print('<word>: the word to get the definition. It can be more than one word')
    print('<save_flag>: 1 to save the word to words.txt. Default is 0.')
    sys.exit()

# check the number of arguments
if len(sys.argv) < 2 and len(sys.argv) > 3:
    sys.exit('Wrong number of arguments!')

# check if the call involves parameter stating "save"
sf = 0 # to indicate if save flag is given
if str.isdigit(sys.argv[n_args-1]) == True:
    save_flag = int(sys.argv[n_args-1])
    sf = 1
else:
    save_flag = 0

# variables
word_id = sys.argv[1] # word to look up the definition in dictionary
app_id = '756ccf57' # app id of Oxford Dictionary
app_key = '96fb003eb6bd36c36a78cbb54297fb22' # app key of Oxford Dictionary
base_url = 'https://od-api.oxforddictionaries.com/api/v1/'
source_lang = 'en' # language choice

# construct the word to get the definition
for i in xrange(2,n_args-sf):
    word_id = word_id + ' ' + sys.argv[i]

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
