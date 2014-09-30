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
#print characters[0]

movies = dict() # create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the lambs":"Hanibal Lecture"}
#star wars is the key pointing to darth vader value
print movies["Star Wars"]

'''
#While Loop--------

i = 0
while i<9:
    print "The count is", i
    i = i+1



#For Loop--------
for i in range(0,10):
    print "The count is", i
    i = i+1
# the count will stop at 9

'''

#For Each Loop
rappers = ["Tupac", "NAS", "Eminem"]
for r in rappers:
    print "One of the best rappres is " + r
    pass

#Functions --------

x = 2

def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft"
print a



















