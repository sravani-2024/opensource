def determine_winner(player1, player2):
    
    if player1 == player2:
        return "NULL"
    if(player1 == 'S' and player2 == 'P'):
        return "vignesh"
    return "Charan"
vignesh, charan = input().split()
winner = determine_winner(vignesh, charan)
print(winner)
