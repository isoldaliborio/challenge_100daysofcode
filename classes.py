class Person:
    def __init__(self, msg, love):
        self.message = msg
        self.loved_one = love
        print("Eu estou sendo criada")
    
    def speak(self):
        print(f"Hello! {self.message}")
    
    def love(self):
        print(f"I love you {self.loved_one}!")


dudu = Person("My love!", "Isoldinha")
dudu.speak()
dudu.love()

isoldinha = Person("Darling", "Gordi")
isoldinha.love()
