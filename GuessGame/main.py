import random as rand

i = 0
n = 20
rand_num = int(n * rand.random()) + 1

guess = 0
while guess != rand_num:
    guess = int(input("Enter a number: "))
    if 0 < guess <= n:
        if guess < rand_num:
            print(str(guess) + " is smaller than " + str(rand_num))
        elif guess > rand_num:
            print(str(guess) + " is greater than " + str(rand_num))
        else:
            print("Congratulations, you won the game")
            break
    else:
        print("Sorry!...You quit the game")
        break


