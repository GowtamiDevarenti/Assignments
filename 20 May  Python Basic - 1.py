#!/usr/bin/env python
# coding: utf-8

# #Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
# ans.Keywords in Python are reserved words that have predefined meanings and cannot be used as identifiers (variable names, function names, etc.). These keywords are part of the Python language syntax and have specific purposes.
# These keywords have specific meanings in Python and are used to define the structure and behavior of the code.
# 
# To print all the Python keywords, you can use the keyword library in Python. Here's an example:
# 

# In[2]:


import keyword
all_keywords = keyword.kwlist
print(all_keywords)


# #Q.2. What are the rules to create variables in python?
# ans.
# variable name should be meaningful
# Variable name must start with letter or underscore
# Multi -Word name in python
# Camel case:each word starts with small letter and Capital word.eg: myName,myVariableName
# pascal case :each word starts with capital letter.Eg:MyName,MyVariableName
# snake case:each word is separated by underscore.eg:my_variable_name
# we cant use reserved name
# python is case sensitive
# No Spaces or Special Characters

# #Q.3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# Ans.In Python, there are several standards and conventions followed for variable naming to improve code readability and maintainability. Here are some commonly used guidelines:
# 
# Snake Case: Python conventionally uses snake_case for variable names. In snake case, words are written in lowercase letters, and multiple words are separated by underscores. For example: my_variable, total_count, is_student.
# 
# Descriptive Names: Variable names should be descriptive and indicate the purpose or content of the data they represent. This helps in understanding the code and makes it easier to maintain. For example: name, age, is_student, total_count.
# 
# Avoid Single Letters: It is generally recommended to avoid using single letters (except for simple loop counters). Instead, use meaningful names that provide context. For example, use count instead of c, or index instead of i.
# 
# Use Plural for Collections: When naming variables that represent collections or sequences of items, it is common to use plural names. For example: users, items, names.
# 
# Avoid Reserved Words: Avoid using Python keywords or reserved words as variable names. This can lead to confusion and syntax errors. For example, don't use if, for, while, def, etc., as variable names.
# 
# Constants: For variables that represent constants or values that should not be modified, it is common to use uppercase letters and underscores. For example: MAX_VALUE, PI.
# 
# Consistency: Maintain consistency in variable naming throughout your codebase. If you use a specific naming style or convention, stick to it consistently to ensure code readability and maintainability.
# 
# It's important to note that these conventions are not strict rules enforced by Python itself, but rather widely followed community guidelines. Adhering to these conventions can greatly enhance the readability and maintainability of your code, making it easier for others to understand and collaborate on your projects.

# #Q.4. What will happen if a keyword is used as a variable name?
# ans.There are two main reasons:
# 
# It makes the developer's life hard; and
# 
# It makes the compiler's life hard.
# 
# If keywords were allowed as variable names, it would be very hard to tell (for the developers and the compilers) whether something was a variable or a keyword. For example, what does the following mean?
# 
# if(x == 10)
# 
# Is it an if-statement, or calling a function called if?
# 
# Neither the developer nor the compiler would be able to tell.

# In[3]:


if = 10  # Attempting to use 'if' as a variable name


# #Q.5. For what purpose def keyword is used?
# ans.Python def keyword is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function. In Python, a function is a logical unit of code containing a sequence of statements indented under a name given using the “def” keyword. In Python def keyword is the most used keyword.
# Use of def keyword:
# In the case of classes, the def keyword is used for defining the methods of a class.
# def keyword is also required to define the special member function of a class like __init__().
# The possible practical application is that it provides the feature of code reusability rather than writing the piece of code again and again we can define a function and write the code inside the function with the help of the def keyword. It will be more clear in the illustrated example given below. There can possibly be many applications of def depending upon the use cases.

# In[4]:


def python_def_keyword():
	print("Hello")
python_def_keyword()


# #Q.6. What is the operation of this special character ‘\’?
# ans.The special character \ in Python is known as the backslash or escape character. It has various operations and is used to represent special characters or sequences in strings and other literals. Here are some common uses of the backslash:
# 
# Escape Sequences: The backslash is used to introduce escape sequences that represent special characters within strings. For example:
# 
# \' represents a single quote character (')
# \" represents a double quote character (")
# \\ represents a literal backslash character ()
# \n represents a newline character
# \t represents a tab character
# \r represents a carriage return character, etc.
# These escape sequences allow you to include special characters or control characters within strings that would otherwise be difficult to represent directly.
# 
# Unicode Escapes: The backslash can be used to represent Unicode characters using their hexadecimal or Unicode code point values. For example:
# 
# \uXXXX represents a Unicode character with the four-digit hexadecimal value (e.g., \u20AC represents the Euro symbol €)
# \UXXXXXXXX represents a Unicode character with the eight-digit hexadecimal value (e.g., \U0001F600 represents the smiling face emoji 😄)
# Unicode escapes allow you to include characters from various scripts and symbols that may not be available on your keyboard directly.
# 
# Line Continuation: The backslash can be used to continue a logical line of code onto the next physical line. This is useful when you have long statements that need to be split into multiple lines for better readability. For example:

