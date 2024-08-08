import requests
from icecream import ic
import json

email = "ulugbek9015@gmail.com"
password =  "99KJL102MNB@I"

def login():
    url = "https://crmapi.mentalaba.uz/v1/auth/super-admin/login"
    body = {
        "email": email,
        "password": password
    }
    response = requests.post(url, json=body)
    if response.status_code == 200:
        data = response.json()
        ic(data)
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None
# login()
def verify(code):
    url = "https://crmapi.mentalaba.uz/v1/auth/super-admin/verify-login"
    body = {
        "email": email,
        "code": code
    }
    ic(body)
    response = requests.post(url, json=body)
    if response.status_code == 200:
        data = response.json()
        token = data['token']
        ic(data)
        return token
    else:
        ic(f"Error: {response.status_code}")
        return None
    
# verify(354783)

def finally_json(file_path):
    array = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for obj in data:
            applicant_id = obj['Applicant Id']
            contract_file_link = obj['Contract Url']
            new_obj = {
                "applicant_id": applicant_id,
                "contract_file_link": contract_file_link
            }
            if contract_file_link.startswith("https://billing.e-edu.uz"):
                array.append(new_obj)
    file_name = "finally1_new3.json"
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(array, file, ensure_ascii=False, indent=4)
    return file_name

# finally_json("AIFU_08_05(4).json_result.json")

def send_file(token, file_path):
    url = "https://crmapi.mentalaba.uz/v1/application"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    with open(file_path, 'rb') as file:
        files = {
            "file": (file_path, file, "application/json")
        }

        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            data = response.json()
            ic(data)
            return data
        else:
            ic(f"Error: {response.status_code}")
            return 
        
login()
code = int(input("input your code: "))
token = verify(code)
ic(token)
file_name = finally_json("AIFU_06_08 (4).json_result.json")
ic(file_name)
# data = send_file(token, file_name)
# ic(data)