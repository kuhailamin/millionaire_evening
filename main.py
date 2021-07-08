import random
from playsound import playsound
QUESTIONS=[]
handle = open("Question_backup.txt", "r")
for line in handle:
    info=line.split(",")
    question={
        "question":info[0],
        "options":[info[1],info[2],info[3],info[4]],
        "answer":int(info[5])
    }
    QUESTIONS.append(question)

# close hello.txt
handle.close( )

AMOUNTS=[100,200,300,400,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]


print("I'm George Gherdahi. Welcome to Who Wants to Be a Millionare.")
name=input("Introduce yourself to the audience")
print("Welcome "+name+" to the show! We are excited to have you!")
answer=input("So, tell us. What will you do if you win the million dirhams? 1: Invest it, 2: Buy one million meals and feed the hungry, 3: Travel the world, 4: Buy a fancy car, 5: Save it in the bank")
if answer=="1":
    print("Wow! smart idea! Good luck")
elif answer=="2":
    print("You are a rare gem! Very generous! We need people like you! God bless you")
elif answer=="3":
    print("Nice! But, do you need 1M Drhs for that? Interesting")
elif answer=="4":
    print("I'm sure you will enjoy it, but really 1 Mh Drhs for a car? Why? You can rent it for a month for much less money")
elif answer=="5":
    print('You should reconsider! Because money loses value as time passes by. Besides, money is either digits in the bank or a piece of paper')
num_questions=5
for i in range(5):
    index=random.randint(0,num_questions-1)
    Q=QUESTIONS[index]
    del QUESTIONS[index]
    print(Q["question"])
    Options=Q["options"]
    print("Option 1:",Options[0])
    print("Option 2:", Options[1])
    print("Option 3:", Options[2])
    print("Option 4:", Options[3])
    answer=int(input("What is the answer? 1-4"))
    answer=answer-1
    if answer==Q["answer"]:
        print("Well done! You got ",AMOUNTS[index])
    else:
        print("Sorry. You lost")
        playsound('disappointed.mp3')
        break
else:
    print("Congratulations! you won the million dirhmas")
    playsound('applaud.mp3')

