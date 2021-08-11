# import turtle

# class Polygon:
# 	def __init__(self,name,sides):
# 		self.name = name
# 		self.sides = sides
# 		self.interor_angles = (self.sides-2)*180
# 		self.angle = self.interor_angles/self.sides
# 	def draw(self):
# 		for x in range(self.sides):
# 			turtle.forward(100)
# 			turtle.right(180-self.angle)
# 		turtle.done()

# class Test(Polygon):
# 	def __init__(self,name,sides,one):
# 		self.one = one 
# 		super().__init__(name,sides)

# tx = Test("one", 4, "one1")

# print(tx.one)

# Video Link : https://youtu.be/vgeTzWo0pXg


# How every thing is object in python?
# 1. What Is OOP
# 2. What is OOP Part 2
# 3. Creating Our Own Objects

"""
Naming convention : Use capital letter  and camel case for class name 
keywords : Class,Instantiat,Instance
"""
class BigObj:
	pass

obj1 = BigObj()


# 4. Attributes and Methods
# 5. __init__

class PlayerCharacter:
	membership = True  # this is class object attribute .

	def __init__(self,name,age):
		self.name = name  #These are attributes , own by every object created from this class
		self.age = age

	def run(self): # method 
		print("Run")

obj1 = PlayerCharacter("Player1",33)
obj2 = PlayerCharacter("Player2",34)

obj1.attack = 50

print(obj1.age)
print(obj1.attack)




# 6. @classmethod and @staticmethod


class ClassAndStatic:

	def __init__(self,name,age):
		self.name = name
		self.age = age

	@classmethod
	def add1(cls,one,two):
		return one+two

	""" class method can access wihtout creating object , access by the class name 
	And another thing to remember most of the time you have to use class method to instantiate a class by 
	creating an object """

	@classmethod
	def add2(cls,one,two):
		return cls("mamun",one + two)


	""" the static method never care about class attributes"""

	@staticmethod
	def add3(one,two):
		return one + two



print(ClassAndStatic.add1(2,3))

obj3 = ClassAndStatic.add3(3,4)

print(obj3)

# 7. Reviewing What We Know So Far


# 8. DEVELOPER FUNDAMENTALS V


# 9. Encapsulation

'''
 encapsulation refers to the bundling of data with the methods that operate on that data, 
 or the restricting of direct access to some of an object's components
 example :
 class attributes and methods 
'''

# 10. Abstraction

'''
it is process of hiding implementation details and 
only showing the functionality to the user. 
Abstraction focus on what the object does instead of how it does.
'''


# 11. Private vs Public Variables

# 12. Inheritance

# 13. Inheritance 2

# 14. Polymorphism

# 15. super()

# 16. Object Introspection
# 17. Dunder Methods

# 18. Exercise Extending List
# 19. Multiple Inheritance
# 20. MRO - Method Resolution Order


