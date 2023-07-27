#!/usr/bin/env python
# coding: utf-8

# #1. Explain what inheritance is in object-oriented programming and why it is used.
# Ans:In object-oriented programming (OOP), inheritance is a mechanism that allows a class to inherit the properties and behaviors (methods) of another class. The class that inherits is called the subclass or derived class, and the class from which it inherits is called the superclass or base class. The subclass extends or specializes the functionality of the superclass, adding new features or overriding existing ones.
# 
# Inheritance is used to establish a hierarchical relationship between classes, creating a parent-child relationship. It promotes code reusability and modularity, as it allows common attributes and behaviors to be defined in a superclass and then inherited by multiple subclasses. This way, subclasses can inherit and utilize the code from the superclass, eliminating the need to rewrite or duplicate code.
# 
# The key benefits of inheritance include:
# 
# Code reuse: Inheritance enables subclasses to inherit the properties and methods of the superclass. This reduces code duplication and promotes a more efficient and organized development process. Common functionalities can be defined in the superclass, and the subclasses can inherit and extend them as needed.
# 
# Modularity: Inheritance enhances the modular design of software systems. It allows classes to be structured in a hierarchical manner, where each class represents a specific level of abstraction. This modular structure makes the codebase easier to understand, maintain, and update.
# 
# Polymorphism: Inheritance is closely related to the concept of polymorphism, which allows objects of different classes to be treated as instances of a common superclass. This enables the use of a single interface to represent multiple related objects, promoting flexibility and extensibility in the code.
# 
# Encapsulation: Inheritance helps in achieving encapsulation, one of the fundamental principles of OOP. By encapsulating related attributes and behaviors within classes, inheritance allows for better organization, data hiding, and separation of concerns. Changes made to the superclass can be localized and affect all the subclasses that inherit from it.
# 
# inheritance is a powerful feature of object-oriented programming that facilitates code reuse, modularity, polymorphism, and encapsulation. By establishing hierarchical relationships between classes, it promotes efficient development, maintenance, and extensibility of software systems.

# #2.Discuss the concept of single inheritance and multiple inheritance, highlighting their differences and advantages.
# Ans.In object-oriented programming, both single inheritance and multiple inheritance are mechanisms that allow a class to inherit properties and behaviors from other classes. However, they differ in the number of superclasses a subclass can inherit from.
# 
# 1.Single Inheritance: Single inheritance is a concept where a subclass can inherit from only one superclass. This means that a subclass can have one direct parent class, and it inherits the properties and behaviors defined in that superclass. The superclass can, in turn, have its own superclass, creating a single linear hierarchy.
# 
# Advantages of Single Inheritance:
# 
# :Simplicity: Single inheritance simplifies the class hierarchy by enforcing a clear and straightforward relationship between classes. It avoids complexities that can arise from multiple superclasses with potential conflicts or ambiguity.
# 
# :Ease of maintenance: With a linear class hierarchy, it is generally easier to understand, maintain, and debug the codebase. Changes made to the superclass are localized and have a limited impact on the subclass.
# 
# 2.Multiple Inheritance: Multiple inheritance allows a subclass to inherit from multiple superclasses, enabling it to acquire properties and behaviors from multiple sources. This means that a subclass can have multiple direct parent classes, and it inherits the characteristics defined in all of those superclasses.
# 
# Advantages of Multiple Inheritance:
# 
# Code reuse and flexibility: Multiple inheritance enables greater code reuse by inheriting functionality from multiple superclasses. This promotes modular design and allows the subclass to combine features from different sources, making it more flexible and adaptable.
# 
# Expressive power: Multiple inheritance can model complex relationships and scenarios more accurately. It allows the creation of classes that combine traits and behaviors from various parent classes, providing a richer and more expressive representation of real-world objects or concepts.
# 
# However, multiple inheritance also brings certain challenges and concerns:
# 
# Name clashes: If multiple superclasses define methods or attributes with the same name, conflicts may arise. This can result in ambiguity, and the programmer needs to handle these conflicts explicitly.
# 
# Increased complexity: With multiple superclasses, the class hierarchy becomes more intricate, which can make the code harder to understand and maintain. It may require careful consideration and design decisions to avoid confusion and potential pitfalls.
# 
# Diamond problem: The diamond problem occurs when a subclass inherits from two superclasses, both of which inherit from a common superclass. This can lead to ambiguity in method resolution, as the subclass does not know which superclass's method to use. Programming languages handle this problem differently, providing mechanisms like method overriding or virtual inheritance to resolve it.
# 
# It's worth noting that while single and multiple inheritance have their differences and advantages, some programming languages support only single inheritance (e.g., Java), while others allow multiple inheritance (e.g., C++). Some languages provide alternative mechanisms, like interfaces or mixins, to achieve similar goals without the complexities of multiple inheritance. The choice between single and multiple inheritance depends on the specific requirements, design considerations, and language capabilities in a given programming context.

