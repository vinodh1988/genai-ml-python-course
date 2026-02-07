# ===== SINGLE INHERITANCE =====
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        print(Animal.speak(self))  # Call parent method (optional)
        return "Woof!"


# ===== MULTIPLE INHERITANCE =====
class Swimmer:
    def swim(self):
        return "Swimming..."
    def speak(self):
        return "I can swim but I don't speak!"

class Flyer:
    def fly(self):
        return "Flying..."
    def speak(self):
        return "I can fly but I don't speak!"

class Duck(Swimmer, Flyer):
    def speak(self):
        print(Swimmer.speak(self))  # Call Swimmer's speak
        print(Flyer.speak(self))    # Call Flyer's speak
        return "Quack!"


# ===== DEMONSTRATION =====
if __name__ == "__main__":
    # Single inheritance
    print("=== Single Inheritance ===")
    dog = Dog()
    print(dog.speak())  # Output: Woof!
    
    # Multiple inheritance
    print("\n=== Multiple Inheritance ===")
    duck = Duck()
    print(duck.speak())   # Output: Quack!
    print(duck.swim())    # Output: Swimming...
    print(duck.fly())     # Output: Flying...
    
    # MRO (Method Resolution Order)
    print("\n=== MRO for Duck ===")
    print(Duck.__mro__)