# this is just for understanding and for understanding basic feature and operations in python
# Asking user to enter first number then we will ask second number then we will sum first and second and get the addition
'''First_number = input("Enter the first number :")
Second_number = input("Enter the second number :")
Sum = float(First_number) + float(Second_number)

print("Sum :" + str(Sum)) 
'''

# this is to use if else conditions and check the weight in kg or lbs
#we will enter weight and then we will choose weather we want to see weight in kg or lbs or covert our own weight into kg or lbs

'''
Weight = int(input("Enter your weight:"))

Weight_unit = str(input("(K)g or (L)bs:"))

Kilo  = Weight/0.453592
lbs  = Weight*0.45
if Weight_unit.upper() == "K":
  print("Weight in lbs:" + str(Kilo))
elif Weight_unit.upper() == "L":
  print("Weight in kg:" + str(lbs))

'''

# Write Python3 code here

class car():
	
	# init method or constructor
	def __init__(self, model, color):
		self.model = model
		self.color = color
		
	def show(self):
		print("Model is", self.model )
		print("color is", self.color )
		
# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()	 # same output as car.show(audi)
ferrari.show() # same output as car.show(ferrari)

# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)
