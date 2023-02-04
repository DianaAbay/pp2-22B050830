#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)  #['Ford', 'Volvo', 'BMW']

#Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)  #Ford

#Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)  #['Toyota', 'Volvo', 'BMW']

#Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)  #3


#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
"""Output:
Ford
Volvo
BMW"""

#Adding Array Elements
#Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)  #['Ford', 'Volvo', 'BMW', 'Honda']


#Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)  #['Ford', 'BMW']

#Delete the element that has the value "Volvo":
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)  #['Ford', 'BMW']