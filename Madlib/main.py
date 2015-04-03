__author__ = 'DanielleMonroe'

#Strings
name = raw_input("Enter your name?  ")
some = raw_input("Pick a number between 2-16. ")
color = raw_input("What is your favorite color?  ")
number = raw_input("Give me a number between 8-22.  ")
fight = raw_input("How afraid of spiders are you? ")
flight = raw_input("Pick a number between 4-7. ")

#Array
people = ["Lulu", "George"]
people.append(name)

#Dictionary
scream = dict()
scream = {"Yell":"AAAAHHHH", "Stomp":"SQUISH!!"}

#Numbers
jep1 = 200
jep2 = 400
ft = 3

#Conditional Statements
if some > 12:
    ans = "answered correctly"
else:
    ans = "answered incorrectly"


if number < 18:
    cat = "DOGS"
else:
    cat = "CATS"


if flight < 6:
    react = scream["Yell"]

else:
    react = scream["Stomp"]

#Loop
i = flight
while i<7:
    react
    i = i+1

#Function
def spider(l, w):
    size = l + w
    return size

ss = spider(3, 5);

story = '''
{people} are contestants on Jeopardy. {name} is {ft} feet tall, round, and has {color} hair.
{name} gets to select first and chooses {cat} for {jep1}.
{name} {ans}. Before the next answer could be said, {name} noticed a {ss} inch spider on the console.
{name} yelled {react} because they {fight} afraid spiders.
{name} then passed out for 10 minutes. Out of nowhere the a {cat} came and peed on {name}'s leg.
Afterwards, {name} decided that she wanted {cat} for {jep2} and won the game.

'''
print story.format(**locals())