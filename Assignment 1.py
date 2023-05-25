#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# *
# hello
# 
# -87.8
# 
# -
# 
# /
# 
# +
# 
# 6
# 
# Ans:
# 
# Values:
# 
# "hello" (string)
# -87.8 (float)
# 6 (integer)
# 
# Expressions:
# 
#  (*) Multiplication operator
#  (-) Subtraction operator
#  (/) Division operator
# 

# 2.What is the difference between string and variable?
# 
# Ans:A string and a variable are two different concepts in programming.
# 
# A string is a data type that represents a sequence of characters. It is typically used to store and manipulate textual data. In many programming languages, a string is denoted by enclosing the characters within quotation marks, either single ('') or double (""). For example, "Hello, World!" is a string.
# 
# A variable is a symbolic name that represents a value or data stored in the computer's memory. Variables are used to store and manipulate different types of data, including strings, numbers, and more. Variables are assigned values, and those values can be changed during the execution of a program.

# In[1]:


# String
message = "Hello, World!"
print(message)  # Message: Hello, World!

# Variable
x = 5
y = 10
sum = x + y
print(sum)  # Sum: 15


# In[4]:


# Single quotes
string1 = 'Hello, World!'
print(string1) 

# Double quotes
string2 = "I am Mayookha"
print(string2)  

# Triple quotes for multi-line strings
string3 = """I am 32years old.
I am Doctor ."""
print(string3)



# In[ ]:


3. Describe three different data types.
Ans:Integers,strings,floats
Integers are whole numbers,without a fractional component.they can be positive or negative.


# In[ ]:


X = 10


# A string is a data type that represents a sequence of characters. It is typically used to store and manipulate textual data. In many programming languages, a string is denoted by enclosing the characters within quotation marks, either single ('') or double (""). For example, "Hello, World!" is a string.

# In[11]:


Myname = 'Gowtami'
print(Myname) 


# In Python, "float" refers to the floating-point data type, which is used to represent real numbers with decimal points. Floats in Python are used to store and manipulate numerical values that can have fractional parts.
# 
# Floats can be positive or negative and can have values ranging from very small to very large. They are typically represented using decimal notation, including the decimal point and an optional exponent using the scientific notation.
# 
# 
# 

# In[13]:


x = 3.14
y = -0.5
z = 1.23e6  # Equivalent to 1.23 * 10^6

print(x)  # Output: 3.14
print(y)  # Output: -0.5
print(z)  # Output: 1230000.0


# 4. What is an expression made up of? What do all expressions do?
# Ans:An expression is made up of one or more elements that combine to produce a new value or result. These elements can include literals (such as numbers or strings), variables, operators, and function calls. Expressions are used in programming to perform computations, make comparisons, or evaluate conditions.
# 
# All expressions in programming have a specific purpose, which is to produce a value. The value can be of various types, such as a number, a string, a boolean, or even a more complex data structure. The result of an expression can be assigned to a variable, used as part of a larger expression, or used in control flow statements to make decisions.
# 
# Here are a few examples of expressions in Python:
# 
# Arithmetic expression:In this expression, 2 + 3 * 4 combines addition and multiplication operators to calculate the result, which is 14. The value 14 is assigned to the variable result.
# 
# String concatenation expression:
# In this expression, "Hello, " and "World!" are string literals that are concatenated using the + operator. The result is the string "Hello, World!", which is assigned to the variable greeting.
# 
# Comparison expression:
# In this expression, 10 == 5 * 2 compares the value of 10 with the result of 5 * 2 using the equality operator (==). The result is True because 10 is indeed equal to 10.
# 
# Expressions play a crucial role in programming as they enable computations, comparisons, and the manipulation of data. They are fundamental for building algorithms, making decisions, and performing various operations in a program.

# In[19]:


#Arithmetic expression
result = 2 + 3 * 4


# In[20]:


# String concatenation expression:
greeting = "Hello, " + "World!"


# In[21]:


#Comparison expression:
is_equal = 10 == 5 * 2


