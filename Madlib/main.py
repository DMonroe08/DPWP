__author__ = 'DanielleMonroe'

#Strings
#These are variable that are created by the users and effect the conditional statements below
name = raw_input("Enter your name?  ")
some = raw_input("Pick a number between 2-16. ")
color = raw_input("What is your favorite color?  ")
number = raw_input("Give me a number between 8-22.  ")
fight = raw_input("How afraid of spiders are you? ")
flight = raw_input("Pick a number between 4-7. ")

#Array
#Gives the predetermined names of the contestants and adds the user name
people = ["Lulu", "George"]
people.append(name)

#Dictionary
scream = dict()
scream = {"Yell":"AAAAHHHH", "Stomp":"SQUISH!!"}

#Numbers
jep1 = 200
jep2 = 400
ft = 3

#Mathematical operator
#Calculates how much of a prize the winner and losers receive
win = (jep1 + jep2) * ft

lose = (jep2 - jep1) / ft

#Conditional Statements
#Each conditional statement gives a text result in the paragraph based on the numerical value given
if some > 12:
    ans = "answered correctly"
else:
    ans = "answered incorrectly"


if number < 18:
    cat = "DOGS"
else:
    cat = "CATS"

#This condition results in a string placed in the Madlib depending on what number they put in when asked the questions in the beginning in the "flight" section
if flight < 6:
    react = scream["Yell"]

else:
    react = scream["Stomp"]

#Loop
#This loop repeats "welcome to jeopardy" Before the "story" section starts
hi = "Welcome to Jeopardy"
i = 0
while i < 4:
    print hi
    i = i+1



#Function
#This function calculates the size of the spider that is then placed into the paragraph
def spider(l, w):
    size = l + w
    return size

ss = spider(3, 5);

#This is the madlib that compiles all of the variables, conditions, loops, etc into a story
story = '''
{people} are contestants on Jeopardy. {name} is {ft} feet tall, round, and has {color} hair.
{name} gets to select first and chooses {cat} for {jep1}.
{name} {ans}. Before the next answer could be said, {name} noticed a {ss} inch spider on the console.
{name} yelled {react} because they {fight} afraid spiders.
The spider crawled on {name} and they all yelled "EEWWWW!!!".
{name} then passed out for 10 minutes. Out of nowhere the a {cat} came and peed on {name}'s leg.
Afterwards, {name} decided that she wanted {cat} for {jep2} and won the game.
{name} won {win} golden monkeys when everybody else got to take home {lose} paper clips.

'''
print story.format(**locals())


#This loop prints out that each contestant hates spiders
cont = ["Alex", "Lulu", "George"]
for c in cont:
    print c + " now hates spiders"