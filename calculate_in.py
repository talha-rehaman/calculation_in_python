class calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
cal =calculator()
print(cal.divide(10,5))