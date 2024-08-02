import requests
from sign_in import signIn
import time
token = signIn()
from icecream import ic
from degrees import degrees_, eduTypes, languages, ByUniversityAndEduType, \
typesByEduTypeAndDegree,languagesByEduType, byEduTypeAndLanguageAndType

# def typesId(eduType,degreeId):
#     ic(eduType,degreeId, 'typeid keldi')
#     if eduType == 'Kunduzgi' and degreeId == 'Bakalavr':
#         eduType = 11
#         degreeId = 11
#         educationLevelId = 11
#         return eduType, degreeId, educationLevelId
#     elif eduType == 'Sirtqi' and degreeId == 'Bakalavr':
#         eduType = 11
#         degreeId = 13
#         educationLevelId = 11
#         return eduType, degreeId, educationLevelId
#     elif eduType == 'Kunduzgi' and degreeId == 'Magistr':
#         eduType = 12
#         degreeId = 11
#         educationLevelId = 11
#         return eduType, degreeId, educationLevelId

class University:
    def __init__(self, token):
        self.token = token
        self.degrees = []
        self.eduTypes = []
        self.languages = []
        self.ByUniversityAndEduTypes = []
        self.typesByEduTypeAndDegrees = []
        self.languagesByEduTypes = []
        self.byEduTypeAndLanguageAndTypes = []
    
    def return_degrees(self, name):
        data = degrees_(self.token)
        if data is not None:
            for degree in data:
                code = degree['code']
                name = degree['name']
                if name == name:
                    obj = {
                        'code': code,
                        'name': name
                    }
                    return obj
                # self.degrees.append(obj)
            # return self.degrees
        else:
            ic(data)
            return None
    def return_edu_types(self, name):
        data = eduTypes(self.token)
        if data is not None:
            for eduType in data:
                code = eduType['code']
                name = eduType['name']
                if name == name:
                    obj = {
                        'code': code,
                        'name': name
                    }
                    return obj
            #     self.eduTypes.append(obj)
            # return self.eduTypes
        else:
            ic(data)
            return None
    
    def return_languages(self):
        data = languages(self.token)
        if data is not None:
            for language in data:
                code = language['code']
                name = language['nameUz']
                obj = {
                    'code': code,
                    'name': name
                }
                self.languages.append(obj)
            return self.languages
        else:
            ic(data)
            return None
    
    def return_by_university_and_edu_type(self, eduTypeId, degreeId, IspecialityCode, IeduTypeName, IdegreeName):
        data = ByUniversityAndEduType(self.token, eduTypeId, degreeId, 11)
        if data is not None:
            for obj in data:
                checkingAccountId = obj['checkingAccountId']
                # ic(checkingAccountId)
                contractPriceId = obj['contractPriceId']
                # ic(contractPriceId)

                specialityName = obj['specialityName']
                # ic(specialityName)
                specialityCode = obj['specialityCode']
                # ic(specialityCode)
                eduTypeName = obj['eduTypeName']
                # ic(eduTypeName)
                degreeName = obj['degreeName']
                # ic(degreeName)
                contractPrice = int(obj['contractPrice'])
                # ic(contractPrice)
                if specialityCode == IspecialityCode and eduTypeName == IeduTypeName and degreeName == IdegreeName:
                    new_obj = {
                        'checkingAccountId': checkingAccountId,
                        'contractPriceId': contractPriceId,
                        'specialityName': specialityName,
                        'contractPrice': contractPrice
                    }
                    ic(new_obj)
                    return new_obj

                    # self.ByUniversityAndEduTypes.append(new_obj)
            # return self.ByUniversityAndEduTypes
        else:
            ic(data)
            return None
    
    def return_typesByEduTypeAndDegree(self, eduTypeId, degreeId):
        data = typesByEduTypeAndDegree(self.token, eduTypeId, degreeId)
        if data is not None:
            for obj in data:
                name = obj['name']
                code = obj['code']
                new_obj = {
                    'name': name,
                    'code': code
                }
                return new_obj
            #     self.typesByEduTypeAndDegrees.append(new_obj)
            # return self.typesByEduTypeAndDegrees
        else:
            ic(data)
            return None
    
    def return_languages_by_edu_type(self, eduTypeId, degreeId, typeCode):
        data = languagesByEduType(self.token, eduTypeId, degreeId, typeCode)
        if data is not None:
            for obj in data:
                name = obj['name']
                id = obj['id']
                new_obj = {
                    'name': name,
                    'code': id
                }
                return new_obj
            #     self.languagesByEduTypes.append(new_obj)
            # return self.languagesByEduTypes
        else:
            ic(data)
            return None

    def return_by_edu_type_and_language_and_type(self, eduTypeId, lagaugeId, typeCode, degreeId):
        data = byEduTypeAndLanguageAndType(self.token, eduTypeId, lagaugeId, typeCode, degreeId)
        if data is not None:
            for obj in data:
                name = obj['name']
                id = obj['id']
                # new_obj = {
                #     'name': name,
                #     'id': id
                # }
                return id
            #     self.byEduTypeAndLanguageAndTypes.append(new_obj)
            # return self.byEduTypeAndLanguageAndTypes
        else:
            ic(data)
            return None


# def retrun_ContractID_directions(eduTypeName, degreeName, directionCode):
#     try:
#         university_typesId = University(token)
#         ic(eduTypeName, degreeName, directionCode, 'directionsga keldi 24')
#         res_degree = university_typesId.return_degrees(degreeName)
#         res_eduType = university_typesId.return_eduTypes(eduTypeName)
#         res_return_ByUniversityAndEduType = university_typesId.return_ByUniversityAndEduType(
#             res_eduType['code'],
#             res_degree['code'],
#             directionCode,
#             eduTypeName,
#             degreeName)
        