# #3.Explain the terms "base class" and "derived class" in the context of inheritance.
# A.In the context of inheritance, the terms "base class" and "derived class" are used to describe the relationship between classes.
# 
# 1.Base Class: A base class, also known as a superclass or parent class, is the class from which other classes inherit properties and behaviors. It serves as the starting point or foundation for creating derived classes. The base class defines common attributes and methods that are shared by multiple related classes.
# 
# In terms of inheritance, the base class is the class that is extended or specialized by other classes. It contains the essential functionality that can be inherited by its derived classes. The base class can have its own base class, creating a hierarchical chain of inheritance.
# 
# For example, consider a base class called "Animal" that defines common attributes and behaviors of animals, such as "name" and "eat()". Other classes like "Dog" and "Cat" can inherit from the "Animal" class, gaining its properties and methods.
# 
# 2.Derived Class: A derived class, also known as a subclass or child class, is a class that inherits properties and behaviors from a base class. It extends or modifies the functionality of the base class by adding new features or overriding existing ones. The derived class is created by specifying the base class from which it inherits.
# 
# Inheritance allows the derived class to inherit all the non-private members (attributes and methods) of the base class. It can access and utilize the inherited members directly, as if they were defined within the derived class itself. Additionally, the derived class can introduce its own specific attributes and behaviors.
# 
# Continuing with the previous example, the "Dog" and "Cat" classes are derived classes from the "Animal" base class. They inherit the common attributes and methods defined in the "Animal" class, such as "name" and "eat()". The derived classes can further define their own specific attributes and behaviors, such as "bark()" in the "Dog" class and "meow()" in the "Cat" class.
# 
# The base class is the class that is inherited from, providing a foundation of shared functionality. The derived class is the class that inherits from the base class, extending or modifying the inherited functionality while adding its own unique characteristics.

# #4.What is the significance of the "protected" access modifier in inheritance? How does it differ from "private" and "public" modifiers?
# A.Inheritance and access modifiers play a crucial role in encapsulation and controlling the visibility of members (attributes and methods) in object-oriented programming. The "protected" access modifier has a specific significance in the context of inheritance, and it differs from the "private" and "public" modifiers in the following ways:
# 
# 1.Private Access Modifier: The "private" access modifier restricts the visibility of a member to only the class in which it is defined. It prevents access to the member from any other class, including derived classes. Private members are encapsulated within the class, and they cannot be inherited or accessed directly by subclasses.
# 
# 2.Protected Access Modifier: The "protected" access modifier allows the visibility of a member within the class in which it is defined, as well as in its derived classes. Protected members are accessible by the class itself and any subclasses that inherit from it. This means that protected members can be inherited, accessed, and utilized by derived classes, but they remain hidden from other classes outside the inheritance hierarchy.
# 
# The significance of the "protected" access modifier in inheritance can be summarized as follows:
# 
# Inheritance and Code Reuse: Protected members enable code reuse by allowing derived classes to access and utilize the inherited members. This promotes the reuse of common functionality defined in the base class within its derived classes, enhancing code modularity and reducing duplication.
# 
# Encapsulation and Controlled Access: By using the "protected" modifier, a class can expose certain members to its derived classes while still encapsulating them from external classes. This helps in maintaining the integrity of the class's internal implementation, as the protected members are hidden from unrelated classes.
# 
# 3.Public Access Modifier: The "public" access modifier provides the widest visibility for members. Public members are accessible from any class, including derived classes, as well as from code outside the class hierarchy. Public members are not limited to inheritance and can be accessed directly by any other class.
# 
# To summarize the differences:
# 
# Private members are only accessible within the class itself and are not inherited or accessible by derived classes. :Protected members are accessible within the class itself and its derived classes, allowing for code reuse and controlled access. :Public members have the broadest visibility and can be accessed by any class, whether it is a derived class or not.
# 
# The choice of access modifier depends on the desired level of encapsulation, information hiding, and the intended visibility of members to other classes, particularly in the context of inheritance.

