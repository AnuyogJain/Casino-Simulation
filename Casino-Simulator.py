import random

def Dicebet(money):
    print("Rules: Roll bigger number to win.")
    bet=int(input("Enter bet value "))
    if money<bet:
        print("\nNot enough money.\n")
        return 0
    d1= (random.randint(2, 12))
    d2= (random.randint(2, 12))
    print ("\nYou rolled 2 dices that land on total of",d1,"on bet of",bet,"$.")
    print ("Computer rolled 2 dices that land on total of",d2,"on bet of",bet,"$.")
    if d1==d2:
        print("\nNobody won.")
        return 0
    elif d1>d2:
        print("\nYou won.")
        return bet
    else:
        print("\nYou lost.")
        return -bet

def Scratch(card):
    if card<1:
        print("\nNot enough Scratch cards.\n")
        return 0
    num= (random.randint(1,10))
    if num==1:
        print("\nYou scratched a card and won a Jackpot of 10000","$.\n")
        return 10000
    elif num==2:
        print("\nYou scratched a card and won 4000","$.\n")
        return 4000
    elif num==3:
        print("\nYou scratched a card and won 2500","$.\n")
        return 2500
    elif num==4:
        print("\nYou scratched a card and won 500","$.\n")
        return 500
    elif num==5:
        print("\nYou scratched a card and won 1500","$.\n")
        return 1500
    else:
        print("\nYou scratched a card but won nothing. \n")
        return 0

def BuyScratch(money):
    print("Rules: Random prizes.")
    if money<2000:
        print("\nNot enough money.\n")
        return 0
    print("\nYou bought a Scratch Card of 2000","$.\n")
    return 1
    
def slots():
    print("Rules: Random prizes.")
    print("\nYou did slots for 1000 $.")
    num= (random.randint(1,5))
    num2= (random.randint(1,5))
    num3= (random.randint(1,5))
    if num==num2==num3:
        print("\n7 7 7\nYou won Jackpot of 5000","$.\n")
        return 5000
    elif num==num2 or num==num3 or num2==num3:
        print("\nYou won 2000 $.\n")
        return 2000
    else:
        print("\nBetter luck next time.\n")
        return 0

def roulette(money):
    print("Rules: Bet on one a right option to win.")
    win=0
    color= (random.randint(3, 4))
    num= (random.randint(1, 36))
    print("What you want to bet on:\n 1.Odd\n 2.Even\n 3.Red\n 4.Black\n 5.1-12\n 6.13-24 \n 7.25-36\n 8.Bet")
    while True:
        choice = int(input("Enter a choice "))
        if choice==1 or choice==2:
                bet=int(input("Enter bet value "))
                if bet<=money:
                    win-=bet
                    if choice==1 and (num%2)!=0:
                        win+=(bet*2)
                    elif choice==2 and (num%2)==0:
                        win+=(2*bet)
                else:
                    print("Not enough money.")
        elif choice==3 or choice==4:
            bet=int(input("Enter bet value "))
            if bet<=money:
                win-=bet
                if color==choice:
                    win+=(2*bet)
            else:
                    print("Not enough money.")        
        elif choice==5 or choice==6 or choice==7:
            bet=int(input("Enter bet value "))
            if bet<=money:
                win-=bet
                if choice==5 and num>=0 and num<=12:
                    win+=(2*bet)
                elif choice==6 and num>=13 and num<=24:
                    win+=(2*bet)
                elif choice==7 and num>=25 and num<=36:
                    win+=(2*bet)
            else:
                    print("Not enough money.")        
        elif choice==8:
            break
        else:
            print("Invalid choice.")
    print("\nNumber was",num,".")
    if color==3:
        print("Colour was red.")
    elif color==4:
        print("Colour was black.")
    if num%2!=0:
        print("Number was odd.\n")
    elif num%2==0:
        print("Number was even.\n")
    if win>=0:
        print("You won",win,"$")
    else:
        print("You lost",(win*-1),"$")
    return win    
        
def wof():
    print("Rules: Random prizes.")
    print("\nYou rotated Wheel of Fortune for 1000 $.")
    num= (random.randint(1,10))
    if num==1:
        print("\nYou won Jackpot of 3000","$.\n")
        return 3000
    elif num==3:
        print("\nYou won 1500","$.\n")
        return 1500
    elif num==4:
        print("\nYou won 1000","$.\n")
        return 1000
    elif num==5:
        print("\nYou won 500","$.\n")
        return 500
    elif num==6:
        print("\nYou won 100","$.\n")
        return 100
    elif num==7:
        print("\nYou won 100","$.\n")
        return 100   
    elif num==8:
        print("\nYou won a Scratch card.","\n")
        return 1      
    else:
        print("\nGot nothing.\n")
        return 0
       
