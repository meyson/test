import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})

print('Response: ')
print(r.json())
print('- headers'*60)
print(r.headers)
print('- cookies'*60)

print(r.cookies)

