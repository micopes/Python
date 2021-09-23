import requests, json

url = '---'
token = '---'
path = 'start'

headers = {'X-Auth-Token' : token, 
           'Content-Type' : 'application/json'}

data = '{"problem" : 1}'

r = requests.post('/'.join([url, path]), headers = headers, data = data)
print(r)

