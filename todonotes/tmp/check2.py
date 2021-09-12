import requests

# user_data = {
#    'username': 'django',       #200
#    'password': 'geekbrains'    #{'token': '0a08d5986e3891b5e720812c71ff176686f5323e'}
user_data = {
    'Authorization':
        'Token 0a08d5986e3891b5e720812c71ff176686f5323e'
}

url = 'http://127.0.0.1:8000/api/projects/'

response = requests.get(url, data=user_data)
print(response.status_code)
print(response.json())
