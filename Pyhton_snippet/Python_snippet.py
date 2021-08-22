#Python_365
#Day_1
#Python_snippets
#pythonprogramming 
#python3
#pythoncoding 
#pythondeveloper



# # To check your Python verson inside a script:

# import sys
# print(sys.version)


# Output : 3.7.9

# # # To check where is Python installed inside a script:

# import sys,os
# print(os.path.dirname(sys.executable))

# Output : C:\Users\aristo\AppData\Local\Programs\Python\Python37


#         # PIP --> Python package management system (Part-1) 

#     1. Install Package 

#             --👀> pip install <package_name>

#     2. Update package 

#             --👀> pip install <package_name> --upgrade
#                                 or
#             --👀> pip install -U <package_name>


#     3. Uninstall package 

#             --👀> pip uninstall <package_name> 


# #                    #    PyGems.com


     # PIP(LIST) --> Python package management system (Part-2) 

#          1. See Installed Packages  

#                 --👀> pip list

#         2. See Local Installed Packages 

#                 --👀> pip list -l

#         3. Outdated Packages 

#                 --👀> pip list -o 
    
#         4. Up-to-date packages

#                 --👀> pip list -u 

# ---------------------------------    pip list -v -----------------

# #                    #    PyGems.com



#      # PIP(Freeze) --> Python package management system (Part-3) 

#      **** Used for export installed modules and reinstall ****

#          1. See Installed Packages with version 

#                 --👀> pip Freeze

#         2. Export Installed Packages into txt file

#                 --👀> pip Freeze > requirements.txt

#         3. Install packages from a text file (exported by Freeze) 

#                 --👀>  pip install -r requirements.txt
    
# $ pip freeze > requirements.txt
# Open the text file, replace the == with >=, 
# and execute:

# $ pip install -r requirements.txt --upgrade



#                   #    PyGems.com
               #https://www.facebook.com/pygems

# Day-6

#       # Update all installed python packages with pip-review

#       Step 1 : Install pip-review 

#                 🔥 --> pip isntall pip-review

#       Step 2 : View Packages update information

#                 🔥 --> pip-review

#       Step 3 : Update all Packages

#                 🔥 --> pip-review --interactive


# import dis

# def foo():
#      print("hello")


# print(dis.dis(foo))


# If you are using the Windows operating system
# Make sure you have added the path to environment variables

# Check python is installed or not and also the version by cmd?
# How to run python script by cmd?
# How to run python script with interactive shell by cmd?






# # Check python is installed or not and also the version by cmd?
# *** Make sure you have added the path to environment variables ***

# cmd->🔥 python 

# cmd->🔥 python --version

# # How to run python script by cmd?

# cmd->🔥 python script.py

# # How to run python script with interactive shell by cmd?

# cmd->🔥 python -i script.py

# import os
# # os.system('systeminfo')
# os.system("python --version")

# How to print all python keyword list ?

# import keyword
# print(keyword.kwlist)

#page-31
#Day - 9

#Creating variables and assigning values

# How to print docstring(documentation string) of a function, method, class, or module.

# import math

# print(math.__doc__)


# Output : This module provides access to the mathematical functions
# defined by the C standard.


#Day - 10


# # Here are the available types in Python. Use type() to find out what
# # type your object is. 
# Text Type:          str
# Numeric Types: int, float, complex
# Sequence Types:     list, tuple, range
# Mapping Type:  dict
# Set Types:          set, frozenset
# Boolean Type:  bool
# Binary Types:  bytes, bytearray, memoryview


# Day -10

# Rules for variable naming:

# No need to specify a data type when declaring a variable in Python, Python interpreter automatically picks the most suitable built-in
# data type for it:

# 1. Variables names must start with a letter or an underscore.
# x = True # valid
# _y = True # valid

# 8x = False # invalid (starts with numeral)
# $y = False #invalid (starts with symbol)

# 2. The remainder of your variable name may consist of letters, numbers and underscores.
# has_2_in_it = "Still Valid"

# 3. Names are case sensitive.
# Q = 9
# p = Q*5
# =>NameError: name 'Q' is not defined

#Day-11

# Assignment in python

# When you use "=", name for the object on the left of "=" and assign the reference of the object on the left to the "="

# Which is like :

#           a_name = an_object

#           pi = 3.14


# You can assign multiple values to multiple variables in one line. Note that there must be the same number of
# arguments on the right and left sides of the

#           a, b, c = 1, 2, 3
#           print(a, b, c)

#           # Output: 1 2 3

# Assign a single value to several variables simultaneously

#           a = b = c = 1
#           print(a, b, c)

#           # Output: 1 1 1

# The above is also true for mutable types (like list, dict, etc.)

# x = y = [7, 8, 9] 
# x = [13, 8, 9] 
# print(y) 
# # Output: [7, 8, 9]
# print(x)
# # Output: [13, 8, 9]



# The above is also true for mutable types (like list, dict, etc.)

