import requests

# environ import for environment variables
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def auth_url():
    return env('AUTH_URL') + '?' + 'client_id=' + env('CLIENT_ID') + '&' + 'redirect_uri=' + 'http://localhost:8000/votes/' + '&' + 'response_type=' + 'code' 

def auth_grant(code: str):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    params = {
        'client_id': env('CLIENT_ID'),
        'client_secret': env('CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/votes/'
    }

    url = env('TOKEN_URL')
    response = requests.post(url, data=params)
    return response.json()

def get_osu_user(code: str):
    token = auth_grant(code)

    headers = {
        'Authorization': f"{token['token_type']} {token['access_token']}",
    }
    url = env('API_URL') + 'me'

    response = requests.get(url, headers=headers)
    return response