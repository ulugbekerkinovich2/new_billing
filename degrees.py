import requests
from icecream import ic

from sign_in import signIn


token = signIn()
base_url = "https://billing.e-edu.uz/"
def degrees_(token):
    url = f"{base_url}api/public/degrees"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None

def eduTypes(token):
    url = f"{base_url}api/public/getEduType"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None

def ByUniversityAndEduType(token, eduTypeId, degreeId, educationLevelId=11):
    url = f"{base_url}api/classifier/speciality/byUniversityAndEduType"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "eduTypeId": eduTypeId,
        "degreeId": degreeId,
        "educationLevelId": educationLevelId
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None
    
def typesByEduTypeAndDegree(token, eduTypeId, degreeId):
    url = f"{base_url}api/adminService/contractTemplate/admin/typesByEduTypeAndDegree"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "eduTypeId": eduTypeId,
        "degreeId": degreeId
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None
    
def languages(token):
    url = f"{base_url}api/public/languages"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None
    
def languagesByEduType(token, eduTypeId, degreeId, typeCode):
    url = f"{base_url}api/adminService/contractTemplate/languagesByEduTypeAndDegreeAndType"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "eduTypeId": eduTypeId,
        "degreeId": degreeId,
        "typeCode": typeCode
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None

def byEduTypeAndLanguageAndType(token, eduType, lagaugeId, typeCode, degreeId):
    url = "https://billing.e-edu.uz/api/adminService/contractTemplate/byEduTypeAndLanguageAndType"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "eduTypeId": eduType,
        "languageId": lagaugeId,
        "typeCode": typeCode,
        "degreeId": degreeId
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        ic(f"Error: {response.status_code}")
        return None