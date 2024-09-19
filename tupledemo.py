#tuples can store the multiple data and data can't change
# Define the tuple
myTuple = ("Ivan", "Anshu", "Wani", "Anjani", "Wani")

# Print the tuple
print(myTuple)

# Print the type of the tuple
print(type(myTuple))

# Access the element at index 1 using square brackets
print(myTuple[1])  # This will print "Anshu"

# Access the element at index 1 again using square brackets
print(myTuple[1])  # This will print "Anshu" again


# myTuple(1) = "Adarsh"
# print(myTuple)

for item in myTuple:
   print(item)

#dictionary can store multiple data in key value pair
myDict = {
      "name": "ashish tyagi" ,
       "email": "ashishkrthakur955@gmail.com",
       "mobile": "8789650922"
}
print(type(myDict))

print(myDict)

for item in myDict:
    print(item)



print(myDict.get("keys"))

# Correctly modify the value associated with the key "name"
myDict["name"] = "Adarsh"

# Print the updated dictionary to verify the change
print(myDict)

#oops
#class and object

class Mohit:
    age = 20
    print("im from delhi")

#create object and pass class properties
mohit = Mohit()
print(mohit.age)

bornYear = int(input("Enter born year"))
currentYear = int(input("Enter current year"))
class AgeCalculator:
    ageInYear = currentYear - bornYear
    dob = "19 feb 1991"
age = AgeCalculator()
print(age.ageInYear, age.dob)


#polymorphism method overloading
def age(dob):
    print(dob)

def age(dob, name):
    print(dob, name)

# Call the function with both arguments
x = age("19 oct 1991", "Unknown Name")  # Provide a default or placeholder value for `name`
y = age("20 feb 2024", "Wani Sharma")


     




   


   

