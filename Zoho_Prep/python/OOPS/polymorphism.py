class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Boow!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

def animal_sound(animal):
    return animal.speak()

print("Dog says: ", animal_sound(dog))
print("Cat says: ", animal_sound(cat))