# Unpack with dummy variable and is conventional to use the underscore (_) for assigning unwanted
# values

#           a, b, _ = 1, 2, 3
#           print(a, b)

#           # Output: 1, 2

# #                   #    PyGems.com
#                #https://www.facebook.com/pygems

# An object is called mutable if it can be changed.

# Examples of immutable Data Types:

# ⚡ int, long, float, complex
# ⚡ str
# ⚡ tuple
# ⚡ frozenset


# An object is called immutable if it cannot be changed in any way.

# Examples of mutable Data Types:

# ⚡ list
# ⚡ set


# Built in Modules and Functions:

# print(dir(__builtins__))


# # To know all the functions in a module we can assign the functions list to a variable, and then print the variable.

# import math

# print(dir(math))


# # For any user defined type, its attributes, its class's attributes can be retrieved using dir().

# class Hello():
     
#      def fullName(self):
#           pass

# print(dir(Hello))

#Day_14

# Single line, inline and multiline comments

# -> Single-line comments begin with the hash character (#) and are terminated by the end of line.

# Single line comment:

# # This is a single line comment in Python

# Inline comment:

# print("Hello! World") # This is inline comment, prints "Hello! World"

# ->Multiple comment have """ or ''' on either end. 

# """
# This type of comment spans multiple lines.
# These
# """

# #Day-16
# #Python Data Types (string) - Part 1

# A string is a sequence of characters enclosed in single ('') or double (" ") quotation marks.
# Note that string is ordered and immutable which means you can access it's elements by index but each time one makes any changes
# to the string, completely new string object will be created.

# Example :

# a_str = 'Hello World'
# b_str = "Hello World"

# # #                   #    PyGems.com
#                #https://www.facebook.com/pygems



# capitalize(),title(),upper(),lower(),casefold()

# #Day-16
# #Python3_Basics
# #Python Data Types (string) - Part 2
# #String methods - capitalize()



# capitalize(): Converts first character of a string to uppercase letter and lowercases all other characters and doesn't take any parameter.

# Example:
#           string = "i love Python."
#           print(string.capitalize())

#           Output : "I love python."


#                              PyGems.com
# #                #https://www.facebook.com/pygems

# title():

# Example:
# string = "i love Python."
# print(string.capitalize())

# Output : "I love python."

# #                   #    PyGems.com
#                #https://www.facebook.com/pygems


###









###


# Day-17
# Python3_Basics
# Python Data Types (string) - Part 3
# String methods - capitalize()

#  title() -  Converts the first character of each word to upper case

# text1 = 'I am a python Developer.'
# text2 = '140202223 bu15 bu*f 25'
# text3 = "He's an python Developer, isn't he?"


# print(text1.title())
# print(text2.title())
# print(text3.title())

# # Output:

# I Am A Python Developer.
# 140202223 Bu15 Bu*F 25
# He'S An Python Developer, Isn'T He?


# # lower() -  Converts a string into lower case


# print(text1.lower())
# print(text2.lower())
# print(text3.lower())

# i am a python developer.
# 140202223 bu15 bu*f 25
# he's an python developer, isn't he?

# #casefold() - Converts string into lower case (aggressive lower())

# ***For example, the German lowercase letter ß is equivalent to ss. However, since ß is already lowercase, the lower() method does nothing to it.
# But, casefold() converts it to ss**

# #  swapcase() - Swaps cases, lower case becomes upper case and vice versa

# print(text1.swapcase())
# print(text2.swapcase())
# print(text3.swapcase())

# Output:

# i AM A PYTHON dEVELOPER.
# 140202223 BU15 BU*F 25
# hE'S AN PYTHON dEVELOPER, ISN'T HE?


# #                   #    PyGems.com
#                #https://www.facebook.com/pygems



# Day-19
# Python3_Basics
# Python Data Types (string) - Part 4
# String methods - Return True or False 

 # isalnum() -  Returns True if all characters in the string are alphanumeric
 # isalpha() -  Returns True if all characters in the string are in the alphabet
 # isdecimal() -  Returns True if all characters in the string are decimals
 # isdigit() -  Returns True if all characters in the string are digits
 # isidentifier() - Returns True if the string is an identifier
 # islower() -  Returns True if all characters in the string are lower case
 # isnumeric() -  Returns True if all characters in the string are numeric
 # isprintable() -  Returns True if all characters in the string are printable
 # isspace() -  Returns True if all characters in the string are whitespaces
 # istitle() -  Returns True if the string follows the rules of a title
 # isupper() -  Returns True if all characters in the string are upper case



#                           #    PyGems.com
#                    #https://www.facebook.com/pygems

# Day-20
# Python3_Basics
# Python Data Types (string) - Part 5
# String methods - index(),rindex(),find(),rfind()

*** index and find methods are almost same except find used for only string but index works with other data types . Another thing both are 
quit different in terms of error handaling ***

string = "Never underestimate the power of python and Python is an extremely versatile language."