# #5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# Ans:The "super" keyword in inheritance is used to call a method from the parent class (superclass) within the child class (subclass). It allows the child class to access and utilize the functionalities of the parent class. This is particularly useful when you want to override a method in the child class while still retaining some of the behavior from the parent class.
# 
# Let's provide an example in Python to illustrate the use of the "super" keyword:
# 
# Suppose we have a parent class called Animal, which has a method called make_sound() that prints the sound of the animal. We will then create a child class called Dog, which will inherit from the Animal class but override the make_sound() method to print a specific sound for dogs.

# In[5]:


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

# Creating an instance of the Dog class
dog_instance = Dog("Buddy", "Labrador")

# Calling the make_sound() method of the Dog class
dog_instance.make_sound()


# In this example, we have two classes, Animal and Dog. The Dog class inherits from the Animal class. We use the super() function in the __init__ method of the Dog class to call the __init__ method of the parent class, Animal, and initialize the name attribute. This allows us to reuse the code from the Animal class.
# 
# Similarly, the make_sound() method in the Dog class overrides the make_sound() method of the Animal class. However, if we still want to use the functionality of the Animal class and print a generic animal sound, we can use the super().make_sound() statement inside the make_sound() method of the Dog class. This way, when we call dog_instance.make_sound(), it prints "Woof!" (from the Dog class) and not "Generic animal sound" (from the Animal class).

# #6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
# Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
# attribute called "fuel_type". Implement appropriate methods in both classes.
# 

# In[6]:


# Define the base class "Vehicle"
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Define the derived class "Car" that inherits from "Vehicle"
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        # Call the display_info() method of the base class and then add fuel_type information
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Test the classes
if __name__ == "__main__":
    # Create a Vehicle instance
    vehicle1 = Vehicle("Brand", "ModelX", 2022)
    vehicle1.display_info()

    # Create a Car instance
    car1 = Car("Toyota", "Camry", 2023, "Gasoline")
    car1.display_info()


# Explanation:
# 
# We first create the base class Vehicle with the make, model, and year attributes. It also has a method display_info() that prints the information about the vehicle.
# Next, we create the derived class Car that inherits from the Vehicle class. The Car class adds an additional attribute fuel_type and overrides the display_info() method to also display the fuel type.
# In the Car class, we use the super() function to call the __init__() method of the base class (Vehicle) to initialize the common attributes (make, model, and year).
# We then test the classes by creating instances of both Vehicle and Car classes and calling their display_info() methods to check if the information is displayed correctly.

# #7. Create a base class called "Employee" with attributes like "name" and "salary."
# Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
# attribute called "department" for the "Manager" class and "programming_language"
# for the "Developer" class.

# In[8]:


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Manager class
    manager = Manager("Gowtami Devarenti", 75000, "HR")

    # Creating an instance of the Developer class
    developer = Developer("Mayookha Bhumireddy", 65000, "Python")

    # Accessing attributes
    print(f"Manager: {manager.name}, Salary: ${manager.salary}, Department: {manager.department}")
    print(f"Developer: {developer.name}, Salary: ${developer.salary}, Programming Language: {developer.programming_language}")


