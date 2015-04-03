__author__ = 'DanielleMonroe'


#one lined comments
'''
Doc strings
'''

first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your name  ")
#print "hello there,",  response

birth_year = 1984
current_year = 2015
age = current_year - birth_year
#print "You are " + str(age) + " years old"

budget = 90
if budget > 100:
    brand = "Nike"
    #print "Yay! We can buy cool" + brand + "shoes!"
elif budget > 50:
    #print "We can at least get some generic sneakers"
    pass
else:
    #print "No cool shoes for me."
    pass

characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi won")
#print characters[0]


movies = dict() #creat dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

#Loops

#While Loop
'''
i = 0
while i<9:
    print "The count is", i
    i = i+1


 #For Loop
for i in range (0,9):
    print "the count is", i
    i = i+1

'''

#"For Each" Loop
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    #print "One of the best rappers is " + r
    pass

#Functions

x = 2

def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40);
#print "My area is " + str(a) + " sqft"
#print a


title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message = message.format(**locals())
print message