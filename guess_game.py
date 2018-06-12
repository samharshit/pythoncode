from random import randrange
while True :
    com = randrange(1,50)
    c = 1
    while c <= 5 :
        user = int(input("Your Guess : "))
        if user > com :
            print("Be in limits Think Lower")
        elif user < com :
            print("Be Big Think Big")
        else :
            print("Computer Guess : ",com)
            print("Yeah you have won the Game : ")
            break
        if c == 5 :
            print("Computer Guess : ",com)
            print("You Such a Looser ")
        c = c + 1

    ch = input("Press yes to continue : ").strip().lower()
    if ch == 'y' or ch == 'yes' :
        continue
    else :
        break
