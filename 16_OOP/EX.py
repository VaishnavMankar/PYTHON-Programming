# 1. Define the class (the blueprint)
class Dog:
    # The __init__ method is the constructor. It runs when a new object is created.
    # 'self' refers to the specific instance of the class (the dog being created).
    def __init__(self, name, breed, age):
        # Attributes: data associated with each dog object
        self.name = name
        self.breed = breed
        self.age = age
        print(f"{self.name} the {self.breed} has been created!")

    # A method: a function that belongs to the class
    def bark(self):
        print(f"{self.name} says: Woof!  Woof!")

    # Another method that uses the object's attributes
    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")
    
    # A method that modifies an attribute
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old. 🎂")


# 2. Create objects (instances) of the Dog class
print("--- Creating our dogs ---")
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Lucy", "Poodle", 5)

print("\n--- Let's see what our dogs can do ---")

# 3. Use the objects' attributes and methods
dog1.display_info()
dog2.display_info()

print("\n--- Calling the bark method ---")
dog1.bark()
dog2.bark()

print("\n--- It's Buddy's birthday! ---")
dog1.celebrate_birthday()

print("\n--- Final check on Buddy's age ---")
dog1.display_info()