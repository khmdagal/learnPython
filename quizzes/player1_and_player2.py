import getpass

player1_wins = []
player2_wins = []

while len(player1_wins) < 3 and len(player2_wins) < 3:
    
    player1_move = getpass.getpass('Hey player1 please enter your move  ')
    player2_move = getpass.getpass('Hey big boss player2 please enter your big move  ')

    if player1_move == player2_move:
        print('Hey guys take it easy, You are === TIE ====now')
    elif player1_move == 'rock' and player2_move == 'scissor':
        player1_wins.append(player1_move)
        print('Hey man player1 === WON == this move.. lets see next move')
        print('🥌 wins over ✂')
    elif player1_move == 'paper' and player2_move == 'rock':
        player1_wins.append(player1_move)
        print('Hey man player1 === WON == this move.. lets see next move')
        print('📃 wins over 🥌')
    elif player1_move == 'scissor' and player2_move == 'paper':
        player1_wins.append(player1_move)
        print('Hey man player1 === WON == this move.. lets see next move')
        print('✂ wins over 📃')
    else:
        player2_wins.append(player2_move)
        print('Sorry my princes player1  this guy is not EASY, NOT EASY')
    
    print(f'''

        ''')
    
print('player1',player1_wins)
print('player2',player2_wins)
if len(player2_wins) >= 3:
    print(f'''
            The Game is Over now
                                 🏆
        The winner 🥇🥇🥇 player2 🥇🥇🥇
                ''')
    print('player1',player1_wins)
    print('player2',player2_wins)
if len(player1_wins) >= 3:
    print(f'''
                The Game is Over now
                                🏆
            The winner 🥇🥇🥇 player1 🥇🥇🥇
                ''')
    print('player1',player1_wins)
    print('player2',player2_wins)
