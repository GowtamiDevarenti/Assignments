#!/usr/bin/env python
# coding: utf-8

# #1.What are the two values of the Boolean data type? How do you write them?
# 
# Ans:The two values of the Boolean data type in Python are True and False.
# 
# you can think of True as representing a condition or statement that is considered to be true or valid. On the other hand, False represents a condition or statement that is considered to be false or invalid.
# 
# In Python, these Boolean values are written as True and False exactly as shown, with the first letter capitalized. It's important to note that they are not enclosed in quotation marks, as they are keywords in the Python programming language.

# #2.What are the three different types of Boolean operators?
# 
# Ans:The three different types of Boolean operators are:
# 
# AND operator: It combines two or more conditions and returns true only if all the conditions are true. In simpler terms, it's like asking if both things are true.
# " For example, if we have the conditions "It is sunny" and "I have an umbrella," the result of the AND operator would be "true" only if both conditions are true. Otherwise, it would be "false."
# 
# Example:
# Condition 1: It is sunny.
# Condition 2: I have an umbrella.
# Result: It is sunny AND I have an umbrella (true if both conditions are true, false otherwise).
# 
# OR operator: It combines two or more conditions and returns true if at least one of the conditions is true. In simpler terms, it's like asking if either of the things is true.
# " For example, if we have the conditions "It is raining" and "I have a raincoat," the result of the OR operator would be "true" if either condition is true. It would be "false" only if both conditions are false.
# 
# Example:
# Condition 1: It is raining.
# Condition 2: I have a raincoat.
# Result: It is raining OR I have a raincoat (true if at least one condition is true, false if both conditions are false).
# 
# 
# NOT operator: It takes a single condition and returns the opposite value. If the condition is true, the NOT operator returns false, and if the condition is false, it returns true. In simpler terms, it's like negating or flipping the truth value of a statement.
# Example:
# Condition: It is not raining.
# Result: NOT (It is not raining) (true if it is actually raining, false if it is not raining).
# 

# #3. Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).
# Ans:
# 
# Here are the truth tables for each Boolean operator:
# 
# 1. AND Operator:
# 
# | Operand 1 | Operand 2 | Result |
# |-----------|-----------|--------|
# |   False   |   False   | False  |
# |   False   |   True    | False  |
# |   True    |   False   | False  |
# |   True    |   True    | True   |
# 
# 2. OR Operator:
# 
# | Operand 1 | Operand 2 | Result |
# |-----------|-----------|--------|
# |   False   |   False   | False  |
# |   False   |   True    | True   |
# |   True    |   False   | True   |
# |   True    |   True    | True   |
# 
# 3. NOT Operator:
# 
# | Operand | Result |
# |---------|--------|
# |  False  |  True  |
# |  True   | False  |
# 
# In the truth tables, the "Operand 1" and "Operand 2" columns represent the input Boolean values for the respective operators, and the "Result" column indicates the evaluated result based on the operator's logic.
#     

# #4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# Ans:
#     
# Let's evaluate the given expressions:
# 
# (5 > 4) and (3 == 5)
# (5 > 4) evaluates to True
# (3 == 5) evaluates to False
# True and False evaluates to False
# 
# not (5 > 4)
# 
# (5 > 4) evaluates to True
# not True evaluates to False
# 
# (5 > 4) or (3 == 5)
# 
# (5 > 4) evaluates to True
# (3 == 5) evaluates to False
# True or False evaluates to True
# 
# not ((5 > 4) or (3 == 5))
# 
# (5 > 4) evaluates to True
# (3 == 5) evaluates to False
# True or False evaluates to True
# not True evaluates to False
# 
# (True and True) and (True == False)
# 
# True and True evaluates to True
# True == False evaluates to False
# True and False evaluates to False
# (not False) or (not True)
# 
# not False evaluates to True
# not True evaluates to False
# True or False evaluates to True
# 
# 

# In[12]:


# Expression 1
result_1 = (5 > 4) and (3 == 5)
print(result_1)  # Output: False

