import requests

from icecream import ic

from sign_in import signIn
def contractWithoutApp(address,
                       admissionType,
                       birthDate, 
                       citizenship,
                       contractPriceId,
                       checkingAccountId,
                       contractSum,
                       contractTemplateId,
                       country,
                       district,
                       dtmBall,
                       dtmSpeciality,
                       eduFinishedRequest,
                       existInDTM,
                       fatherName,
                       firstName,
                       gender,
                       lastName,
                       monthId,
                       nationality,
                       passportExpireDate,
                       phoneNumber,
                       photo,
                       pinfl,
                       region,
                       serialAndNumber):
    url = "https://billing.e-edu.uz/api/applicant/contractWithoutApp"
    token = signIn()
    headers = {
        "Authorization": "Bearer " + token
    }
    body = {
        "address": address,
        "admissionType": admissionType,
        "birthDate": birthDate,
        "citizenship": citizenship,
        "contractPriceId": contractPriceId,
        "checkingAccountId": checkingAccountId,
        "contractSum": contractSum,
        "originalContractSum": contractSum,
        "contractTemplateId": contractTemplateId,
        "country": country,
        "district": district,
        "dtmBall": dtmBall,
        "dtmSpeciality": dtmSpeciality,
        "eduFinishedRequest": eduFinishedRequest,
        "existInDTM": existInDTM,
        "fatherName": fatherName,
        "firstName": firstName,
        "gender": gender,
        "lastName": lastName,
        "monthId": monthId,
        "nationality": nationality,
        "passportExpireDate": passportExpireDate,
        "phoneNumber": phoneNumber,
        "photo": photo,
        "pinfl": pinfl,
        "region": region,
        "serialAndNumber": serialAndNumber,
        "discount": 0
    }
    ic( address,
        admissionType,
        birthDate, 
        citizenship,
        contractPriceId,
        checkingAccountId,
        contractSum,
        contractTemplateId,
        country,
        district,
        dtmBall,
        dtmSpeciality,
        eduFinishedRequest,
        existInDTM,
        fatherName,
        firstName,
        gender,
        lastName,
        monthId,
        nationality,
        passportExpireDate,
        phoneNumber,
        pinfl,
        region,
        serialAndNumber)
    from GetContract import Contract
    checkContract = Contract().checkContract(pinfl)
    ic("checkContract -->", checkContract)
    if checkContract is False:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 201 or response.status_code == 200:
            data = response.json()
            return data
        else:
            message = response.json().get('message')
            return {'message': message, 'status_code': response.status_code}
    elif checkContract:
        ic('Contract already exists')
        return checkContract

# res = contractWithoutApp()