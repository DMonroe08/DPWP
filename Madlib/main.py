__author__ = 'DanielleMonroe'

name = raw_input("Enter your name?  ")
some = raw_input("Pick a number between 2-16. ")
color = raw_input("What is your favorite color?  ")
number = raw_input("Give me a number between 8-22.  ")
fight = raw_input("How afraid of spiders are you? ")
flight = raw_input("Pick a number between 4-7. ")


people = ["Lulu", "George"]
people.append(name)

scream = dict()
scream = {"Yell":"AAAAHHHH", "Stomp":"SQUISH!!"}

jep1 = 200
jep2 = 400


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

i = 0
while i<4:
    react
    i = i+1

def spider(l, w):
    size = l + w
    return size

ss = spider(3, 5);

story = '''
{people} are contestants on Jeopardy. {name} is very short {color} hair.
{name} gets to select first and chooses {cat} for {jep1}.
{name} {ans}. Before the next answer could be said, {name} noticed a spider on the console.
{name} yelled {react} because they {fight} afraid spiders. The spider was {ss} inches big.

'''
print story.format(**locals())