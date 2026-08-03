import re

text = "My email is student123@gmail.com and my phone number is 9876543210."

# Search Email
email = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)

# Search Phone Number
phone = re.search(r'\b[6-9]\d{9}\b', text)

if email:
    print("Email Found:", email.group())

if phone:
    print("Phone Number Found:", phone.group())