#  index() -  Searches the string for a specified value and returns the position of where it was found
string.index("power")

output : 24


#  rindex() - Searches the string for a specified value and returns the last position of where it was found
string.index("python")

output : 33
#  find() - Searches the string for a specified value and returns the position of where it was found
string.index("power")

output : 24
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
string.index("python")

output : 33

Error handaling :
string.index("?")  Output : ValueError: substring not found

string.find("?")  Output : -1



#                           #    PyGems.com
#                    #https://www.facebook.com/pygems

# Python_365
# Day-21
# Python3_Basics
# Python Data Types (string) - Part 6
# String Formating methods : format(),format_map()
#python3
#pygems



# format() - Formats specified values in a string

# Syntex : { }.format(string or value)

# Simple example : 
# str = "I love python"

# print("I love {}".format("python"))
# print("I {} {}".format("love","python"))
# print(str.format("python"))

# Output : 
# I love python
# I love python
# I love python

# Positional argument and Keyword arguments:

# print("I {0} {1}".format("love","python"))
# print("I {1} {0}".format("love","python"))

# print("I {0} {lang}".format("love",lang="python"))


# Output : 
# I love python
# I python love
# I love python

# Space : 

# print("{0:5} love python".format("I"))

# Here 0 is the positon of I and 5 the total space size (inclusive the string size)

# Output :

# I    love python // total 5 spces including I




# format_map() - Formats specified values in a string and used to return an dictionary key’s value.


# a = {'x':'Faiyaz', 'y':'Karim'}
  

# print("{x}'s last name is {y}".format_map(a))

# Output:

# John's last name is Wick


# #                           #    PyGems.com
# #                    #https://www.facebook.com/pygems




# Day-22
# Python3_Basics
# Python Data Types (string) - Part 8 
# String methods 


string = "I Love Python."


#  center() - Returns a centered string

Syntax :
string.center(length, character) // character is optional

string.center(20)
string.center(20,"_")

Output:
   I Love Python.
___I Love Python.___


#  rjust() -  Returns a right justified version of the string
#  ljust() -  Returns a left justified version of the string



                              PyGems.com
                   https://www.facebook.com/pygems




# Day-23
# Python3_Basics
# Python Data Types (string) - Part 9
# String methods 


#  join() - Joins the elements of an iterable to the end of the string

Syntax of the join():   separator.join(iterable)

a = ['1','2','3']

print("-".join(a)) 

Output : 1-2-3

#  split() -  Splits the string at the specified separator, and returns a list

Syntax of the split():   str.split(separator, maxsplit)

string = "I Love. Python."

print(string.split()) # If separator is not provided then any white space is a separator.

print(string.split(".")) # Using . separator

print(string.split(".",0))


Output :

Without any parameter : ['I', 'Love.', 'Python.']
Using separator :       ['I Love', ' Python', '']
Using maxsplit  :       ['I Love', ' Python.']




#  rsplit() - splits string from the right at the specified separator, and returns a list




#                           #    PyGems.com
#                    #https://www.facebook.com/pygems

# Day-24
# Python3_Basics
# Python Data Types (string) - Part 10
# String methods 

txt = "     I love Python      "

#  strip() -  Returns the string by removing both the leading and the trailing characters 

print(txt.strip())
Output  : I Love Python

#  rstrip() - Returns a right trim version of the string
#  lstrip() - Returns a left trim version of the string

txt2 = "One\nTwo\nThree"

#  splitlines() - Splits the string at line breaks and returns a list
print(txt2.splitlines())
Output : ['One', 'Two', 'Three']

#  zfill() -  Fills the string with a specified number of 0 values at the beginning

string = "Mango"

print(string.zfill(10))
Output : 00000Mango


#                           #    PyGems.com
#                    #https://www.facebook.com/pygems



# Day-25
# Python3_Basics
# Python Data Types (string) - Part 11
# String methods 



#  count() -  Returns the number of times a specified value occurs in a string

Syntax : string.count(substring, startIndex, endIndex) 
Note : startIndex, endIndex are optional

txt = "python is popular programming language"
print(txt.count('p'))

print(txt.count('p',5,20))
Output :
4
3

#  replace() -  Returns a string where a specified value is replaced with a specified value
Syntax : str.replace(old, new  count) 
Note :Cont is optional

txt = "abcd abcd abcd"

print(txt.replace('abcd','ABCD'))
print(txt.replace('abcd','ABCD',2))


#  endswith() - Returns true if the string ends with the specified value

#  startswith() - Returns true if the string starts with the specified value

#                           #    PyGems.com
#                    #https://www.facebook.com/pygems



# Day-26
# Python3_Basics
# Python Data Types (string) - Part 12 (Last Part)
# String methods 


#  translate() -  Returns a translated string
#  maketrans() -  Returns a translation table to be used in translations
#  encode() - Returns an encoded version of the string

#                           #    PyGems.com
#                    #https://www.facebook.com/pygems