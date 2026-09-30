import random
import time
user = 1
def int_convert(user,i):
    while True:
        user = input(i)
        if user.isdigit() == True:
            user = (float(user))
            return user
        elif user.isdigit() == False:
            print("Try again")
min = (int(int_convert(min,"Enter min value: ")))
max = (int(int_convert(max,"Enter max value: ")))
num = 1.1
cmin = min
cmax = max
compg = []
userg = []
rnum = random.randint(min,max)
def computer_guess(num,cmin,cmax,compg,rnum):
    while True:
        num = cmin + cmax
        num =  (float(num))
        num = num//2
        compg.append(num)
        if num == rnum:
            return num
        elif num > rnum:
            cmax = num-1
        elif num< rnum:
            cmin = num+1

while True:
    user = int_convert(user,"Enter your Guess: ")
    if user > rnum:
        print("Too High, try again")
        userg.append(user)
    elif user < rnum:
        print("Too Low, try again")
        userg.append(user)
    elif user == rnum:
        print("CORRECT!")
        userg.append(user)
        break
    else:
        print("error")

num = computer_guess(num,cmin,cmax,compg,rnum)
print (f"\n---AI Stats---\nGuesses: {compg}\nNumber of guesses: {len(compg)}")
print (f"\n---Your Stats---\nGuesses: {userg}\nNumber of Guesses: {len(userg)}")
if len(userg) < len(compg):
    for i in ("The Winner Is..."):
        print(i,end="",flush=True)
        time.sleep(.2)
    print(" ")
    print("YOU!")
elif len(userg) > len(compg):
    for i in ("The Winner Is..."):
        print(i,end="",flush=True)
        time.sleep(.2)
    print(" ")
    print("AI!")   
elif len(userg) == len(compg):
    for i in ("The Winner Is..."):
        print(i,end="",flush=True)
        time.sleep(.2)
    print(" ")
    print("The friends we made along the way")
    time.sleep(1)
    print("It's a Tie!")
else:
    print("error")
    