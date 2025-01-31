# age_number is equal to a float (decimal) number from asking for an age. Then it prints the type to verify its a float
age1 = float(input("Enter age of First Friend: "))
print(type(age1))
age2 = float(input("Enter age of Second Friend: "))
print(type(age2))
age3 = float(input("Enter age of Third Friend: "))
print(type(age3))
age4 = float(input("Enter age of Fourth Friend: "))
print(type(age4))
age5 = float(input("Enter age of Fifth Friend: "))
print(type(age5))

#Gets the float ages from before and adds
total_age = age1 + age2 + age3 + age4 + age5

#Gets total age from before and divides
average_age = total_age / 5

#Prints a message and the average age
print(f"The average age of your friends is:  {average_age}")