# 5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# Ans:The main difference between expressions and statements is that expressions produce a value, while statements perform actions or control the flow of a program. Expressions are used within statements to calculate values or make comparisons. Statements, on the other hand, contain expressions and other keywords to carry out specific tasks and define the structure of a program.
# 
# Statement:
# The statement "spam = 10" is an example of an assignment statement in programming. In this specific case, the variable "spam" is being assigned the value of 10. This means that the variable "spam" now holds the value 10, and you can use this value in subsequent parts of your code.
# 
# A statement, on the other hand, is a complete instruction or action that performs a specific task. It represents a complete line of code and typically consists of one or more expressions, keywords, and control flow structures. Statements are used to control the flow of a program, define actions, and manipulate data. Examples of statements include variable assignments (spam = 10), conditional statements (if, else, elif), loops (for, while), and function definitions.

# In[12]:


get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


# In[22]:


bacon = 22
bacon + 1


# Ans:In the code provided, there is a variable named bacon that is initially assigned the value 22. Then, there is an expression bacon + 1 which adds 1 to the value of bacon. However, the result of this expression is not saved or stored anywhere.
# 
# So, even though the expression bacon + 1 evaluates to 23, the variable bacon still contains its original value of 22.

# 7. What should the values of the following two terms be?
# 'spam' +'spamspam'
# 'spam' * 3

# In[23]:


'spam' +'spamspam'
'spam' * 3


# 7.What should the values of the following two terms be? 'spam' +'spamspam' 'spam' * 3
# Ans:n the first term 'spam' + 'spamspam', we are combining or joining the string 'spam' with the string 'spamspam'. When we do this, the two strings are merged together, resulting in the longer string 'spamspamspam'.
# 
# In the second term 'spam' * 3, we are multiplying the string 'spam' by 3. This means that we are repeating the string three times. So, when we multiply 'spam' by 3, it becomes 'spamspamspam'.
# 
# In both cases, the result is the same: the string 'spamspamspam'.

# 8. Why is eggs a valid variable name while 100 is invalid?
# 
# Ans: Variable names in Python must abide by a set of constraints in order to be legitimate. As for the guidelines:
# 
# -Letters (a-z, A-Z), numbers (0–9), and underscores (_) are the only characters that can be used in variable names. They cannot include any more special characters or blank spaces.
# 
# -A digit cannot begin a variable name. The first character in them must be a letter or an underscore.
# 
# Let's think over the instances you gave while keeping in mind these guidelines:
# 
# Because "eggs" only contains letters and starts with a letter, it is a legal variable name.
# 
# Since "100" begins with a digit, it is not a permitted variable name. Starting with a digit in a variable name is against the requirement that variable names must begin with a letter or an underscore.

# 9.What three functions can be used to get the integer, floating-point number, or string version of a value?
# 
# Ans:In Python, there are three functions commonly used to convert values to specific types:
# 
# int(): This function is used to convert a value into an integer. It takes a parameter, which can be a number or a string representing a number, and returns an integer. If the value cannot be converted into an integer (for example, if it contains non-numeric characters), it will raise an error.

# In[29]:


value = "19"
integer_value = int(value)
print(integer_value) 


# float(): This function is used to convert a value into a floating-point number (a decimal number). Similar to int(), it takes a parameter that can be a number or a string representing a number and returns a floating-point number. If the value cannot be converted into a float, it will raise an error.

# In[28]:


value = "2.197"
float_value = float(value)
print(float_value) 


# str(): This function is used to convert a value into a string. It takes a parameter of any type and returns a string representation of that value. It is particularly useful when you want to concatenate or display a value as a string.

# In[27]:


value = 30
string_value = str(value)
print(string_value)  


# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten' + 99+ ' burritos'.
# 
# Ans: The expression 'I have eaten' + 99 + ' burritos' causes an error because it is attempting to concatenate (combine) a string, an integer, and another string without converting the integer to a string explicitly.
# 
# In Python, the + operator is used for both addition and string concatenation. However, when you use the + operator with different types of operands, such as a string and an integer, Python requires explicit type conversion to perform the concatenation successfully.
# 
# To fix the error and make the expression work as intended, you can convert the integer 99 to a string using the str() function. By converting the integer to a string, you ensure that all the operands are of the same type (string) and can be concatenated together.

# In[30]:


'I have eaten ' + str(99) + ' burritos'


# The str(99) converts the integer 99 to a string, allowing it to be concatenated properly with the other strings. The result would be 'I have eaten 99 burritos', where the number 99 is now treated as a string and properly combined with the other strings.