# Expression 2
result_2 = not (5 > 4)
print(result_2)  # Output: False

# Expression 3
result_3 = (5 > 4) or (3 == 5)
print(result_3)  # Output: True

# Expression 4
result_4 = not ((5 > 4) or (3 == 5))
print(result_4)  # Output: False

# Expression 5
result_5 = (True and True) and (True == False)
print(result_5)  # Output: False

# Expression 6
result_6 = (not False) or (not True)
print(result_6)  # Output: True


# #5.What are the six comparison operators?
# 
# Ans: 
# The six comparison operators in Python are:
# 
# Equal to (==): Checks if two values are equal.
# 
# Not equal to (!=): Checks if two values are not equal.
# 
# Greater than (>): Checks if the left value is greater than the right value.
# 
# Less than (<): Checks if the left value is less than the right value.
# 
# Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.
# 
# Less than or equal to (<=): Checks if the left value is less than or equal to the right value.
# 
# These operators are used to compare values and return a Boolean result (True or False) based on the comparison.
# 

# In[13]:


#Equal to (==): Checks if two values are equal.
x = 5
y = 10
print(x == y)  # Output: False


# In[14]:


#Not equal to (!=): Checks if two values are not equal.
x = 5
y = 10
print(x != y)  # Output: True


# In[15]:


#Greater than (>): Checks if the left value is greater than the right value.
x = 5
y = 10
print(x > y)  # Output: False


# In[16]:


#Less than (<): Checks if the left value is less than the right value.
x = 5
y = 10
print(x < y)  # Output: True


# In[17]:


#Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.
x = 5
y = 10
print(x >= y)  # Output: False


# In[18]:


#Less than or equal to (<=): Checks if the left value is less than or equal to the right value.
x = 5
y = 10
print(x <= y)  # Output: True


# #6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
# Ans:The equal to operator (==) is used for comparison, while the assignment operator (=) is used for assigning values to variables.
# 
# The equal to operator (==) is used to compare two values and determine if they are equal. It returns a Boolean value (True or False) based on the comparison. 

# In[19]:


# For example:
x = 5
y = 10
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")



# 
# 
# 
# In this example, the == operator compares the values of x and y and determines that they are not equal, so the output would be "x is not equal to y".On the other hand, the assignment operator (=) is used to assign a value to a variable. 
# x = 5
# y = x
# In this example, the value of x (which is 5) is assigned to the variable y using the = operator.
# 
# To differentiate between the equal to operator and the assignment operator, you need to consider the context in which they are used. The equal to operator is used for comparison in conditions, such as in if statements or in boolean expressions. The assignment operator is used to assign values to variables.
# 
# In summary, the equal to operator (==) is used for comparison, while the assignment operator (=) is used for assigning values to variables.
# 
# 

# #7. Identify the three blocks in this code:
# 
# spam = 0
# 
# if spam == 10:
# 
# print('eggs')
# 
# if spam > 5:
# 
# print('bacon')
# 
# else:
# 
# print('ham')
# 
# print('spam')
# 
# print('spam')

# In[39]:


#Ans:
#The code provided has three blocks identified by indentation. Here are the blocks:

#Block 1:

spam = 0

if spam == 10:
    print('eggs')  # Block 1

if spam > 5:
    print('bacon')  # Block 2



    
    
#This block contains the if statement that checks if spam is equal to 10. 
#If the condition is true, it executes the indented code print('eggs').

#Block 2:

if spam > 5:
    print('bacon')

#This block contains the second if statement that checks if spam is greater than 5.
#If the condition is true, it executes the indented code print('bacon').

#Block 3:

else:
    print('ham')
print('spam')
print('spam')


#This block starts with the else statement, which is associated with the second if statement. 
#If the condition in the second if statement is false, it executes the indented code print('ham').
#The subsequent lines print('spam') and print('spam') are not indented, so they are not part of the else block. 
#They are separate statements executed unconditionally.

#It is important to properly indent the code in Python, as indentation defines the blocks and their associated statements.





    


