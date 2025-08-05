user_info = {
    "username": "Larka",
    "password": "BatsAreDamnCute",
    "phone_number": "+4930901820"
}

items = {
    "date": "03/12/2023",
    "item": "",
    "total": "",
    "weight": "",
    "quantity": ""
}

print(" "*15,"-"*29)
print(" "*15,"|   Amazon Expense Report   |")
print(" "*15,"-"*29)
print(f"name: {user_info["username"]}"," "*4,
      "password: ***"," "*4,
      "Tel: +49***"+user_info["phone_number"][-2:])
print(f"Date: {items["date"]}")
print("-"*60)