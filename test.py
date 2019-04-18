from random import shuffle,randint
from collections import deque
import time
from tqdm import tqdm
import os
from animation_spin import animation,start_art
import numpy as np



class Player:
    def __init__(self,n):
        self.n = n

class Slotmachine:
    def __init__(self,cost):
        self.a = deque(["★","$","♚","☻","➓","☛","✔"])
        self.b = deque(["★","$","♚","☻","➓","☛","✔"])
        self.c = deque(["★","$","♚","☻","➓","☛","✔"])
        self.n = len(self.a)
        self.middle = None
        self.price = cost
        self.turn = 0

    def complete_wheel(self):
        size = self.n
        numb = [20,1,1,1,1,1,1]
        i = 0
        for ele in range(self.n):
            for _ in range(numb[i]):
                self.a.append(self.a[ele])
                self.b.append(self.b[ele])
                self.c.append(self.b[ele])
            i += 1
        self.n = len(self.a)

    def print_list_check(self):
        print(self.a)
        print(self.b)
        print(self.c)

    def count_ele(self):
        a = ["★","$","♚","☻","➓","☛","✔"]
        for ele in a:
            print(self.a.count(ele))
        print(len(self.a))

    def randomnize(self):
        shuffle(self.a)
        shuffle(self.b)
        shuffle(self.c)

    def spin(self):
        self.a.rotate(1)
        self.b.rotate(-1)
        ra = randint(1,5)
        if ra == 1:
            self.c.rotate(-2)
        elif ra == 2:
            self.c.rotate(-1)
        elif ra == 3:
            self.c.rotate(1)
        elif ra == 4:
            self.c.rotate(2)

    def check_win(self):
        if self.a[self.middle] == self.b[self.middle] and self.a[self.middle] == self.c[self.middle]:
            print(" Winner !")
            return (True,self.a[self.middle])
        else:
            return (False,None)
    
    def print_wheel(self):
        os.system("clear")
        self.middle = int(self.n / 2)
        row1 = [" ", " "] + [self.a[self.middle - 2],self.b[self.middle - 2],self.c[self.middle - 2]] + [" " , " "]
        row2 = [" ", " "] + [self.a[self.middle - 1],self.b[self.middle - 1],self.c[self.middle - 1]] + [" " , " "]
        row3 = ["⇨", " "] + [self.a[self.middle],self.b[self.middle],self.c[self.middle]] + [" ", "⇦"]
        row4 = [" ", " "] + [self.a[self.middle + 1],self.b[self.middle + 1],self.c[self.middle + 1]] + [" " , " "]
        row5 = [" ", " "] + [self.a[self.middle + 2],self.b[self.middle + 2],self.c[self.middle + 2]] + [" " , " "]
        
        print(" ".join(row1))
        print(" ".join(row2))
        print(" ".join(row3))
        print(" ".join(row4))
        print(" ".join(row5))

    def winnings(self,s):
        if s == "★":
            print("You just won: ",3 * self.price)
            return 3 * self.price
        elif s == "$":
            print("You just won: ",5* self.price)
            return 5* self.price
        elif s == "♚":
            print("You just won: ",10* self.price)
            return 10* self.price
        elif s == "☻":
            print("You just won: ",50* self.price)
            return 50* self.price
        elif s == "➓":
            print("You just won: ",100* self.price)
            return 100* self.price
        elif s == "☛":
            print("You just won: ",200* self.price)
            return 200* self.price
        elif s == "✔":
            print("You just won JACKPOT: ",1000000* self.price)
            return 1000000* self.price

def main_game():
    #print("Loading Game ...")
    #for i in tqdm(range(100)):
    #    time.sleep(0.05)
    os.system("clear")
    start_art()
    os.system("clear")

    n = 0
    while True:
        try:
            n = int(input("How much money do you want to input: "))      
        except ValueError:
            print("Not an integer! \n")
            continue
        else:
            break

    while n < 2:
        os.system("clear")
        print("You need to input more than 2 $")
        n = 0
        while True:
            try:
                n = int(input("How much money do you want to input: "))      
            except ValueError:
                print("Not an integer!\n")
                continue
            else:
                break
    print()

    
    cost = 0
    while True:
        try:
            cost = int(input("Cost per spin: "))      
        except ValueError:
            print("Not an integer!\n")
            continue
        else:
            break

    while (cost >= n) or (cost < 1):
        os.system("clear")
        print("You have ",n,"$")
        if (cost > n):
            print("You cannot play if spinning cost more than what you input")
        if (cost < 1):
            print("The cost of spinning cannot be less than 1 $")
        while True:
            try:
                cost = int(input("Cost per spin: "))      
            except ValueError:
                print("Not an integer!\n")
                continue
            else:
                break

    player = Player(n)
    slot = Slotmachine(cost)
    slot.complete_wheel()
    while player.n >= slot.price:
        print("Number times played = ",slot.turn)
        x = input("Enter anything to play ")
        slot.randomnize()
        animation()
        player.n -= slot.price
        os.system("clear")
        print("You still have ",player.n,"$ left! It costs ",slot.price, "$ to pay! \n ")
        x = input("Enter anything to play ")

        times = 0.01

        for i in range(100):
            os.system("clear")
            slot.spin()
            slot.print_wheel()
            time.sleep(times)
            times += 0.001

        status,what = slot.check_win()

        if status:
            res = slot.winnings(what)
            player.n += res
            print("You now have {}".format(player.n))
        else:
            print("Sorry you lose! You still have {} $\n".format(player.n))
        
        slot.turn += 1

    print("It seems like you don't have enough money to play, too bad, come back when you have more!")
            

        

        
        


            


main_game()

"""
a = Slotmachine()
a.complete_wheel()
a.randomnize()

a.print_wheel()
print(a.a)
print(a.b)
print(a.c)
"""
