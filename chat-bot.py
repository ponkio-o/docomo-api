#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import types

KEY = 'API key'

# 1回目の呼び出し（会話の開始）

endpoint = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=REGISTER_KEY'
url = endpoint.replace('REGISTER_KEY', KEY)

#会話の入力
utt_content = raw_input('>>')

payload = {'utt' : utt_content, 'context': ''}
headers = {'Content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
data = r.json()

response = data['utt']
context = data['context']
print "response: %s" %(response)

while True:
    utt_content = raw_input('>>')
    payload['utt'] = utt_content
    payload['context'] = data['context']

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    response = data['utt']
    context = data['context']

    print "response: %s" %(response)
