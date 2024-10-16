import random 



choice = ['rock', 'paper', 'scissor']


result = True


while result != False:
    element = random.randint(0,len(choice) - 1)
    computer_player = choice[element]
    Enter_your_choice = input('Enter your choice ')
    your_move = Enter_your_choice.lower()
    if your_move == computer_player:
        print(f""" Your are TIE
            {your_move} same choice {computer_player} 
            """)
        print(result)
    elif your_move == 'paper' and computer_player == 'rock':
        print(f"""You WON 🎉
            {your_move} WINS over {computer_player} 
            """)
        print(result)
    elif your_move == 'rock' and computer_player == 'scissor':
        print(f"""You WON 🎉
            {your_move} WINS over {computer_player}
            """)
        print(result)
    elif your_move == 'scissor' and computer_player =='paper':
        print(f"""You WON 🎉
            {your_move} WINS over {computer_player}
            """)
        print(result)
    else:
        print(f"""      
              GAME IS OVER 
              
              OOOOOOh man You LOSS 🎇 Boom

            {computer_player} WINS over {your_move}  

            """)
        result = False
        print(result)
        
  