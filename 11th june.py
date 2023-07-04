#!/usr/bin/env python
# coding: utf-8

# #1.What is a lambda function in Python, and how does it differ from a regular function?
# Ans:A lambda function in Python, also known as an anonymous function, is a small, one-line function that doesn't require a formal definition using the def keyword. Lambda functions are defined using the lambda keyword and can take any number of arguments but can only have a single expression.
# 
# The syntax of a lambda function is as follows:
# 

# In[1]:


lambda arguments: expression


# The key differences between a lambda function and a regular function are as follows:
# 
# Syntax: Lambda functions have a concise syntax compared to regular functions. They are defined in a single line and don't require a separate function name, return statement, or explicit block of code.
# 
# Anonymous: Lambda functions are anonymous, meaning they don't have a name associated with them. They are usually defined inline where they are needed and aren't assigned to any variable.
# 
# Single Expression: Lambda functions can only contain a single expression. The expression is evaluated and the result is automatically returned. There can't be multiple statements or complex control flow structures within a lambda function.
# 
# Limited Functionality: Due to their simplicity, lambda functions are typically used for small, one-off tasks and simple operations. They are not suitable for more complex tasks that require multiple statements or extensive logic.
# 
# Here's an example to illustrate the difference between a lambda function and a regular function:

# In[2]:


# Regular function
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)  # Output: 12

# Equivalent lambda function
multiply_lambda = lambda a, b: a * b

result_lambda = multiply_lambda(3, 4)
print(result_lambda)


# In this example, the regular function multiply() takes two arguments and returns their product. The lambda function multiply_lambda is defined using the lambda keyword and has the same functionality as the regular function. The lambda function is then called with arguments 3 and 4, resulting in the same output as the regular function.
# 
# Lambda functions are particularly useful when working with higher-order functions such as map(), filter(), or reduce(), where a function is expected as an argument. Instead of defining a separate function, a lambda function can be used directly inline, making the code more concise and readable.
# 
# Overall, lambda functions provide a compact and convenient way to define simple functions on the fly without the need for a formal function definition.

# #2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
# them?
# ans: Yes, a lambda function in Python can have multiple arguments. The syntax for defining and using multiple arguments in a lambda function is similar to that of a regular function.
# Here's an example of a lambda function with multiple arguments:

# In[5]:


multiply = lambda x, y : x * y

result = multiply(3, 4)
print(result)  


# In this example, the lambda function multiply takes two arguments x and y and returns their product. The function is defined using the lambda keyword, followed by the arguments separated by commas, and a colon (:) before the expression. The expression in this case is x * y, which is evaluated and returned.
# 
# When calling the lambda function, you can pass the required arguments within the parentheses, just like with a regular function call. In the example, multiply(3, 4) is called, and it returns the result of multiplying 3 and 4, which is 12.
# 
# Lambda functions with multiple arguments can be used in various scenarios, such as when working with higher-order functions or in cases where a small, inline function is needed for a specific purpose.

# #3. How are lambda functions typically used in Python? Provide an example use case.
# ans.Lambda functions are typically used in Python when a small, one-line function is required without the need for a formal function definition. They are commonly used in conjunction with higher-order functions such as map(), filter(), and reduce(), where a function is expected as an argument.
# 
# Here's an example use case to illustrate the typical usage of lambda functions:

# In[6]:


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() with lambda function to square each number
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  


# Using a lambda function in this case allows us to define the squaring operation in a concise and inline manner without the need for a separate function definition. It simplifies the code and eliminates the need to define a separate named function.
# 
# Lambda functions can also be used with filter() to selectively filter elements from a list based on a condition or with reduce() to perform operations like summing elements or finding the maximum value. They provide a convenient way to define simple functions on the fly when working with higher-order functions that expect a function as an argument.

# #4. What are the advantages and limitations of lambda functions compared to regular functions in
# Python?
# ans.Lambda functions in Python have several advantages and limitations compared to regular functions. Here are the key points to consider:
# 
# Advantages of Lambda Functions:
# 
# Concise Syntax: Lambda functions provide a more compact syntax compared to regular functions. They can be defined in a single line, which can make the code more readable and expressive.
# 
# Inline Definition: Lambda functions are defined inline at the point of use, eliminating the need for a separate function definition. This can be advantageous when you need a small, one-time function and don't want to clutter your code with unnecessary function definitions.
# 
# Anonymous: Lambda functions are anonymous, meaning they don't require a specific name. This is useful when you only need a function for a specific task and don't intend to reuse it elsewhere in your code.
# 
# Higher-Order Functions: Lambda functions are commonly used with higher-order functions such as map(), filter(), and reduce(). They provide a convenient way to define simple functions on the fly without the need for a separate named function.
# 
# Limitations of Lambda Functions:
# 
# Single Expression: Lambda functions can only contain a single expression, limiting their ability to handle complex logic or multiple statements. They are best suited for simple, one-line operations.
# 
# Lack of Statements and Control Flow: Lambda functions cannot contain statements like if, while, or for loops, as these require multiple lines of code. Lambda functions are restricted to expressions only.
# 
# Reduced Readability: While lambda functions can make code more concise, they can also reduce readability when used excessively or inappropriately. Complex operations are often better served by regular functions with descriptive names.
# 
# Limited Functionality: Due to their simplicity and limitations, lambda functions are not suitable for tasks that require extensive logic or complex operations. Regular functions provide more flexibility and can handle a wider range of requirements.
# 
# It's important to consider these advantages and limitations when deciding whether to use a lambda function or a regular function in your Python code. While lambda functions can be handy in specific scenarios, regular functions are more versatile and provide greater flexibility for complex tasks.

