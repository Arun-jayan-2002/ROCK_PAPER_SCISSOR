import random

print('\n\b ROCK_PAPER_SCISSOR')
print('\n\t\b 1.Start \n\t\b 2.Exit')
option=int(input('\n\t\bEnter your choice (1 or 2) :- '))
a=['paper','scissor','rock']
while option==1:
    def p1():
        usr=None
        # flag=True
        while usr not in a:
            usr=input('\n\tchoose (rock , paper or scissor) :- ') 
        return usr
    def p2():
        r2=random.choice(a)
        print(f'\n\tthe Player 2 is choose {r2}')
        return r2
    # print(p1())
    # print(p2())
    a1=p1()
    a2=p2()

    

    if a1=='paper'and a2=='rock':
        print('\n\t\bplayer 1 is winner')

    elif a1=='scissor' and a2=='paper':
        print('\n\t\bplayer 1 is winner ')

    elif a1=='rock' and a2=='scissor':
        print('\n\t\bplayer 1 is winner ')

    elif a1=='rock'and a2=='paper':
        print('\n\t\bplayer 2 is winner')

    elif a1=='paper' and a2=='scissor':
        print('\n\t\bplayer 2 is winner ')

    elif a1=='scissor' and a2=='rock':
        print('\n\t\bplayer 2 is winner ')

    elif a1=='rock' and a2=='rock':
        print('\n\t\bEqual')

    elif a1=='paper' and a2=='paper':
        print('\n\t\bEqual')

    elif a1=='scissor' and a2=='scissor':
        print('\n\t\bEqual')

    print('\n\t\b 1.Start \n\t\b 2.Exit')
    option=int(input('\n\t\bEnter your choice (1 or 2) :- '))
if option==2:
    exit()