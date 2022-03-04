
class Dog:

    def __init__(self, weight, color, voice):
        self.weight = weight
        self.color = color
        self.voice = voice

    def voiceT(self):
        print(f'{self.voice}')

rex = Dog(20, "brown", "Gaf Gaf!")
rex.voiceT()

class Cat:
    def __init__(self, age, color, voice):
        self.age =age
        self.color =color
        self.voice =voice

    def voiceCat(self):
        print(f'{self.voice}')
masha = Cat(3, "blue", "Мяу Мяу!" )
masha.voiceCat()

class Cow:
    def __init__(self, weight, color, voice):
        self.weght = weight
        self.color = color
        self.voice = voice

    def voiceCow(self):
        print(f'{self.voice}')

marta = Cow(123, 'white', 'Muu Muu!')
marta.voiceCow()

class Bear:
    def __init__(self, weight, color, voice):
        self.weght = weight
        self.color = color
        self.voice = voice

    def voiceBear(self):
        print(f'{self.voice}')

marta = Bear(260, 'brown', 'Arr Arr!')
marta.voiceBear()

input()