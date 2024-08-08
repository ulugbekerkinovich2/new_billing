from converter import excel_to_json
import json
import requests
from icecream import ic
import time
excell = "AIFU_barchasi.xlsx"
# json_f = "AIFU_barchasi.json"
json_f1 = "AIFU_08_08_oxirgisi.json_result.json"

# excel_to_json(excell, json_f)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzY0MiwiZmlyc3RfbmFtZSI6IkFuaXEgdmEgaWp0aW1vaXkgZmFubGFyIHVuaXZlcnNpdGV0aSIsImxhc3RfbmFtZSI6ImFkbWluLnVlc3MudXoiLCJiaXJ0aF9kYXRlIjpudWxsLCJwaG9uZSI6bnVsbCwicm9sZSI6InVuaXZlcnNpdHlfYWRtaW4iLCJhdmF0YXIiOiJsb2dvLzU1NWQ5YjRkLTg1YTAtNGY5Ni04NGRlLTBkNjY1MDY0MTRkNi5wbmciLCJlbWFpbCI6ImluZm9AYWlmdS51eiIsImlzX3ZlcmlmeSI6dHJ1ZSwiY3JlYXRlZF9hdCI6IjIwMjQtMDYtMDNUMDQ6NDg6NTguNjU2WiIsInVwZGF0ZWRfYXQiOiIyMDI0LTA2LTAzVDA0OjQ4OjU4LjY1NloiLCJhdXRoX2tleSI6bnVsbCwidGhpcmRfbmFtZSI6bnVsbCwiYWRtaW5fdHlwZSI6bnVsbCwicmVnaXN0cmF0aW9uX3R5cGUiOiJwaG9uZSIsInRvdGFsX2NhbGwiOm51bGwsImNhbl9zZWVfYWxsX2FwcGxpY2FudHMiOnRydWUsInVuaXZlcnNpdHlJZCI6NiwiaWF0IjoxNzIzMDkwNTEzLCJleHAiOjE3MjMxMzM3MTN9.sQqw6jV-etkFKK6_oJzkLG9JORScrXw1gN7xx2vOi58"
def update_status(_id, type):
    url = "https://crmapi.mentalaba.uz/v1/applicants/applicant"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    body = {
        "applicants_id": [int(_id)],
        "status": "contract",
        # "status": "came-exam",
        # "status": "recommended-student",
        "type": type
    }
    ic(body)
    response = requests.patch(url, json=body, headers=headers)
    if response.status_code == 200:
        print(f"Status updated for applicant_id: {_id}")


# def users():
#     url = "https://crmapi.mentalaba.uz/v1/applicants?offset=0&limit=2000&admission_year=2024&type=all&status=recommended-student&is_transfer_student=false&is_second_specialty=false"
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         entities = data['entities']
#         for entity in entities:
#             applicant_id = entity['applicant_id']

cont = 0
with open(json_f1, 'r', encoding='utf-8') as f:  # Corrected 'json_f' to a placeholder file name
    data = json.load(f)
    for obj in data:
        applicant_id = obj['Applicant Id']  # Use snake_case for variables
        pin = obj['Pin'] #
        # if pin is None:
        #     ic(pin, applicant_id)
        #     # time.sleep(200)
        #     if applicant_id.startswith("crm"):
        #         _id = applicant_id.split("crm")[-1]  # Get the part after 'crm'
        #         update_status(_id, "crm")
        #         cont += 1
        #     elif applicant_id.startswith("mt"):
        #         _id = applicant_id.split("mt")[-1]  
        #         update_status(_id, "mentalaba")
        #         cont += 1
            
        # elif pin is not None:
        #     continue
        Contract_Url = obj['Contract Url']
        ic(Contract_Url)
        if Contract_Url == "Bu fuqaroda tasdiqlangan ariza mavjud" and applicant_id.startswith("mt"):
            _id = applicant_id.split("mt")[-1]
            update_status(_id, "mentalaba")
            cont += 1
        elif Contract_Url == "Bu fuqaroda tasdiqlangan ariza mavjud" and applicant_id.startswith("crm"):
            _id = applicant_id.split("crm")[-1]
            update_status(_id, "crm")
            cont += 1
        
ic(cont)