# #8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.
# 
# Ans:
# an if-elif-else statement in Python to achieve this. Here's an example code that accomplishes the desired behavior:
# 

# In[2]:


if condition1:
    # Code to execute if condition1 is true
elif condition2:
    # Code to execute if condition1 is false and condition2 is true
else:
    # Code to execute if both condition1 and condition2 are false


# In[41]:


spam = 1

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In this code, the value of spam is checked using the if-elif-else statement. If spam is equal to 1, it prints "Hello". If spam is equal to 2, it prints "Howdy". If spam is any other value, it prints "Greetings!".
# 
# You can modify the value of spam variable to test different cases and see the corresponding output.

# #9.If your programme is stuck in an endless loop, what keys you’ll press?
# Ans:If your program is stuck in an endless loop while running in a Python environment, you can typically interrupt the execution using the following key combination:
# 
# Ctrl + C on Windows or Linux
# Command + C on macOS
# 
# Pressing these keys will send an interrupt signal to the Python interpreter, which will cause the program to terminate and return control back to the command line or the Python environment.

# #10. How can you tell the difference between break and continue?
# Ans:Break: When encountered within a loop (such as for or while), the break statement terminates the loop immediately and transfers the control to the next statement outside the loop. It breaks out of the loop entirely, skipping any remaining iterations. After the loop is terminated by break, the program continues to execute from the next statement after the loop.
# 
# Continue: When encountered within a loop, the continue statement skips the rest of the current iteration and moves the control back to the loop's beginning for the next iteration. It effectively bypasses the remaining code within the loop for that particular iteration and jumps to the next iteration.
# 
# To summarize, break is used to exit the loop entirely, while continue is used to skip the remaining code within the loop for the current iteration and move to the next iteration.
# 
# 

# In[42]:


#Break
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# In[43]:


#continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# #11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# In a for loop, the expressions range(10), range(0, 10), and range(0, 10, 1) all generate a sequence of numbers, but there are some differences in their syntax and behavior:
# 
# range(10): This expression creates a sequence that starts from 0 (by default) and goes up to, but does not include, the specified number. In this case, the sequence will contain numbers from 0 to 9. The step size between consecutive numbers is implicitly set to 1.
# 

# In[44]:


for i in range(10):
    print(i)


# range(0, 10): This expression defines a range that starts from the first specified number (0) and ends at the second specified number (10), excluding the endpoint. The step size between consecutive numbers is implicitly set to 1.

# In[45]:


for i in range(0, 10):
    print(i)


# range(0, 10, 1): This expression creates a range starting from the first specified number (0), ending at the second specified number (10), excluding the endpoint. The third argument represents the step size, which in this case is explicitly set to 1. The step size determines the difference between consecutive numbers in the sequence.

# In[46]:


for i in range(0, 10, 1):
    print(i)


# In summary, all three expressions (range(10), range(0, 10), and range(0, 10, 1)) produce the same sequence of numbers from 0 to 9 in steps of 1. The difference lies in the syntax used to specify the start, stop, and step values within the range() function.

# #12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

# Here's a short program that prints the numbers 1 to 10 using a for loop:

# In[47]:


for i in range(1, 11):
    print(i)


# In[48]:


# here's an equivalent program that prints the numbers 1 to 10 using a while loop:
i = 1
while i <= 10:
    print(i)
    i += 1


# In the for loop program, the range(1, 11) function generates a sequence of numbers from 1 to 10, and the loop iterates over each number in the sequence.
# 
# In the while loop program, a variable i is initialized to 1. The loop continues as long as i is less than or equal to 10. Inside the loop, i is printed, and then incremented by 1 using i += 1 to ensure the loop eventually terminates.

# #13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?
# Ans:
#   After importing the spam module, you can call the bacon() function by using the following syntax:  

# In this code, spam refers to the imported module, and bacon() is the function defined within the spam module. By prefixing the function name with the module name followed by a dot (spam.bacon()), you can access and call the bacon() function from the spam module.

# In[ ]:


import spam

spam.bacon()

