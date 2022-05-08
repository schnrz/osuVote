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
    credentials = response.json()
    return response.json()

def get_osu_user():

    data = {
        'client_id': env('CLIENT_ID'), 
        'client_secret': env('CLIENT_SECRET'),
        'grant_type': 'authorization_code'
    }

    url = env('TOKEN_URL')

    response = requests.post(url, data=data)
    if response:
        return response.json().get('access_token')
    else:
        return response
    # .json().get('access_token')