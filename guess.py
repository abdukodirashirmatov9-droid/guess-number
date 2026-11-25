import random
n = random.randit(0,10)
guess = int(input("guess a number between 0 and 10" )
            guesses = 0
            while True: 
            if n == guess:
            print("Нашли число ")
            break 
             guesses+=1
            if guesses >= 3:
            print("Проиграли")
            break
         
