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
rupeesAmount = int(input("Enter the amount in Rs"))
rsIntoDollar = (rupeesAmount/84)
print(rsIntoDollar)

print("Convert dollars into rupees")
dollarAmount = int(input("Enter the amount in dollars"))
dollarIntors = (dollarAmount*84)
print(dollarAmount, "convert into rs", dollarIntors);

#WAP to check that you are eligible for voting or not
userAge = int(input("Enter your age"))
#for voting you must be greater than 17
if (userAge > 17):
     print("You are eligible for voting")
else:
     print("You are not eligible for voting")

#WAP to check user eligible for job application
# if gender is female and age is greater than 17
# if gender is male they can apply for private job
userAge = int(input("Enter your Age"))
userGender = input("Enter your gender")

#method1
if(userAge > 17 and userGender == "female"):
     print("you are eligible for govt job")
elif(userAge > 17 and userGender == "male"):
     print("you are eligible for private job")
else:
     print("you are not eligible for job")

#WAP to check the greatest no. among 3 no.
# a = int(input("Enter a value "))
# b = int(input("Enter b value"))
# c = int(input("Enter c value"))
a = 7
b = 6
c = 5
#check the greatest value in a,b,c
if(a > b and a > c):
     print("a is the greatest no.")
elif(b > a and b > c):
     print("b is the greatest no.")   
else:
     print("c is the greatest no.")       

#Switch condition is replacement of multiple if else block

friendname = {"Ashish" , "Vivek" , "Aman" , 1,2,3,1}
print(type(friendname))

friendname
print(friendname)

#to add the new friend name in list

#print after adding name
print("After", friendname)

#to add the name in specific position

#print after adding name at 0 index
print("Add name at index 0", friendname)
#to print element in the given list
for names in friendname:
     print(names)


    


       





































