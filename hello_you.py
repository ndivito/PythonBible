#Ask user for name
name = input("What is your name?: ")
print(name)

#Ask user for their age
age = input("How old are you?: ")
print(age)

#Ask user for their city
city = input("What city do you live in?: ")
print(city)

#Ask user what they enjoy
love = input("What do you love doing?: ")
print(love)

#Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}".format(name,age,city,love)


#Print output to the screen
print(string)