def blackjack(money):
    print("Rules: Draw cards totalling upto sum of 21.")
    print("       Picture cards counts as 10. Ace is 1.")
    print("       If sum of cards gets more than 21 then card holder will lose.")
    print("       Computer will draw another card on sum of 16 or less.")
    print("       Whomever gets more sum will win.")
    bet=int(input("Enter bet value "))
    if money<bet:
        print("\nNot enough money.\n")
        return 0
    win=0
    t1= (random.randint(1, 13))
    t2= (random.randint(1, 13))
    t3= (random.randint(1, 13))
    t4= (random.randint(1, 13))
    pic='J','Q','K'
    #print(t1,t2,t3,t4)
    print("Computer cards = ",end ="")
    if t1>10:
        char= (random.randint(0, 2))
        print(pic[char],end ="")
        t1=10
    elif t1==1:
        print("A ",end="")
    else:
        print(t1,end ="")
    if t2>10:
        t2=10
    print(" *")    
    print("Your cards = ",end ="")
    if t3>10:
        char= (random.randint(0, 2))
        print(pic[char]," ",end="")
        t3=10
    elif t3==1:
        print("A ",end="")    
    else:
        print(t3," ",end="")
    if t4>10:
        char= (random.randint(0, 2))
        print(pic[char])
        t4=10
    elif t4==1:
        print("A ")    
    else:
        print(t4)    
    #print(t1,t2,t3,t4)
    sum1=t1+t2
    sum2=t3+t4
    #print(sum1,sum2)
    print("\n1.Hit\n2.Stand\n")
    temp=1
    while True:
        if temp==0:
            choice=2
        else:    
            choice = int(input("Enter a choice: "))
        if choice==1:
            temp= (random.randint(1, 10))
            print("You drew",temp,".")
            sum2+=temp
            if sum2>21:
                print("Sum of computer's cards = ",sum1,".") 
                print("Sum of Your cards = ",sum2,".")
                print("You lost.")
                win=(bet*(-1))
                return win
        elif choice==2:
            if sum1<=16:
                temp= (random.randint(1, 10))
                print("Computer drew",temp,".")
                sum1+=temp
            if sum1>21:
                print("Sum of computer's cards = ",sum1,".") 
                print("Sum of Your cards = ",sum2,".") 
                print("You won.")
                win=bet
                return win
            if sum1<=16:
                temp=0
                continue
            print("Sum of computer's cards = ",sum1,".") 
            print("Sum of Your cards = ",sum2,".")  
            if sum1==sum2:
                print("Match drew.")
                win=0
                return win
            elif sum2>sum1:
                print("You won.")
                win=bet
                return win
            else:
                print("You lost.")
                win=(bet*(-1))
                return win
        else:
            print("Enter valid choice")
    return win        
money=10000
card = 0
count=0
bet=0
scratchc=0
slot=0
roulete=0
whof=0
bj=0
print("\t\tWELCOME TO CASINO\nHere you can try your luck with various games.")
print("You will start with 10000$ and can play any of the game.")
print("\nYou can choose any of the following: ")
print("1. Betting\n2. Buy a Scratch card ($2000)\n3. Use a Scratch card\n4. Slots ($1000)\n5. Roulette\n6. Wheel of fortune ($1000)\n7. BlackJack\n8. Work\n9. Profile\n10. Exit")
print("\nYou have",money,"$.")
while True:
    choice = int(input("Enter a choice (Enter 0 for menu): "))
    if choice==1:
        money= money + Dicebet(money)
        print("Money =",money,"$.\n")
        bet+=1
    elif choice==3:
        money= money + Scratch(card)
        print("Money =",money,"$.")
        if card>0:
            card-=1
            scratchc+=1
        print("You have",card,"Scratch cards left.\n")
    elif choice==2:
        if BuyScratch(money)==1:
            card+=1
            money-=2000
        print("You have",card,"Scratch cards.\n")
        print("Money =",money,"$.")
    elif choice ==4:
        if money>=1000:
            money-=1000
            slot+=1
            money+=slots()
            print("Money =",money,"$.")
        else :
            print("\nNot enough money.\n")
            print("Money =",money,"$.")
    elif choice == 5:
        money+=roulette(money)
        roulete+=1
        print("Money =",money,"$.")
    elif choice ==6:
        if money>=1000:
            whof+=1
            money-=1000
            win=wof()
            if win==1:
                card+=1
            else:
                money+=win
            print("Money =",money,"$.")
        else :
            print("\nNot enough money.\n")
            print("Money =",money,"$.")
    elif choice ==8:
        if count<5:
            num= (random.randint(int(-money/2),int(money/2)))
            if num>=0:
                print("\nYou worked hard and earned",num,"$.")
            else:
                print("\nYou slacked off at work and lost",num,"$.")
            money+=num    
            print("Money =",money,"$.")
            count+=1
            print("You can work",5-count,"more times.\n")
        else:
            print("\nYou are too tired to work.\n")
    elif choice==7:
        money+=(blackjack(money))
        print("Money =",money,"$.")
        bj+=1
    elif choice==9:
        print("\nYou have",money,"$.")
        print("You have",card,"Scratch cards.")
        print("You can work",5-count,"more times.")
        print("Bet:",bet)
        print("Strached cards:",scratchc)
        print("Slot Machine:",slot)
        print("Roulette:",roulete)
        print("BlackJack:",bj)
        print("Wheel of fortune:",whof,"\n")
    elif choice==10:
        break
    elif choice ==0:
        print("\n1. Betting\n2. Buy a Scratch card ($2000)\n3. Use a Scratch card\n4. Slots ($1000)\n5. Roulette\n6. Wheel of fortune ($1000)\n7. BlackJack\n8. Work\n9. Profile\n10. Exit\n")
    else:
        print("\nPlease enter a valid choice.\n")