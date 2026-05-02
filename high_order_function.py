def validate(func):
    def check(*args):
        name, email, phone = args
        
        if name == "":
            print("Naam empty hai ❌")
            return
        if "@" not in email:
            print("Email sahi nahi ❌")
            return
        if len(phone) != 11:
            print("Phone number sahi nahi ❌")
            return
        func(*args)
    return check

@validate
def submit_form(name, email, phone):
    print(f"Form submit ho gaya ✅")
    print(f"Name: {name}, Email: {email}, Phone: {phone}")

submit_form("Talha", "talha@gmail.com", "03001234567")  # ✅