# #5. Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.
# ans.Yes, lambda functions in Python can access variables defined outside of their own scope. These variables can be accessed from the enclosing scope, similar to regular functions and other constructs in Python. This behavior is known as "lexical scoping" or "closure."
# 
# Here's an example to illustrate how lambda functions can access variables from their enclosing scope:

# In[9]:


def outer_function():
    x = 10

    # Lambda function accessing variable from outer scope
    lambda_func = lambda y: x + y

    return lambda_func

# Call outer function and assign the lambda function to a variable
my_lambda = outer_function()

# Call the lambda function with an argument
result = my_lambda(15)

print(result)  


# In this example, the outer_function() defines a variable x with a value of 10. Inside the function, a lambda function lambda_function is defined, which takes an argument y and returns the sum of x and y. The lambda function accesses the variable x from its enclosing scope, which is the outer_function().
# 
# When outer_function() is called and the result is assigned to the result variable, it returns the lambda function. The lambda function, in turn, is called with an argument of 5, resulting in the sum of 10 (from x) and 15. The output is 25.
# 
# Lambda functions have access to the variables in the enclosing scope due to the concept of lexical scoping. They "capture" the values of these variables at the time of their creation. This behavior is particularly useful when working with higher-order functions or when you want to create functions dynamically that rely on values from their surrounding context.
# 
# It's important to note that lambda functions can access variables from the enclosing scope, but they cannot modify them. If you need to modify variables from the enclosing scope, you would need to use regular functions and explicitly declare those variables as nonlocal within the function.

# #6. Write a lambda function to calculate the square of a given number.
# ans.Lambda functions are particularly useful for simple operations like squaring a number, where a full function definition may be unnecessary.

# In[11]:


square = lambda x: x**2
print(square(4))


# #7. Create a lambda function to find the maximum value in a list of integers.
# ans:Lambda functions can be handy when you need a quick and concise way to perform simple operations on a list, such as finding the maximum value.

# In[13]:


numbers = [5, 2, 8, 1, 9, 3, 12, 17, 19]

maximum = lambda lst: max(lst)
result = maximum(numbers)

print(result)  


# #8. Implement a lambda function to filter out all the even numbers from a list of integers.
# ans:Using a lambda function with filter() allows you to succinctly filter elements from a list based on a specific condition without the need for a separate function definition.
# 

# In[14]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,13,17,32]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  


# #9. Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.
# ans:The lambda function is used as the key to determine the sorting order. By passing this lambda function as the key, the sorted() function sorts the strings list in ascending order based on the length of each string.
# 
# The output of this example is ['kiwi', 'grape', 'apple', 'banana', 'orange'], which is the sorted list of strings based on their lengths in ascending order.
# 
# Using a lambda function with the key parameter of sorting functions allows you to customize the sorting behavior based on specific criteria. In this case, the lambda function enables sorting the strings based on their lengths.

# In[15]:


strings = ["apple", "banana", "orange", "kiwi", "grape"]

sorted_strings = sorted(strings, key=lambda x: len(x))
print(sorted_strings)  


# #10. Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.
# ans:Using a lambda function with filter() allows you to filter elements from one list based on their presence in another list, effectively finding the common elements.

# In[17]:


list1 = [1, 2, 3, 4, 5, 9,12]
list2 = [4, 5, 6, 7, 8,9,11,18]

common_elements = list(filter(lambda x: x in list1, list2))
print(common_elements)  


# #11. Write a recursive function to calculate the factorial of a given positive integer.
# ans:Recursion is a powerful technique for solving problems by breaking them down into smaller, similar subproblems. In the case of calculating factorials, the recursive approach simplifies the calculation by reducing it to the factorial of a smaller number.

# In[20]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")  


# #12. Implement a recursive function to compute the nth Fibonacci number.
# ans:Recursion is a powerful technique for solving problems by breaking them down into smaller, similar subproblems. In the case of computing Fibonacci numbers, the recursive approach simplifies the calculation by reducing it to the sum of smaller Fibonacci numbers.

# In[22]:


def fibonacci(n):
    # Base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and Fibonacci of (n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 6
result = fibonacci(number)
print(f"The {number}th Fibonacci number is {result}")  


# #13. Create a recursive function to find the sum of all the elements in a given list.
# ans:Recursion is a powerful technique for solving problems by breaking them down into smaller, similar subproblems. In the case of finding the sum of a list, the recursive approach simplifies the calculation by reducing it to the sum of a smaller sublist.

# In[23]:


def recursive_sum(lst):
    # Base case: empty list has a sum of 0
    if len(lst) == 0:
        return 0
    # Recursive case: add first element with the sum of the rest of the list
    else:
        return lst[0] + recursive_sum(lst[1:])


numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(f"The sum of the list {numbers} is {result}")  


# #14. Write a recursive function to determine whether a given string is a palindrome.
# ans:Recursion is a powerful technique for solving problems by breaking them down into smaller, similar subproblems. In the case of determining palindromes, the recursive approach simplifies the task by comparing characters from the beginning and end of the string.

# In[26]:


def is_palindrome(s):
    # Base case: empty string or single character is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if first and last characters match, and recursively check the remaining substring
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


string1 = "radar"
string2 = "hello"
string3 = "Level"

print(is_palindrome(string1)) 
print(is_palindrome(string2)) 
print(is_palindrome(string3)) 


# #15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
# ans:Recursion is a powerful technique for solving problems by breaking them down into smaller, similar subproblems. In the case of finding the GCD, the recursive approach simplifies the calculation by repeatedly applying the Euclidean algorithm until the base case is met.

# In[27]:


def gcd(a, b):
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a
    # Recursive case: recursively calculate GCD by dividing b from a
    else:
        return gcd(b, a % b)

# Example usage
number1 = 24
number2 = 36
result = gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is {result}")  


# In[ ]:




