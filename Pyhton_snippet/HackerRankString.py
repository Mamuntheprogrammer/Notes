# Python_365
# Day-26
# Python3_Basics
# Python Data Types : String
# Solving String related problems: (src : hackerrank) 
# Problem title : sWAP cASE


""" 
Problem description : 
You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa.

Input and Output example :

input : Www.HackerRank.com 

Output : wWW.hACKERrANK.COM

"""
# Solution 1 :

def swap_case(s):
	d = ''
	for x in s:
		if (x.isupper()==True):
			d+=x.lower()
		else:
			d+=x.upper()
	return d

print(swap_case("Hello moZur"))



# Solution 2:

print(''.join(list(map(lambda x: x.upper() if x.islower() else x.lower(),"Hello moZur"))))



                           #    PyGems.com
                 #https://www.facebook.com/pygems








# Python_365
# Day-26
# Python3_Basics
# Python Data Types : String
# Solving String related problems: (src : hackerrank) 
# Problem title : 


""" 
Problem description : 

Input and Output example :

input : 

Output : 

"""