# #8. Design a base class called "Shape" with attributes like "colour" and "border_width."
# Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
# specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
# the "Circle" class.
# Ans:To implement the above requirements, we'll create a Python script with a base class called "Shape" and two derived classes, "Rectangle" and "Circle." We'll add attributes to each class as specified in the guidelines.
# 
# Here's the Python code for the implementation:

# In[10]:


class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print(f"Colour: {self.colour}, Border Width: {self.border_width}")


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}, Width: {self.width}")

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"Radius: {self.radius}")

    def area(self):
        import math
        return math.pi * self.radius ** 2


# Testing the classes
if __name__ == "__main__":
    # Creating instances of Rectangle and Circle
    rect = Rectangle("Blue", 2, 5, 10)
    circle = Circle("Red", 1, 7)

    # Displaying information and calculating area
    print("Rectangle Information:")
    rect.display_info()
    print("Rectangle Area:", rect.area())

    print("\nCircle Information:")
    circle.display_info()
    print("Circle Area:", circle.area())


# Explanation:
# 
# We define the Shape class with attributes colour and border_width. It has a method display_info() to display the shape's information.
# The Rectangle class is derived from the Shape class and has additional attributes length and width. It also overrides the display_info() method to include its specific information and defines an area() method to calculate the area of the rectangle.
# The Circle class is also derived from the Shape class and has an additional attribute radius. It overrides the display_info() method to include its specific information and defines an area() method to calculate the area of the circle.

# #9. Create a base class called "Device" with attributes like "brand" and "model." Derive
# two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
# "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.
# Ans:
# Sure, here's the Python code for the classes "Device," "Phone," and "Tablet" following the given guidelines:

# In[12]:


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
# Create instances of Phone and Tablet classes
phone1 = Phone("Apple", "iPhone X", 6.1)
tablet1 = Tablet("Samsung", "Galaxy Tab S7", 8000)

# Accessing attributes
print(f"Phone: {phone1.brand} {phone1.model}, Screen Size: {phone1.screen_size} inches")
print(f"Tablet: {tablet1.brand} {tablet1.model}, Battery Capacity: {tablet1.battery_capacity} mAh")


# Explanation:
# 
# We created a base class called Device with attributes brand and model. The __init__ method initializes these attributes when an instance of the class is created.
# 
# The Phone class is derived from the Device class using inheritance. It has an additional attribute screen_size specific to the phone.
# 
# The Tablet class is also derived from the Device class and has an additional attribute battery_capacity specific to the tablet.
# 
# With this implementation, you can create instances of the Phone and Tablet classes, and they will have access to the attributes of the base class Device as well as their specific attributes.

# #10. Create a base class called "BankAccount" with attributes like "account_number" and
# "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
# "BankAccount." Add specific methods like "calculate_interest" for the
# "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

# In[13]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.05

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.fees = 0.01

    def deduct_fees(self):
        fees = self.balance * self.fees
        self.balance -= fees
        return fees


# Test the implementation
if __name__ == "__main__":
    # Create SavingsAccount instance
    savings_account = SavingsAccount("SAV-123", 1000)
    savings_account.display_balance()
    interest = savings_account.calculate_interest()
    print(f"Interest earned: {interest}")
    savings_account.display_balance()

    # Create CheckingAccount instance
    checking_account = CheckingAccount("CHK-456", 2000)


# Explanation:
# 
# The BankAccount class serves as the base class, containing attributes account_number and balance. It has methods to deposit, withdraw, and display the account balance.
# 
# The SavingsAccount class is derived from BankAccount. It inherits the account_number and balance attributes and defines an additional attribute interest_rate. The calculate_interest method calculates the interest based on the balance and interest rate and adds it to the account balance.
# 
# The CheckingAccount class is also derived from BankAccount. It inherits the account_number and balance attributes and defines an additional attribute fees. The deduct_fees method calculates the fees based on the account balance and deducts it from the balance.
# 
# In the test section, we create instances of SavingsAccount and CheckingAccount to demonstrate the functionality of the classes. We call the calculate_interest method on the savings_account instance to calculate and add interest, and the deduct_fees method on the checking_account instance to deduct fees.
