import json
import pandas as pd
import os
import time
from icecream import ic
from tqdm import tqdm
# from sign_in import signIn
import datetime

from converter import excel_to_json
# from user_info import userInfo
# from directions import directions
# from contract import contractWithoutApp
# from GetContract import Contract
import stat

# token = signIn()

contract_template_id=10  #TODO AIFU uchun
ic(contract_template_id)
excel_file_path = 'AIFU_26_07_new.xlsx'
json_file_path = 'AIFU_26_07_new.json'

def check_user(array, application_id):
    for item in array:
        if item['Applicant Id'] == application_id:
            return False
    return True
    

with open("data.json", 'r', encoding='utf-8') as json_file:
    data_obj = json.load(json_file)

def find_by_pnfl(pinfl):
    for item in data_obj:
        if str(item['pinfl']) == str(pinfl):
            ic(item)
            return item['contractUrl']
    return None

# Convert Excel to JSON
excel_to_json(excel_file_path, json_file_path)

array = []
extra_array = []

def save_to_json_and_excel(array, json_file_path, excel_file_path):
    temp_json_file = f"{json_file_path}_result_temp2.json"
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

        os.chmod(f"{excel_file_path}_result.xlsx", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
    except PermissionError as e:
        ic(f"Permission error while saving Excel: {e}")
        return

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    try:
        for item in tqdm(data):
            Application_id = item.get('Applicant Id')
            fullname = item.get('Full Name', '').upper() if item.get('Full Name') else 'topilmadi'
            ic('----------------->', Application_id)
            phone = item.get('Phone Number')
            additional_phone = item.get('Additional Number')
            personal_email = item.get('Personal Email')
            degree = item.get('Degree')
            direction = item.get('Department')
            direction_code = item.get('Direction Code')
            education_language = item.get('Education Language')
            passport = item.get('Passport')
            pin = item.get('Pin')
            gender = item.get('Gender')
            ic(item.get('Birth Date'))
            birth_date2 = item.get('Birth Date')
            
            if "." not in birth_date2:
                birth_date_demo = item.get('Birth Date')
                timestamp_s = birth_date_demo / 1000

            # Convert to datetime
                birth_date = datetime.datetime.fromtimestamp(timestamp_s)
                birth_date1 = birth_date.strftime('%Y.%m.%d')
                ic(birth_date1)
                birth_date2 = '-'.join(reversed(birth_date1.split('.')))
            birth_date = birth_date2
            # birth_date2 = '-'.join(reversed(item.get('Birth Date').split('.')))

            # ic(birth_date)
            # break
            region = item.get('Region')
            education_type = item.get('Education Type')
            Photo = item.get('Photo')
            Certificates = item.get('Certificates')
            Status = item.get('Status')
            # getUrlContract = Contract
            if pin == "topilmadi":
                continue
            url = find_by_pnfl(pin)
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
                    "Contract Url": url if url else None
                        }
            array.append(new_obj)
            save_to_json_and_excel(array, json_file_path, excel_file_path)
    except Exception as e:
        ic(e)
        ic(item)