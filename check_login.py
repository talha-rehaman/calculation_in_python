def login_required(func):
    def wrapper(*args):
        username,password = args
        if username == "admin" and password == "password":
            print("Login successful ✅")
            
            func(*args)
        else:
            print("Login failed ❌")    
    return wrapper
@login_required
def login(username,password):
    print(f"Welcome {username}!")

@login_required
def access_dashboard(username,password):
    if username == "admin" and password == "password":
        print("Access granted to dashboard ✅")
    else:
        print("Access denied to dashboard ❌")
login("admin","password")  # ✅
access_dashboard("admin","password")  # ✅