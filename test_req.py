import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})

print('Response: ')
print(r.json())
print('-'*60)
print(r.headers)
print('-'*60)

print(r.cookies)

