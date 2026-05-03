class animals:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} bolti hai : {self.sound}")
animalsObject= animals("dog","bhow bhow")
animalsObject.speak()

cat = animals("Cat", "Meow Meow")
cat.speak()

