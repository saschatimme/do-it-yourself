#!/usr/local/bin/python3
import sys, json, requests, os, base64
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
data = json.loads(base64.b64decode(form.getvalue("data")))
# gdwg server
url = "https://c107-250.cloud.gwdg.de/conics"
headers = {'content-type': 'application/json'}
# make request to gdwg server
r = requests.post(url, data=json.dumps(data), headers=headers)
# print json to stdout
print("Content-type: text/json\n")
print(r.text)
