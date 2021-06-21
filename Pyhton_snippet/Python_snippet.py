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

# Day-6

#       # Update all installed python packages with pip-review

#       Step 1 : Install pip-review 

#                 🔥 --> pip isntall pip-review

#       Step 2 : View Packages update information

#                 🔥 --> pip-review

#       Step 3 : Update all Packages

#                 🔥 --> pip-review --interactive


import dis

def foo():
     print("hello")


print(dis.dis(foo))