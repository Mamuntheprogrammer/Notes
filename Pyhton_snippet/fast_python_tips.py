alist = [1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
 31, 32, 33, 34, 35, 36, 37, 38, 300, 40, 41, 42, 43, 44, 45, 
 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 
 63, 64, 65, 66, 67, 68, 69,70]

# Tips 1: Always look for builtin function to solve probelm

# find the length of list :
len_of_list = 0
for element in alist:
	len_of_list +=1
print(len_of_list)

# Short Solution:
print(len(alist))



# Tips 2: filter a list 

output = []

for element in alist:
	if element % 2 ==0:
		output.append(element)
print(output)

# Short Solution:

print(list(filter(lambda X: X % 2==0,alist)))

# most short solution 
print([item for item in alist if item %2 ==0])


# Tips 3: Membership testing

# Note that set is faster than list

def check_member(num):
	for item in alist:
		if item==num:
			return True
	return False

print(check_member(300))

# Short Solution: if your element is located at last of list than it is not short solution . see the next


print(300 in alist)


#Very Short Solution: for big range data convert data to any data

make_Set = set(alist)
print(300 in make_Set)

# Tips 4: Remove duplicates

unique = []

for element in alist:
	if element not in unique:
		unique.append(element)

print(unique)

# Short Solution: note that set is not orderedic method
print(set(alist))


# Tips 5: Sort list

print(sorted(alist))

# Short Solution:

alist.sort()
print(alist)


# Tips 6: 1000 operation and 1 Fi=unction

def square1(num1):
	return num1 **2
print([square1(i) for i in range(10)])

# Short Solution:

def square2():
	return [i**2 for i in range(10)]
print(square2())

# Tips 7: Checking for True same as False

if variable == True:

# Faster solution

if variable is True:

# More Faster solution

if variable: # for true
 
if not variable: # for False

# example : checking a empty list 

if len(alist)==0:

# faster 
if alist == []

# more faster 

if not alist:

# Tips 8: create a empty list   list() or []

list()

# faster 
[]


# Tips 9 : asiginig variable

a=2
b=4

# faster 

a,b = 2,4


# Tips 10 : local variable are more faster than working with global variable

output = []

def Oddn()
	for element in alist:
		if element % 2 ==0:
			output.append(element)
print(output)


# faster 



def Oddn():
	output = []
	append = output.append
	for element in alist:
		if element % 2 ==0:
			append(element)
print(output)

