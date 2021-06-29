balance=0
QUESTIONS=["What is the capital of the UAE?","How many emirates are there in the UAE?"]
OPTIONS=[["Abu Dhabi","Dubai","Sharjah","RAK"],["3","5","7","8"]]
ANSWERS=[0,2]
AMOUNTS=[100,200,300,400,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]



print("Welcome to our show: Who wants to be a millionare?")
name=input("May I know your name?")
print("Nice to meet you, "+name+"!")
whattodo=input("What will you do when you win the 1,000,000 AED? 1:Invest it, 2:Buy 1M meals, and feed the hungry, 3: Buy a fancy car, 4: Travel the world, 5: Keep it in the bank")
if whattodo=="1":
    print("Wow! Nice option! Make sure you diversify your investment")
elif whattodo=="2":
    print("Mashallah! God bless you! What a kind act")
elif whattodo=="3":
    print("Enjoy! But you can probably find something as fancy with less money")
elif whattodo=="4":
    print("You will take me with you, right? Enjoy anyways")
else:
    print("You might think it's safe to do that, but with inflation, you will lose the value of the money!")
for index in range(len(QUESTIONS)):
    question=QUESTIONS[index]
    print(question)
    options=OPTIONS[index]
    print("1: ",options[0])
    print("2: ",options[1])
    print("3: ",options[2])
    print("4: ",options[3])
    answer=int(input("What is your answer: 1-4?"))-1
    if answer==ANSWERS[index]:
        print("Excellent job!")
        print("You won",AMOUNTS[index]," AED")
    else:
        print("Sorry ! Wrong answer")
        break