#         res_return_languagesByEduType = university_typesId.return_languagesByEduType(res_eduType['code'], res_degree['code'], 11)
#         res_return_byEduTypeAndLanguageAndType = university_typesId.return_byEduTypeAndLanguageAndType(
#             res_eduType['code'], 
#             res_return_languagesByEduType['code'],
#             11,
#             res_degree['code']
#         )
#         new_obj = {
#             "contractPriceId": res_return_ByUniversityAndEduType['contractPriceId'],
#             "checkingAccountId": res_return_ByUniversityAndEduType['checkingAccountId'],
#             "specialityName": res_return_ByUniversityAndEduType['specialityName'],
#             "contractPrice": res_return_ByUniversityAndEduType['contractPrice'],
#             "contractTemplateId": res_return_byEduTypeAndLanguageAndType
#         }
#         return new_obj
#     except Exception as err:
#         ic(err)

def return_contract_id_directions(edu_type_name, degree_name, direction_code):
    """
    Retrieves and constructs a contract ID data object based on educational type, degree, and direction code.

    Args:
    edu_type_name (str): The name of the education type.
    degree_name (str): The name of the degree.
    direction_code (str): The code for the direction.

    Returns:
    dict: A dictionary containing various contract details.
    """
    # try:
    university = University(token)  # Assuming `token` is defined elsewhere
    # Logging the input parameters
    ic(edu_type_name, degree_name, direction_code, 'directionsga keldi 24')  

    # Retrieve degree and educational type data
    res_degree = university.return_degrees(degree_name)
    res_edu_type = university.return_edu_types(edu_type_name)
    
    # Get data based on university and educational type
    contract_data = university.return_by_university_and_edu_type(
        res_edu_type['code'],
        res_degree['code'],
        direction_code,
        edu_type_name,
        degree_name)
    
    # Get language-related data
    languages_data = university.return_languages_by_edu_type(
        res_edu_type['code'], 
        res_degree['code'], 
        11)  # Assuming '11' is a fixed parameter
    edu_type_language_data = university.return_by_edu_type_and_language_and_type(
        res_edu_type['code'], 
        languages_data['code'],
        11,
        res_degree['code']
    )

    # Constructing the result object
    result = {
        "contractPriceId": contract_data['contractPriceId'],
        "checkingAccountId": contract_data['checkingAccountId'],
        "specialityName": contract_data['specialityName'],
        "contractPrice": contract_data['contractPrice'],
        "contractTemplateId": edu_type_language_data
    }
    ic(result)
    time.sleep(100)
    return result
    # except Exception as err:
    #     ic(err)  # Consider using proper logging instead of `ic` depending on the environment


    # eduTypeId_, degreeId_, educationLevelId_ = typesId(eduTypeId,degreeId)
    # ic(eduTypeId_, degreeId_, educationLevelId_, 'directionsga keldi 26')
    # url = "https://billing.e-edu.uz/api/classifier/speciality/byUniversityAndEduType"
    # params = {
    #     "eduTypeId": eduTypeId_,
    #     "degreeId": degreeId_,
    #     "educationLevelId": educationLevelId_
    # }
    # # ic(token)
    # headers = {
    #     "Authorization": f"Bearer {token}"
    # }
    
    # try:
    #     response = requests.get(url, params=params, headers=headers)
    #     response.raise_for_status()
    #     time.sleep(1)
        
    #     try:
    #         data = response.json()
    #         if len(data) != 0:
    #             for obj in data:
    #                 ic('keldi 47')
    #                 contractPrice = obj['contractPrice']
    #                 contractPriceId = obj['contractPriceId']
    #                 degreeName = obj['degreeName']
    #                 eduTypeName = obj['eduTypeName']
    #                 specialityName = obj['specialityName']
    #                 specialityCode = obj['specialityCode']
    #                 checkingAccountId = obj['checkingAccountId'] if obj['checkingAccountId'] else None
    #                 # ic(eduTypeId ,' <--> ', eduTypeName, ' -- ',degreeId, ' <--> ', degreeName, ' -- ', specialityCode, ' <--> ', directionCode)
    #                 if eduTypeId == degreeName and degreeId == eduTypeName and int(specialityCode) == int(directionCode):
    #                     # ic(contractPrice, contractPriceId, specialityName, 'yuborildi')
    #                     return {
    #                         "contractPrice": int(contractPrice), 
    #                         "contractPriceId":contractPriceId, 
    #                         "specialityName":specialityName,
    #                         "checkingAccountId":int(checkingAccountId)
    #                         }
    #         else:
    #             ic("Error: No data found")
    #             return None, None, None
                
    #     except ValueError:
    #         ic("Error: Unable to parse JSON response")
    #         return None, None, None
    
    # except requests.exceptions.HTTPError as http_err:
    #     ic(f"HTTP error occurred: {http_err}")
    # except requests.exceptions.RequestException as req_err:
    #     ic(f"Request error occurred: {req_err}")

# directions(11, 11, 11)
def eduTypeAndLanguageAndType(token, eduType, lagaugeId, typeCode, degreeId):
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
        if len(data) > 0:
            data = data[0]
            return data['id']

        return data
    else:
        ic(f"Error: {response.status_code}")
        return None

data = eduTypeAndLanguageAndType(token, 12, 11, 11, 11)
print(data)