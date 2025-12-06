import requests

url = "https://seatable-gflt.onrender.com/webhook"

payload = {
    'columns_list': [
        {'name': 'Roll_No', 'type': 'number'},
        {'name': 'Candidate Last Name', 'type': 'text'},
        {'name': 'Degree/Dept', 'type': 'text'},
        {'name': 'Select Year of Passing', 'type': 'number'},
        {'name': 'Nationality', 'type': 'text'},
        {'name': 'num', 'type': 'number'}
    ],
    'table_name': 'A4Zi',
    'query': "add all num column"

}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

# Convert API response → Python dict
data = response.json()

print("Status:", data.get("status"))
print("SQL:", data.get("sql"))
print("Message:", data.get("message"))
