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



# #                    #    PyGems.com



#      # PIP(Freeze) --> Python package management system (Part-3) 

#      **** Used for export installed modules and reinstall ****

#          1. See Installed Packages with version 

#                 --👀> pip Freeze

#         2. Export Installed Packages into txt file

#                 --👀> pip Freeze > requirements.txt

#         3. Install packages from a text file (exported by Freeze) 

#                 --👀>  pip install -r requirements.txt
    




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

import math

print(math.__doc__)


Output : This module provides access to the mathematical functions
defined by the C standard.


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