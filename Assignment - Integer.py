#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input("Enter the value of variable a: "))
b = int(input("Enter the value of variable b: "))

a, b = b, a

print("After swapping:")
print("Value of variable a:", a)
print("Value of variable b:", b)


# In[3]:


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print("The area of the rectangle is:", area)


# In[4]:


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# year = int(input("Enter a year: "))
# 
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
# 

# In[5]:


string = input("Enter a string: ")
character = input("Enter a character: ")

count = string.count(character)

print("The count of", character, "in the string is:", count)


# In[6]:


string = input("Enter a string: ")

reversed_string = string[::-1]

print("The reversed string is:", reversed_string)


# string = input("Enter a string: ")
# 
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")
# 

# In[7]:


string = input("Enter a string: ")

vowels = "aeiouAEIOU"
string_without_vowels = ""

for char in string:
    if char not in vowels:
        string_without_vowels += char

print("String without vowels:", string_without_vowels)


# In[8]:


string = input("Enter a string: ")

capitalized_string = string.title()

print("String with capitalized words:", capitalized_string)


# In[ ]:




