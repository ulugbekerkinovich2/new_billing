import json
import pandas as pd
import os
import time
from icecream import ic
from converter import excel_to_json
from user_info import userInfo
from directions import directions
from contract import contractWithoutApp
from GetContract import Contract
import stat

excel_file_path = 'tavsiya_qilinganlar2.xlsx'
json_file_path = 'tavsiya_qilinganlar2.json'

# Convert Excel to JSON
excel_to_json(excel_file_path, json_file_path)

array = []
extra_array = []

def save_to_json_and_excel(array, json_file_path, excel_file_path):
    temp_json_file = f"{json_file_path}_result_temp.json"
    temp_excel_file = f"{excel_file_path}_result_temp.xlsx"
    
    # Save the array to a temporary JSON file
    try:
        with open(temp_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(array, json_file, indent=4, ensure_ascii=False)
        os.replace(temp_json_file, f"{json_file_path}_result.json")  # Atomically replace the old file

        # Set file permissions
        os.chmod(f"{json_file_path}_result.json", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
    except PermissionError as e:
        ic(f"Permission error while saving JSON: {e}")
        return

    # Convert the JSON file to a temporary Excel file
    try:
        df = pd.DataFrame(array)
        df.to_excel(temp_excel_file, index=False)
        os.replace(temp_excel_file, f"{excel_file_path}_result.xlsx")  # Atomically replace the old file

        # Set file permissions
        os.chmod(f"{excel_file_path}_result.xlsx", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
    except PermissionError as e:
        ic(f"Permission error while saving Excel: {e}")
        return

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    # time.sleep(1)
    try:
        for item in data:
            # ic(array, extra_array)
            Application_id = item.get('Applicant Id')
            fullname = item.get('Full Name', '').upper() if item.get('Full Name') else None
            phone = item.get('Phone Number')
            additional_phone = item.get('Additional Number')
            personal_email = item.get('Personal Email')
            degree = item.get('Degree')
            direction = item.get('Department')
            direction_code = item.get('Direction Code')
            education_language = item.get('Education Language')
            passport = item.get('Passport')
            pin = int(item.get('Pin', 0))
            gender = item.get('Gender')
            birth_date = item.get('Birth Date')
            region = item.get('Region')
            education_type = item.get('Education Type')
            Photo = item.get('Photo')
            Certificates = item.get('Certificates')
            Status = item.get('Status')

            dirs = directions(education_type, degree, direction_code)
            ic(dirs)
            contractPrice = dirs['contractPrice']
            contractPriceId = dirs['contractPriceId']
            specialityName = dirs['specialityName']
            ic(contractPrice, contractPriceId, specialityName)
            user_data = userInfo(pin, passport)
            if user_data:
                ic(user_data)
                address = user_data['address']
                admissionType = 'QABUL'
                birthDate = '.'.join(reversed(user_data['birthDate'].split('.')))
                citizenship = user_data['citizenship'].upper() if user_data['citizenship'] else None
                contractPriceId = contractPriceId
                contractSum = contractPrice
                contractTemplateId = 10
                country = user_data['country'].upper() if user_data['country'] else None
                district = user_data['district'].upper() if user_data['district'] else None
                dtmBall = user_data['dtmBall']
                dtmSpeciality = user_data['dtmSpeciality']
                eduFinishedRequest = None
                existInDTM = False
                fatherName = user_data['fatherName'].upper() if user_data['fatherName'] else None
                firstName = user_data['firstName'].upper() if user_data['firstName'] else None
                gender = str(user_data['gender'])
                givenDate = user_data['givenDate']
                lastName = user_data['lastName'].upper() if user_data['lastName'] else None
                monthId = 12
                nationality = user_data['nationality'].upper() if user_data['nationality'] else None
                passportExpireDate = user_data['passportExpireDate']
                phoneNumber = phone
                photo = user_data['photo']
                pinfl = pin 
                region = user_data['region'].upper() if user_data['region'] else None
                serialAndNumber = passport
                res = contractWithoutApp(
                    address,
                    admissionType,
                    birthDate, 
                    citizenship,
                    contractPriceId,
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
                    serialAndNumber
                )
                UserContract = Contract()
                if res:
                    contractUrl = UserContract.getContract(pinfl)
                    ic(contractUrl)
                    if contractUrl:
                        new_obj = {
                            "Applicant Id": Application_id,
                            "Full Name": fullname,
                            "Phone Number": phone,
                            "Additional Number": additional_phone,
                            "Personal Email" : personal_email,
                            "Degree": degree,
                            "Direction Code": direction_code,
                            "Department": direction,
                            "Education Language": education_language,
                            "Education Type": education_type,
                            "Passport": passport,
                            "Pin": pin,
                            "Gender": gender,
                            "Birth Date": birth_date,
                            "Region": region,
                            "Photo": Photo,
                            "Certificates": Certificates,
                            "Status": Status,
                            "Contract Url": contractUrl
                        }
                        array.append(new_obj)
                        save_to_json_and_excel(array, json_file_path, excel_file_path)
                else:
                    contractUrl = UserContract.getContract(pinfl)
                    if contractUrl:
                        ic(contractUrl)
                        new_obj = {
                            "Applicant Id": Application_id,
                            "Full Name": fullname,
                            "Phone Number": phone,
                            "Additional Number": additional_phone,
                            "Personal Email" : personal_email,
                            "Degree": degree,
                            "Direction Code": direction_code,
                            "Department": direction,
                            "Education Language": education_language,
                            "Education Type": education_type,
                            "Passport": passport,
                            "Pin": pin,
                            "Gender": gender,
                            "Birth Date": birth_date,
                            "Region": region,
                            "Photo": Photo,
                            "Certificates": Certificates,
                            "Status": Status,
                            "Contract Url": contractUrl
                        }
                        extra_array.append(new_obj)
                        save_to_json_and_excel(extra_array, json_file_path, excel_file_path)
                    else:
                        ic('Contract not found')
                        continue
                time.sleep(3)
            else:
                ic('user not found')
                continue
        ic('All done!')
    except Exception as e:
        ic(e)
