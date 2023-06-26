#!/usr/bin/env python
# coding: utf-8

# Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
# and store the results in variables. Then print the data in the following format by calling the
# variables:
# First variable is __ & second variable is __.
# Addition: __ + __ = __
# Subtraction: __ - __ = __
# Multiplication: __ * __ = __
# Division: __ / __ = __

# In[1]:


# Creating two int variables
first_variable = 10
second_variable = 5

# Performing addition, subtraction, multiplication, and division
addition_result = first_variable + second_variable
subtraction_result = first_variable - second_variable
multiplication_result = first_variable * second_variable
division_result = first_variable / second_variable

# Printing the results in the requested format
print(f"First variable is {first_variable} & second variable is {second_variable}.")
print(f"Addition: {first_variable} + {second_variable} = {addition_result}")
print(f"Subtraction: {first_variable} - {second_variable} = {subtraction_result}")
print(f"Multiplication: {first_variable} * {second_variable} = {multiplication_result}")
print(f"Division: {first_variable} / {second_variable} = {division_result}")


# #Q.2. What is the difference between the following operators:
# (i) ‘/’ & ‘//’
# (ii) ‘**’ & ‘^’

# ans:The operators you mentioned have different functionalities:
# 
# (i) / and // Operators:
# 
# The / operator is the division operator in Python. It performs normal division and returns a float result, even if the operands are integers. For example, 5 / 2 would result in 2.5.
# The // operator is the floor division operator in Python. It performs division and rounds down the result to the nearest integer (towards negative infinity). It returns an integer result. For example, 5 // 2 would result in 2.

# In[3]:


x = 5 / 2  # x = 2.5
y = 5 // 2  # y = 2


# (ii) ** and ^ Operators:
# 
# The ** operator is the exponentiation operator in Python. It raises the left operand to the power of the right operand. For example, 2 ** 3 would result in 8 (2 raised to the power of 3).
# The ^ operator, known as the caret operator, is not used for exponentiation in Python. Instead, it is the bitwise XOR operator. It performs the XOR operation on the binary representations of the operands. This operator is used for bitwise operations, not exponentiation.

# In[4]:


x = 2 ** 3  # x = 8
y = 2 ^ 3  # y = 1 (bitwise XOR of 10 and 11 in binary)


# To summarize:
# 
# / is used for normal division, returning a float result.
# // is used for floor division, returning an integer result.
# ** is used for exponentiation, raising the left operand to the power of the right operand.
# ^ is used for bitwise XOR operation, manipulating binary representations of operands.
# It's important to use the correct operator based on the desired operation to avoid unexpected results.

# #Q.3. List the logical operators.
# ans:In Python, the logical operators are used to perform logical operations on Boolean values (True or False) or expressions. The logical operators in Python are:
# 
# and Operator:
# The and operator returns True if both operands are True. Otherwise, it returns False. It evaluates the second operand only if the first operand is True.
# 
# or Operator:
# The or operator returns True if at least one of the operands is True. If both operands are False, it returns False. It evaluates the second operand only if the first operand is False.
# 
# not Operator:
# The not operator is a unary operator that reverses the logical state of its operand. If the operand is True, the not operator returns False. If the operand is False, it returns True.
# 
# These logical operators can be used to combine and manipulate Boolean values or expressions in conditional statements, loops, and other logical operations.
# 
# Example usage:

# In[5]:


x = True
y = False

result = x and y  # result = False
result = x or y   # result = True
result = not x    # result = False


# In the example above, the and operator is used to perform a logical AND operation between x and y, resulting in False. The or operator is used to perform a logical OR operation, resulting in True. The not operator is used to negate the value of x, resulting in False

# #Q.4. Explain right shift operator and left shift operator with examples.
# ans.In Python, the right shift (>>) and left shift (<<) operators are bitwise operators used to perform bit-level operations on integer values. Here's an explanation of both operators with examples:
# 
# Right Shift Operator (>>):
# The right shift operator shifts the bits of the left operand to the right by the number of positions specified by the right operand. The shifted bits are discarded, and the vacant positions are filled with the sign bit (the leftmost bit) for signed integers, or with zeros for unsigned integers.
# 
# Example:

# In[6]:


x = 12  # Binary: 1100
y = x >> 2  # Right shift by 2 positions
print(y)  # Output: 3


# In this example, the binary representation of x is 1100. When we right shift x by 2 positions (x >> 2), the resulting value is 3 because the rightmost two bits are discarded, and the vacant positions are filled with zeros. The binary representation of y is 11, which is equivalent to the decimal value 3.

# Left Shift Operator (<<):
# The left shift operator shifts the bits of the left operand to the left by the number of positions specified by the right operand. The shifted bits are filled with zeros from the right side.
# 
# Example:

# In[7]:


x = 3  # Binary: 11
y = x << 2  # Left shift by 2 positions
print(y)  # Output: 12


# In this example, the binary representation of x is 11. When we left shift x by 2 positions (x << 2), the resulting value is 12 because the bits are shifted to the left by 2 positions, and the vacant positions on the right are filled with zeros. The binary representation of y is 1100, which is equivalent to the decimal value 12.
# 
# The right shift and left shift operators are commonly used in situations where you need to perform bitwise operations, manipulate binary representations of values, or optimize certain calculations.

# #Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
# present in the list or not.

# In[10]:


#Ans: Creating a list of length 15 with int type data
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# Checking if 10 is present in the list
if 10 in my_list:
    print("10 is present in the list.")
else:
    print("10 is not present in the list.")


# In[ ]:




