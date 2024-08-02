import requests
from icecream import ic
import time



def return_conf():
    username = "32909953910040"
    password = "AD597735532909953910040"
    return username,password



def signIn():
    url = "https://billing.e-edu.uz/api/superAdmin/signIn"
    username, password = return_conf()
    body = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=body)
    ic(response.status_code)
    time.sleep(1)
    if response.status_code == 200:
        data = response.json()
        token = data['object']['jwtToken']
        return token
    else:
        ic(response.json())
        return response.json()

# username,password = return_conf()
# signIn(username, password)