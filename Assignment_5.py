#!/usr/bin/env python
# coding: utf-8

# #1. What does an empty dictionary's code look like?
# ans: An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list. The length len() of a dictionary is the number of key-value pairs it has.

# In[9]:


s = {}  # An empty dictionary
print(len(s))  # Output: 0

s = {'name': 'John', 'age': 30}  # A dictionary with two key-value pairs
print(len(s))  # Output: 2
#In the first example, the dictionary my_dict is empty, so its length is zero. 
#In the second example, my_dict has two key-value pairs, so its length is two.


# In[11]:


type(s)


# #2. What is the value of a dictionary value with the key 'foo' and the value 42?

# In[13]:


m = {'foo': 42}
value = m['foo']
print(value)  # Output: 42


# #In this example, the dictionary m is created with the key-value pair 'foo': 42. By accessing the value using the key 'foo', we assign it to the variable value, and when we print value, it outputs 42.

# #3. What is the most significant distinction between a dictionary and a list?
# ans:Lists are just like the arrays, declared in other languages. Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.
# in Python on the other hand is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

# In[19]:


# Python program to demonstrate
# Lists


# Creating a List with
# the use of multiple values
List = ["1", "34.5", "Gowtami"]
print("List containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = ["1", "34.5", "Gowtami","[1,2,3,4,5]"]
print("\nMulti-Dimensional List: ")
print(List)


# #4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# In[21]:


spam = {'bar':100}
spam['foo']
#This will give us key error
     


# #5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[22]:


spam ={'cat':100}
'cat' in spam
     


# In[23]:


'cat' in spam.keys()
#There is no differnce, both check if 'cat' is key of the dictionary and if its a key, returns True.


# #6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# In[25]:


spam ={'cat':100}
'cat' in spam


# In[26]:


spam ={'cat':100}
'cat' in spam.values()

#'cat' in spam checks whether there is a 'cat' key in the dictionary
#'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# #7.What is a shortcut for the following code?
# 

# In[27]:


spam ={'cat':100}
spam.setdefault('color','black')
spam


# #8.How do you 'pretty print' dictionary values using which module and function?
# ans.Prettyprint is the process of converting and presenting source code or other objects in a legible and attractive way. A prettyprinter takes blocks of code and prints them in an aesthetically pleasing fashion, presenting the characters with line breaks and indentations to make the code comprehensible. Prettyprinters are also called code beautifiers.

# import pprint
# A = [ {'Name': 'Gowtami', 'Age': '30', 'Country': 'Sweden'},
#   {'Name': 'Erik', 'Age': '32', 'Country': 'Austria'},
#   {'Name': 'Elsa', 'Age': '18', 'Country': 'Usa'},
#   {'Name': 'Chutki', 'Age': '35', 'Country': 'Usa'}
# ]

# In[29]:


# printing with pprint()
pprint.pprint(A)


# In[30]:


#Printing with print()
print(A)


# In[ ]:




