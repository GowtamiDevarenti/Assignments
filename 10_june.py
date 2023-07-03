#!/usr/bin/env python
# coding: utf-8

# #1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
# example of each.
# ans:A built-in function is a function that is pre-defined in a programming language or software application. These functions are usually a part of the core functionality of the language or application and are available for use without the need to define them. Some examples of built-in functions in Python are len(), which returns the length of an object, and sum(), which calculates the sum of the elements in an iterable.
# A user-defined function, on the other hand, is a function that is defined by the user in their code. These functions are created to perform specific tasks and can be called upon whenever the need arises in the code. User-defined functions can also be referred to as custom functions or homemade functions. Some examples of user-defined functions in Python are:

# In[9]:


#Builtin function
my_string = "Hello, world!"
length = len(my_string)
print(length)  


# In[10]:


#User Defined functions
def multiply(a, b):
    return a * b

result = multiply(10, 3)
print(result)  


# #2. How can you pass arguments to a function in Python? Explain the difference between positional
# arguments and keyword arguments.
# ans:In Python, you can pass arguments to a function in several ways. The two main types of arguments are positional arguments and keyword arguments.
# 
# Positional Arguments:
# Positional arguments are passed to a function based on their position or order. The arguments are assigned to the function parameters in the order they are provided when calling the function.

# In[11]:


def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet("Alice", 25)


# Keyword Arguments:
# Keyword arguments are passed to a function using the names of the parameters. This allows you to specify which argument corresponds to which parameter, regardless of their order.

# In[12]:


def greet(name, age):
    print("Hello, " + name + "! You are " + str(age) + " years old.")

greet(age=25, name="Bob")


# Using keyword arguments provides more clarity and readability, especially when a function has multiple parameters or when you want to skip optional arguments and specify only the necessary ones.
# 
# Additionally, Python allows you to mix positional and keyword arguments. When doing so, the positional arguments must come first, followed by the keyword arguments.

# In[13]:


def greet(name, age, city):
    print("Hello, " + name + "! You are " + str(age) + " years old and live in " + city + ".")

greet("Alice", city="New York", age=25)


# To summarize, positional arguments are passed to a function based on their position, while keyword arguments are passed by specifying the parameter names. Mixing positional and keyword arguments is also allowed as long as the positional arguments come first.

# #3. What is the purpose of the return statement in a function? Can a function have multiple return
# statements? Explain with an example.
# ans:The return statement in a function serves the purpose of specifying the value that the function should output or return to the caller. When a return statement is encountered in a function, the function execution terminates, and the value specified after the return keyword is sent back as the result of the function.
# 
# The return statement allows functions to provide a result or output that can be further used or assigned to a variable, printed, or used in other computations.
# 
# A function can indeed have multiple return statements. However, when a return statement is executed, the function immediately exits, and no further code within the function is executed.
# 
# 

# In[14]:


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student_score = 85
grade = get_grade(student_score)
print("The grade is:", grade)


# It's important to note that once a return statement is encountered, the function exits, and any subsequent code in the function is not executed. Therefore, only one return statement will be executed in a given function call.

# #4. What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful.
# ans:In Python, lambda functions are small, anonymous functions that are defined using the lambda keyword. They are also known as lambda expressions. Unlike regular functions, lambda functions do not require a formal def statement and are typically used for simple, one-line functions.
# 
# Here is the general syntax of a lambda function:

# In[15]:


lambda arguments: expression


# Lambda functions can take any number of arguments, separated by commas, and have a single expression that is evaluated and returned as the result.
# 
# Lambda functions are different from regular functions in the following ways:
# 
# Anonymous: Lambda functions are anonymous, meaning they do not have a name. They are primarily used when you need a small, one-time function without the need for a formal function definition.
# 
# Concise: Lambda functions are typically written in a single line of code, making them concise and easy to write and understand.
# 
# Limited Scope: Lambda functions are limited in their functionality due to their simplicity. They are best suited for simple, one-line expressions and cannot contain complex statements or multiple lines of code.
# 
# Here's an example where a lambda function can be useful:

# In[22]:


# Regular function
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)  # Output: 12

# Equivalent lambda function
multiply_lambda = lambda a, b: a * b

result_lambda = multiply_lambda(3, 4)
print(result_lambda)  



# In[20]:


# Sorting a list of tuples based on the second element of each tuple
my_list = [(1, 5), (3, 1), (2, 3), (4, 2)]

# Sort the list based on the second element of each tuple
sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)


# Lambda functions are especially useful when you need a simple, one-time function and don't want to define a separate function using the def statement. They provide a concise way to express small, inline functions in Python.

# #5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.
# ans:In Python, "scope" refers to the region or context in which a variable or name is defined and can be accessed. The concept of scope applies to functions in Python, defining the visibility and accessibility of variables within the function.
# 
# Local Scope:
# Local scope refers to the variables that are defined within a specific function. These variables can only be accessed within that function and are not visible outside of it. Local variables are created when the function is called and destroyed when the function completes its execution.
# Here's an example to illustrate local scope:
# 

# In[23]:


def my_function():
    x = 10  # Local variable
    print(x)

my_function()  
print(x)  # Raises NameError: name 'x' is not defined


# Global Scope:
# Global scope refers to the variables that are defined outside of any function, at the top level of the script or module. These variables can be accessed from any part of the code, including inside functions. Global variables persist throughout the execution of the program.
# Here's an example to illustrate global scope:

# In[24]:


x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)  # Output: 10


# It's important to note that if a variable is assigned a value within a function, Python considers it as a local variable unless explicitly declared as a global variable using the global keyword. This ensures that the variable is treated as a global variable and retains its value outside of the function.

# In[25]:


x = 10  # Global variable

def my_function():
    global x  # Declaring x as a global variable
    x = 20  # Modifying the global variable
    print(x)

my_function()  
print(x)  


# To summarize, local scope refers to variables defined within a specific function, which are accessible only within that function. Global scope refers to variables defined outside of any function, which can be accessed from anywhere in the code. The global keyword is used to explicitly declare a variable as a global variable within a function.

# #6. How can you use the "return" statement in a Python function to return multiple values?
# ans:In Python, you can use the "return" statement in a function to return multiple values by separating them with commas. The values can be of any data type, such as integers, strings, lists, or even other objects. Here's an example:

# In[26]:


def get_values():
    value1 = 10
    value2 = "Hello"
    value3 = [1, 2, 3]
    return value1, value2, value3

result1, result2, result3 = get_values()

print(result1)  
print(result2)  
print(result3)  


# Note that when using multiple return values, they are actually returned as a tuple. Therefore, you can also assign the returned values to a single variable as a tuple, and access individual values using indexing, like this:

# In[28]:


result = get_values()
print(result[0])  
print(result[1])  
print(result[2])  


# However, using multiple assignment as shown in the first example is more common and convenient when you want to store each returned value in a separate variable.

# #7. What is the difference between the "pass by value" and "pass by reference" concepts when it
# comes to function arguments in Python?
# ans:When it comes to function arguments in Python, the behavior is often described as "pass by assignment" or "pass by object reference." Let's understand the two concepts:
# 
# Pass by Value:
# In "pass by value," the value of the variable is passed to the function. This means that any changes made to the function parameter inside the function do not affect the original variable outside the function. In other words, a copy of the value is passed to the function, and any modifications made to the parameter inside the function are only applicable within the scope of the function.
# 

# In[30]:


def increment(num):
    num += 1

value = 5
increment(value)
print(value)


# In this example, the increment function takes a parameter num and increments it by 1. However, the original value of value remains unchanged because the function receives a copy of the value, not the reference to the original variable.

# Pass by Reference (or Pass by Object Reference):
# In Python, everything is an object, and variables hold references to objects. When you pass an object as an argument to a function, a reference to that object is passed. This means that modifications made to the parameter inside the function can affect the original object outside the function.

# In[32]:


def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  


# It's important to note that although Python uses "pass by object reference," it does not allow reassigning the reference itself. This means that you cannot change what object a variable refers to within a function, only its internal state.
# 
# Understanding the "pass by assignment" concept in Python helps clarify the behavior of function arguments, where modifications to mutable objects (like lists) can affect the original object, while reassigning the reference to an object does not affect the original variable.

# #8. Create a function that can intake integer or decimal value and do following operations:
# a. Logarithmic function (log x)
# b. Exponential function (exp(x))
# c. Power function with base 2 (2x)
# d. Square root
# 
# ans:Here's a Python function that can perform the logarithmic, exponential, power (with base 2), and square root operations based on the input value:

# In[33]:


import math

def perform_operations(value):
    logarithmic_result = math.log(value)
    exponential_result = math.exp(value)
    power_result = math.pow(2, value)
    square_root_result = math.sqrt(value)
    
    return logarithmic_result, exponential_result, power_result, square_root_result

# Example usage:
result1, result2, result3, result4 = perform_operations(5)
print("Logarithmic result:", result1)
print("Exponential result:", result2)
print("Power result (base 2):", result3)
print("Square root result:", result4)


# In[34]:


import math

def perform_operations(value):
    # Logarithmic function (log x)
    logarithm = math.log(value)
    
    # Exponential function (exp(x))
    exponential = math.exp(value)
    
    # Power function with base 2 (2^x)
    power = math.pow(2, value)
    
    # Square root
    square_root = math.sqrt(value)
    
    return logarithm, exponential, power, square_root

# Example usage
result = perform_operations(3.5)
print(result)


# The function returns a tuple containing the results of each operation. You can call the function with a specific value, as shown in the example usage, and then print the result to see the output.
# 
# Please note that the math module is used to perform these mathematical operations.

# #9. Create a function that takes a full name as an argument and returns first name and last name.
# 

# In[35]:


def get_first_last_name(full_name):
    # Split the full name into separate parts
    name_parts = full_name.split()

    # Extract the first name (first part)
    first_name = name_parts[0]

    # Extract the last name (last part)
    last_name = name_parts[-1]

    return first_name, last_name

# Example usage
name = "John Doe"
first_name, last_name = get_first_last_name(name)
print("First Name:", first_name)
print("Last Name:", last_name)


# The function returns the first name and last name as a tuple. In the example usage, the function is called with the name "John Doe," and the first name and last name are printed separately using multiple assignment.
