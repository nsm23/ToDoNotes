import requests

#user_data = {
#    'username': 'django',       #200
#    'password': 'geekbrains'    #{'token': '89de387cd9163d9588dd599eefbd92a678790af1'}
#user_data = {
#    'username': 'django2',       #400
#    'password': 'geekbrains'    #{'non_field_errors': ['Unable to log in with provided credentials.']}

#}
user_data = {
'username': 'Serega',  # 200
'password': 'geekbrains2021'  # {'token': '21fdca5b8bac4edf2b4f9693dbb014a426129968'}
}

url = 'http://127.0.0.1:8000/api-token-auth'

response = requests.post(url, data=user_data)

print(response.status_code)
print(response.json())
