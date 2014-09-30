#one lined comments
'''
Doc Strings
'''

first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name")
#print "Hello there, ", response

birth_year = 1985
current_year = 2014
age = current_year - birth_year
print "You are " + str(age) + " years old"

budget = 90
#change to 90 prints the else statement

if budget > 100:
    brand = "NIKE"
    #print "Yay! We can buy cool " + brand + " shoes!"
elif budget > 50:
    #print "We can at least get some generic sneakers"
    pass
else:
    pass

characters = ["stacy", "matthew", "tyler", "cannon"]
characters.append("Daffy Duck")
print characters

