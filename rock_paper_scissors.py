import random
You_str = (input("Enter you'r choice: "))
computer_str = random.choice([0, 1, 2])
dic = {
    "rock" : 0,
    "paper" : 1,
    "scissor": 2
}
rev_dic = {
    0 : "rock",
    1 : "paper",
    2 : "scissor"
}
You = dic[You_str]
computer = computer_str
print(f" =>You choose {You_str} \n =>Computer choose {rev_dic[computer]}")
if(You == computer):
    print("Ohho It's a draw mate, guess u have to try again")

else:
    if(You==1 and computer==0):
        print("Yoooo Congrats mate!!, you have just won nothing xd anyway, GOOD JOB")
    elif(You==0 and computer==2):
        print("Yoooo Congrats mate!!, you have just won nothing xd anyway, GOOD JOB")
    elif(You==2 and computer==1):
        print("Yoooo Congrats mate!!, you have just won nothing xd anyway, GOOD JOB")
    elif(You==0 and computer==1):
        print("Ahhhh, Bad luck mate Better Luck Next Time")
    elif(You==1 and computer==2):
        print("Ahhhh, Bad luck mate Better Luck Next Time")
    elif(You==2 and computer==0):
        print("Ahhhh, Bad luck mate Better Luck Next Time")
