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



                              PyGems.com
                 https://www.facebook.com/pygems








# Python_365
# Day-27
# Python3_Basics
# Python Data Types : String
# Solving String related problems: (src : hackerrank) 
# Problem title :String Split and Join

""" 
Problem description : You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input: this is a string   
Sample Output: this-is-a-string

"""

def split_and_join(line):
    return "-".join(line.split(" "))


split_and_join("this is a string")


                              PyGems.com
                 https://www.facebook.com/pygems



# Python_365

# Day-28

# Python3_Basics

# Python Data Types : String

# Solving String related problems: (src : hackerrank) 

# Problem title : Find a string

#hackerrank 

#python 
""" 
Problem description : In this challenge, the user enters a string and a substring.
 You have to print the number of times that the substring occurs in the given string. 
 String traversal will take place from left to right, not from right to left.


Sample Input:

ABCDCDC
CDC

Sample Output :

2

"""

def count_substring(a, b):
    count=0
    for x in range(len(a)-len(b)+1):
        if a[x:x+len(b)]==b:
            count+=1
    return count

count_substring("ABCDCDC","CDC")

Output : 2



                              PyGems.com
                 https://www.facebook.com/pygems