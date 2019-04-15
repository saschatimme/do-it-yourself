import sys, json, requests

# since we have a post request we need to read from stdin
data = json.load(sys.stdin)
# gdwg server
url = "https://c107-250.cloud.gwdg.de/conics"
payload = data
headers = {'content-type': 'application/json'}

# make request to gdwg server
r = requests.post(url, data=json.dumps(payload), headers=headers)

# print json to stdout
print('Content-type: text/json')
print("") 
print(r.text)