# In[5]:


result = 10 + \
         20 + \
         30


# #In this case, the backslash indicates that the statement continues on the next line, and Python treats it as a single line of code.
# 
# It's important to note that when the backslash is used as an escape character or for line continuation, it should be followed by another character or sequence to specify its purpose.

# #Q.7. Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple

# (i) Homogeneous List:
# A homogeneous list is a list where all the elements have the same data type. Here's an example of a homogeneous list of integers:

# In[ ]:


numbers = [1, 2, 3, 4, 5]
#In this example, all the elements in the numbers list are integers.


# (ii) Heterogeneous Set:
# A heterogeneous set is a set that contains elements of different data types. Here's an example of a heterogeneous set:

# In[ ]:


my_set = {1, 'apple', True, 3.14}
#In this example, the my_set set contains elements of different types, 
#including an integer (1), a string ('apple'), a boolean (True), and a float (3.14).


# (iii) Homogeneous Tuple:
# A homogeneous tuple is a tuple where all the elements have the same data type. Here's an example of a homogeneous tuple of strings:

# In[ ]:


fruits = ('apple', 'banana', 'orange')
#In this example, all the elements in the fruits tuple are strings.

Note: Lists, sets, and tuples in Python can contain elements of different data types. 
#The terms "homogeneous" and "heterogeneous" are used to describe whether the elements within a particular collection 
#(list, set, tuple) are of the same data type or different data types.


# #Q.8. Explain the mutable and immutable data types with proper explanation & examples.
# ans:Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of objects to change their values. These are often the objects that store a collection of data.
# Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.
# Objects of built-in type that are mutable are:
# 
# Lists
# Sets
# Dictionaries
# User-Defined Classes (It purely depends upon the user to define the characteristics) 
# Objects of built-in type that are immutable are:
# 
# Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
# Strings
# Tuples
# Frozen Sets
# User-Defined Classes (It purely depends upon the user to define the characteristics)
# Object mutability is one of the characteristics that makes Python a dynamically typed language.
# 
# In Python, everything is treated as an object. Every object has these three attributes:
# 
# Identity – This refers to the address that the object refers to in the computer’s memory.
# Type – This refers to the kind of object that is created. For example- integer, list, string etc. 
# Value – This refers to the value stored by the object. For example – List=[1,2,3] would hold the numbers 1,2 and 3
# While ID and Type cannot be changed once it’s created, values can be changed for Mutable objects.

# In[11]:


#Creating a list which contains name of Indian cities  

cities = ['Delhi', 'Mumbai', 'Kolkata']




# In[18]:


# Printing the elements from the list cities, separated by a comma & space
for city in cities:
		print(city, end=' , ')


# In[19]:


#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))


# In[21]:


#Adding a new city to the list cities

cities.append('Chennai')


# In[22]:


#Printing the elements from the list cities, separated by a comma & space 

for city in cities:
	print(city, end=' , ')


# In[23]:


#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(cities)))


# In[24]:


#Creating a Tuple with variable name ‘foo’

foo = (1, 2)


# In[25]:


#Changing the index[0] value from 1 to 3

foo[0] = 3


# #Immutable Objects in Python
# Once again, a simple code would be the best way to depict what immutable stands for. Hence, let us discuss the below code step-by-step:
# 
# 

# In[27]:


#Creating a Tuple which contains English name of weekdays

weekdays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


# In[28]:


# Printing the elements of tuple weekdays

print(weekdays)


# In[29]:


#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(weekdays)))


# In[31]:


#tuples are immutable, so you cannot add new elements, hence, using merge of tuples with the # + operator to add a new imaginary day in the tuple ‘weekdays’

weekdays  +=  'Pythonday',


# In[32]:


#Printing the elements of tuple weekdays

print(weekdays)


# In[33]:


#Printing the location of the object created in the memory address in hexadecimal format

print(hex(id(weekdays)))


# Some mutable data types in Python are:
# list, dictionary, set, user-defined classes.
# 
# Some immutable data types are: 
# int, float, decimal, bool, string, tuple, range.

# #Q.9. Write a code to create the given structure using only for loop.
#  *
#  ***
#  *****
#  *******
#  *********

# In[45]:


n = 5

for i in range(1, n + 1):
    odd_number = 2*i -1
    asterisks = '*'* odd_number
    print(asterisks)

    


# In[35]:





# Q.10. Write a code to create the given structure using while loop.
# |||||||||
# |||||||
# |||||
# |||
# |
# 

# In[7]:


n = 9
i = n
while i >0:
        print(f"{i*'|': ^{n}}")
        i -= 2 


# In[ ]:





# In[ ]:




