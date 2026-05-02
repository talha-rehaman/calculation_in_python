request_count = 0

def rate_limit(func):
    def check(*args):
        global request_count
        request_count += 1
        if request_count > 3:
            print("Bohot zyada requests! Thodi der baad try karo ❌")
            return
        func(*args)
    return check

@rate_limit
def search(query):
    print(f"Search: {query} ✅")

search("Python")    # ✅
search("Django")    # ✅
search("Laravel")   # ✅
search("React")     # ❌ Limit aa gayi