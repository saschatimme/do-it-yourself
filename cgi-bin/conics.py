#!/usr/local/bin/python3

import sys, json, requests, os

raw = sys.stdin.read(int(os.environ.get('HTTP_CONTENT_LENGTH', 0)))

# since we have a post request we need to read from stdin
# data = json.loads(raw)
# gdwg server
# url = "https://c107-250.cloud.gwdg.de/conics"
# payload = data
# headers = {'content-type': 'application/json'}
# # # make request to gdwg server
# r = requests.post(url, data=json.dumps(payload), headers=headers)
# # 
# print json to stdout
print('Content-type: text/json')
print("") 
# print('{hello: 2}')
# print(json.dumps(data))
print(raw)