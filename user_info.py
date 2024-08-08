import requests
from sign_in import signIn

token = signIn()
from icecream import ic

def userInfo(pinfl,serialNumber,birthDate ):
    url = "https://billing.e-edu.uz/api/applicant/userAndDtmInfo"
    headers = {
        "Authorization": "Bearer " + token
    }
    body = {
        "pinfl": str(pinfl),
        "serialAndNumber": str(serialNumber),
        "birthDate": str(birthDate)
    }

    ic(body)
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        # ic(response.json())
        data = response.json()
        # ic(data['givenDate'])
        
        givenDate = data['givenDate']
        passportExpireDate = data['passportExpireDate']
        firstName = data['firstName']
        lastName = data['lastName']
        fatherName = data['fatherName']
        birthDate = data['birthDate']
        citizenship = data['citizenship']
        nationality = data['nationality']
        gender = data['gender']
        country = data['country']
        region = data['region']
        district = data['district']
        address = data['address'] if data['address'] else None
        existInDTM = data['existInDTM']
        dtmSpeciality = data['dtmSpeciality']
        dtmBall = data['dtmBall']
        photo = data['photo']
        obj = {
            "givenDate": givenDate,
            "passportExpireDate": passportExpireDate,
            "firstName": firstName,
            "lastName": lastName,
            "fatherName": fatherName,
            "birthDate": birthDate,
            "citizenship": citizenship,
            "nationality": nationality,
            "gender": gender,
            "country": country,
            "region": region,
            "district": district,
            "address": address,
            "existInDTM": existInDTM,
            "dtmSpeciality": dtmSpeciality,
            "dtmBall": dtmBall,
            "photo": photo
        }
        return obj
    else:
        return False

# data = userInfo(51903046700030, "AC2957306")
# ic(data)