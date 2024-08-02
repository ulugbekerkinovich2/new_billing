from GetContract import Contract
import pandas as pd 
myCotract = Contract()
arr = [
    {
        "Applicant Id": "crm11008",
        "Full Name": "ZARINA NURULLOYEVA VOXID QIZI",
        "Phone Number": 998940089978,
        "Additional Number": "+998 94 014 09 03",
        "Personal Email": None,
        "Degree": "Magistr",
        "Direction Code": 70111801,
        "Department": "Xorijiy til va adabiyoti:  ingliz tili (magistratura)",
        "Education Language": "O'zbek tili",
        "Education Type": "Kunduzgi",
        "Passport": "AC0442201",
        "Pin": 60901035360012,
        "Gender": "2",
        "Birth Date": "09.01.2003",
        "Region": "BUXORO VILOYATI",
        "Photo": "https://crmapi.mentalaba.uz//avatar/d58d22bd-5d58-4bb7-a611-e83d2c7f2849.jpg",
        "Certificates": None,
        "Status": "accepted",
        "Contract Url": "https://billing.e-edu.uz/api/public/download/contract-o8AP9B4U.pdf"
    },
    {
        "Applicant Id": "crm11008",
        "Full Name": "ZARINA NURULLOYEVA VOXID QIZI",
        "Phone Number": 998940089978,
        "Additional Number": "+998 94 014 09 03",
        "Personal Email": None,
        "Degree": "Magistr",
        "Direction Code": 70111801,
        "Department": "Xorijiy til va adabiyoti:  ingliz tili (magistratura)",
        "Education Language": "O'zbek tili",
        "Education Type": "Kunduzgi",
        "Passport": "AC0442201",
        "Pin": 60901035360012,
        "Gender": "2",
        "Birth Date": "09.01.2003",
        "Region": "BUXORO VILOYATI",
        "Photo": "https://crmapi.mentalaba.uz//avatar/d58d22bd-5d58-4bb7-a611-e83d2c7f2849.jpg",
        "Certificates": None,
        "Status": "accepted",
        "Contract Url": "https://billing.e-edu.uz/api/public/download/contract-o8AP9B4U.pdf"
    }
]
myCotract.make_excel(arr)