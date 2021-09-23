import requests, json

url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
token = 'e3414295f0d3158bbee76a157d384690'
path = 'start'

headers = {'X-Auth-Token' : token, 
           'Content-Type' : 'application/json'}

data = '{"problem" : 1}'

r = requests.post('/'.join([url, path]), headers = headers, data = data)
print(r)

