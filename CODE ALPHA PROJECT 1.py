#HANGMAN GAME:
print("WELCOME TO HANGMAN GAME......:)")
i=7
print("PRESS 7 TO START THE GAME")
i = int(input("Enter your choice: "))
if i==7:
    print("THE GAME HAS STARTED")


import random
words = ['haider','python','java','apple','orange','chair']
computer_choice = random.choice(words)
guesses = ["_"]*len(computer_choice)
incorrect_guesses = 0
max_incorrect_guesses = 6
while True:
     print(' '.join(guesses))
     guess = input("Enter your guess letter: ").lower()
     if guess in computer_choice:
         for i in range(len(computer_choice)):
             if computer_choice[i] == guess:
                 guesses[i] = guess
     else:
         incorrect_guesses = incorrect_guesses+1
         print(f"incorrect!({incorrect_guesses}/{max_incorrect_guesses})")
     if '_' not in guesses:
         print("CONGRAGULATIONS! YOU WON\n THE WORD IS",computer_choice)
         break # break statement inside the while loop
     elif incorrect_guesses==max_incorrect_guesses:
         print(f"Sorry you lost! The word was {computer_choice}")
         break # break statement inside the while loop
print("THANK YOU FOR ATTEMPTED.......\n ......:)")



















