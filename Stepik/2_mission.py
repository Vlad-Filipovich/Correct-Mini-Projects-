# Magic Ball 8
from random import *

answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
           "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.",
           "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.",
           "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.",
           "Yes – definitely.", "You may rely on it."]
print("Hello world, I'm Magic Ball 8 and I know all the answers", '\n')


def magic_ball_8():
    while True:
        print("What's your name?")
        name = input()
        print("Nice to meet you", name)
        print("Now you can ask me anything!!!", "What do you want to know about?", sep='\n')
        question = input()
        print(choice(answers))
        print("Is there anything else you want to ask?")
        Y_N = input()
        if Y_N.lower() == 'yes':
            continue
        else:
            break
