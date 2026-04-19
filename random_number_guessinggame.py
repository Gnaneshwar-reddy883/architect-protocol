import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
#print(answer)
guesses = 0
is_running = True
print("Welcome to python number guessing game")
print(f"choose a number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print("the number is out of range")
            print(f"choose a number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("too low,try again!")
        elif guess>answer:
            print("too high,try again")
        else:
            print(f"CORRECT! the answer was {answer}")
            print(f"the number of guesses was {guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"choose a number between {lowest_num} and {highest_num}")