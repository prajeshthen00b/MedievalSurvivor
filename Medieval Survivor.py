#Pick your player!
print('*'*50)
print('Welcome to Medieval Survivor!')
print('*'*50)
import pandas as pd
import numpy as np
pq=vq=3
turns = 5 #a game of 5 rounds
def intro():
    print('1. You shall be allocated a random hero.\n2. Based on a random toss, either you or your opponent shall get to strike first.\n3. You can either chose to:\n\t1. ATTACK\n\t2. SPECIAL ATTACK\n\t3. DEFEND\nAll you need to do to perform an action is to press the digits 1,2 or 3!\nThe character whose health drops below 0 or touches it FIRST, loses the match.\nIf both heroes have a health bar that is above 0 after 5 rounds, you shall go down in history as warriors of equal might!\nThat is it. Thanks for choosing Medieval Survivor, have fun!')
def game():
    player=np.random.randint(0,5)
    cpu=np.random.randint(5,10)
    game=pd.read_excel('MS.xlsx')
    print("The player you have been allocated is...",game.iloc[player,0],"!")
    print(game.iloc[player,0],"is of type:",game.iloc[player,2],"\nRace:",game.iloc[player,1])
    print ('*'*50)
    print("The player you will be facing is...",game.iloc[cpu,0],"!")
    print(game.iloc[cpu,0],"is of type:",game.iloc[cpu,2],"\nRace:",game.iloc[cpu,1])
    Hero=game.iloc[player,0] #names defined
    Villain=game.iloc[cpu,0] 
    print("So it's",Hero,"against",Villain,"!")
    def one_or_two():  #Randomizes attack between ordinary and special!
        y=np.random.randint(1,3)
        return y
    #gotta define all metrics like attack, defense and spl atk for each player
    phit=game.loc[player,'Damage']
    vhit=game.loc[cpu,'Damage']
    pshit=game.loc[player,'Spl Atk']
    vshit=game.loc[cpu,'Spl Atk']
     #special attack limit!
    def pfight():   #function that defines player movement
        global pq,vq
        print('Do you want to\n1. Attack\n2. Special Attack\n3. Defend\nYou have',pq,'special attacks left')
        x=input()
        if x=='1':
            game.loc[cpu, 'HP']-=phit
            print("You have hit",Villain,"with damage worth", phit,"!")
            print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
        elif x=='2':
            if  pq>0:
                game.loc[cpu, 'HP']-=pshit
                print("You have hit",Villain,"with damage worth", pshit,"!")
                print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
                pq-=1
            else:
                print("You have run out of special attacks, proceding with ordinary attack.")
                game.loc[cpu, 'HP']-=phit
                print("You have hit",Villain,"with damage worth", pshit,"!")
                print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
        elif x=='3':
            print('You have chosen to defend!')
            one_or_two=np.random.randint(1,3)
            if one_or_two==1:
                print(Villain, "has inflicted an ORDINARY ATTACK!")
                game.loc[player, 'HP']-=(vhit//2)
                print('Your health is now at',game.loc[player, 'HP'])
            elif one_or_two==2:
                print(Villain,"has chosen to inflict a SPECIAL ATTACK!")
                game.loc[player, 'HP']-=(vshit//2)
                print('Your health is now at',game.loc[player, 'HP'])
    def vfight():   #function that define's player movement
        x=np.random.randint(1,4)
        global pq,vq
        if x==1:
            game.loc[player, 'HP']-=vhit
            print(Villain,"has inflicted an ORDINARY ATTACK!")
            print('Your health is now at',game.loc[player, 'HP'])
        elif x==2:
            if vq>0:
                game.loc[player, 'HP']-=vshit
                print(Villain,"has inflicted a SPECIAL ATTACK!")
                print('Your health is now at',game.loc[player, 'HP'])
                vq-=1
            else:
                game.loc[player, 'HP']-=vhit
                print(Villain,"has inflicted an ORDINARY ATTACK!")
                print('Your health is now at',game.loc[player, 'HP'])
        elif x==3:
            print(Villain,'has chosen to defend!')
            print('Do you want to\n1. Attack\n2. Special Attack? You have',pq,'special attacks left')
            choice=input()       
            if choice=='1':
                print("You have chosen to ATTACK!")
                game.loc[cpu, 'HP']-=(phit//2)
                print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
            elif choice=='2':
                if pq>0:
                    print("You have chosen to inflict a SPECIAL ATTACK!")
                    game.loc[cpu, 'HP']-=(pshit//2)
                    print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
                    pq-=1
                else:
                    print("You have run out of SPECIAL ATTACKS, resorting to an ordinary attack instead.")
                    game.loc[cpu,'HP']-=phit
                    print("You have hit",Villain,"with damage worth", phit,"!")
                    print(Villain,"'s health is now at",game.loc[cpu, 'HP'])
    def check():  #checks for health
       
        if game.loc[player,'HP']<=0:
            print('Alas',Villain,'has proven to be too good of a match for you...')
            print('You look upon the silver moon one last time as you feel yourself slipping away into the abyss.')
            return 0
        elif game.loc[cpu,'HP']<=0:
            print(Villain,'bows down in defeat, inches away from lady death as you spill out their guts all over the floor.')
            print('Congratulations, you win.')
            return 0
    def core():
        global turns
        toss=np.random.randint(0,2)
        if toss==0:
            print('You go first this time.')
            while turns>0:
                print('*'*50)
                print('R O U N D \t ',6-turns)
                print('*'*50)
                pfight()
                check()
                if check()==False:
                    break
                vfight()
                if check()==False:
                    break
                if turns==1:
                    if game.loc[player,'HP']>0 and game.loc[player,'HP']>0:
                        print('EQUALLED')
                        break
                turns-=1
        elif toss==1:
            print(Villain,'goes first this time!')
            while turns>0:
                print('*'*50)
                print('R O U N D \t ',6-turns)
                print('*'*50)
                vfight()
                check()
                if check()==False:
                    break
                pfight()
                if check()==False:
                    break
                if turns==1:
                    if game.loc[player,'HP']>0 and game.loc[player,'HP']>0:
                        print('After 5 rounds of a duel of gargantuan proportion, you both smirk at each other in agreement.\nYes, you have both survived!\nLife is full of dichotomies; today, however, you have found your equal.\nYou both concede mutual victories, hop on to your horses, and ride into the setting sun.\nNot as gladiators...\n...but as equals.')
                    break
                turns-=1
    core()
print("Press 1 to Start Game\nPress 2 to Read Instructions first!")
x=input()
valid=['1','2']
while True:    
    if x not in valid:
        print('INCORRECT INPUT, PAY ATTENTION, ENTER YOUR CHOICE AGAIN!')
        x=input()
    else:
        break
if x=='1':
    game()
elif x=='2':
    intro()
    game()

    


    


    
    
    

    
