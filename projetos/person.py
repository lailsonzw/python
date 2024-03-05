from os import system

class person: 
    name = None
    age = None

    def speak(self):
        print(f'Hello, world my fristname is {self.name}!')
        
    def speakage(self):
        print(f'My age is {self.age}.\n')
    

person1 = person()
person2 = person()

person1.name = 'lailson'
person2.name = 'luiz'

person1.age = 18
person2.age = 17

system('clear')
person1.speak()
person1.speakage()

person2.speak()
person2.speakage()