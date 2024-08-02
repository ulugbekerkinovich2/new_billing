import requests
from icecream import ic

import uuid
import pandas as pd
from sign_in import signIn
token = signIn()
class Contract:
    def __init__(self):
        self.token = token
        self.file_name_1 = uuid.uuid4()
        self.file_name_2 = uuid.uuid4()
        self.page = 1
        self.size = 1000000000

    def getContract(self, pinfl):
        totalElements, id_ = self.__allContracts(self.page, self.size, pinfl)
        if id_ is None:
            newTotalElements, id__ = self.__allContracts(self.page, totalElements, pinfl)
            if id__ is None:
                ic('__id not found')
                return None
            else:
                return self.__fetchContractUrl(id__)
        else:
            return self.__fetchContractUrl(id_)

    def __allContracts(self, page, size, pinfl):
        url = f"https://billing.e-edu.uz/api/adminService/allContracts?page={page}&size={size}&eduTypeId="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        try:
            if response.status_code == 200:
                data = response.json()
                content = data.get('content', [])
                totalElements = data.get('totalElements', 0)
                for obj in content:
                    if str(obj.get('pinfl')) == str(pinfl):
                        return totalElements, obj.get('id')
                return totalElements, None
            else:
                ic(f"Error: {response.status_code}")
                return None, None
        except Exception as e:
            ic(f"Error: {e}")
            return None, None
    def checkContract(self, pinfl):
        url = f"https://billing.e-edu.uz/api/adminService/allContracts?page={self.page}&size={self.size}&eduTypeId="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        try:
            if response.status_code == 200:
                data = response.json()
                content = data.get('content', [])
                for obj in content:
                    app_pinfl = str(obj.get('pinfl'))
                    applicationStatus = obj['applicationStatus']

                    if app_pinfl == str(pinfl) and applicationStatus == "Tasdiqlangan":
                        ic(applicationStatus, app_pinfl)
                        return obj['contractUrl']
                else:
                    return False
            else:
                return None, None
        except Exception as e:
            ic(f"Error: {e}")
            return None, None
    def __fetchContractUrl(self, id_):
        url = f"https://billing.e-edu.uz/api/applicant/contract/{int(id_)}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            contractUrl = data.get('contractUrl')
            if contractUrl:
                return contractUrl
            else:
                ic('Contract URL not found')
                return None
        else:
            ic('Failed to fetch contract URL')
            return None

    def make_json(self, array):
        import json
        filename = f'{self.file_name_1}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(array, f, ensure_ascii=False, indent=4)
    def make_excel(self, array):
        df = pd.DataFrame(array)
        filename = f'{self.file_name_1}.xlsx'
        df.to_excel(filename, index=False)