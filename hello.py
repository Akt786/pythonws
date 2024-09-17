#To print your name
from calendar import c


print("Ashish")

#to print your name using user input
name = input("Enter your name")
print(name)

#WAP to find the current age
currentYear = int(input("Enter the current year"))
bornYear = int(input("Enter the born year"))
ageInYear = currentYear - bornYear
print(ageInYear)

#WAP for currency converter
print("Convert rupees into dollars")
rupeesAmount = int(input("Enter the amount in Rs."))
rsIntoDollar = (rupeesAmount/84)
print(rsIntoDollar)

print("Convert dollars into rupees")
dollarsAmount = int(input("Enter the amount in dollars"))
dollarintors = (dollarsAmount*84)
print(dollarsAmount,"convert into rs", dollarintors);

#WAP to check that you are eligible for voting or not
userAge = int(input("Enter your age"))
#for voting you must greater than 17
if (userAge > 17):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
#WAP to check the user eligible for job application
# if gender is female and age is greater than 17
# if gender is male they can apply for private job
userAge = int(input("Enter the user age"))
userGender = input("Enter your gender")

#method 1
if(userAge > 17 and userGender == "female"):
   print("you r eligible govt job")
elif(userAge > 17 and userGender == "male"):
   print("you r eligible private job")
else:
    print("you r not eligible any job")

#method2
if(userAge > 17):
    if(userGender == "female"):
       print("you r eligible govt job")
    elif(userGender == "male"):   
        print("you r eligible private job")
else:
    print("your gender not exists")


#WAP to check the greatest no among 3 no
# a = int(input("Enter a value"))
# b = int(input("Enter b value"))
# c = int(input("Enter c value"))
a = 5 
b = 6
c = 7
#check the greatest value in a,b,c
if(a > b and a > c):
    print("A is greatest no")
elif (b > a and b > c):
    print("B is greatest no")
else:
    print("C is greatest no")


#Switch condition is replacement of multiple if else block

friendname = {"Ashish" , "Vivek" , "Aman" , 1,2,3, 1}
# print(type(friendname)) 
# friendname

# print(friendname)

#to add the new friend name in list

#print after adding name
print("After", friendname)
#to add the name in specific position

#print after adding name at 0 index
print("Add name at index 0", friendname)
#to remove the name from list

#print after removing name from the list
print(friendname)
#to clear the list
#friendname.clear()
#print(friendname)
#To remove the data in list with specific index
#friendname.pop(2)
#print(friendname)
#To sort the list
# friendname.sort()
# print(friendname)

#to print element in the given list
for names in friendname:
    print(names)

#to print the 1 to 10
# for(int x = 0; x < 11; x++)
# for x in range(1,11);
#     print(x)

#to print the even no from 1 to 10
for evenNo in range(2, 11, 2):
    print(evenNo)

#to print the even no 1 to 10 using for and if
# for no in range(1, 11):
#     if no % 2 == 0;
#         print(no)

#sets used to store the data and data is changeable
sets = {"pawan", "ivan", "anshu", "ivan"}
sets.add("harsh")
sets.remove("harsh")
# sets[0] = "gfnfh"
print(sets)
print(type(sets))

#to add the name of 5 friends using list, sort and traverse
# Step 1: Create a list of five friends
friends = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

# Step 2: Sort the list in alphabetical order
friends.sort()  # We can also use sorted(friends) to return a new sorted list without changing the original list

# Step 3: Traverse and print the sorted list
for friend in friends:
    print(friend)


#while print 1 to 10
i = 0
# while i < 11:
#     print(i)
#     break
#     i= i+1

while i < 11:
    i= i+1
    print(i)
    continue
#function in python
#create function to print statement
def myfunction():
    print("my function called")

#call the function by name
myfunction()

#create function to print statement
def myFunction(x,y):
    z= x*y
    print("area is",z)

#call the function by name
myFunction(2,4)
width = int(input("Enter the width"))
height = int(input("Enter the height"))

area = myFunction(width,height)
print("the area is", area)
    


 


    




import datetime
x = datetime.datetime.now()
print(x.month)







# To create new file and add my name also close the file
# Open the file in write mode and write to it
with open("harsh.txt", "w") as f:
    f.write("My name is harsh tyagi")

# Open the file in write mode again to overwrite the previous content
with open("harsh.txt", "w") as f:
    f.write("My name is harsh tyagi, I'm an MCA student")

# Open the file in read mode to read the content
with open("harsh.txt", "r") as f:
    content = f.read()

print(content)


#to enter your name, email id and college name
name = input("Enter your name")
email = input("Enter your email")
collegeName = input("Enter your college name")
data = name + email + collegeName

#how to delete the file
import os

# Correct function to remove a file
os.remove("harsh.txt")

# With the help of date time function giving current age
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Replace these values with your birthdate
birthdate = datetime(2001, 12, 1)  # Format: year, month, day

age = calculate_age(birthdate)
print(f'Your current age is: {age}')



