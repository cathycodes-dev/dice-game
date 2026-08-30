import player as p

def play_game():

    numPlayers = -1
    while not 0 <= numPlayers <= 4:
        try:
            numPlayers = int(
                input("How many human players are there?  (choose a number 0-4): ")
            )
        except ValueError:
            print("Error must type in a number value")
        else:
            if not 0 <= numPlayers <= 4:
                print("Please enter a number between 0 and 4")

    numAI = None
    if numPlayers <= 3:
        while numAI is None:
            try:
                numAI = int(
                    input(
                        f"How many AI's do you want to play against?  (choose a number 0-{4 - numPlayers}): "
                    )
                )
            except ValueError:
                print("Error must type in a number value")
            else:
                if numAI > (4 - numPlayers)  or numAI < 0:
                    print(f"Please enter a number between 0 and {4 - numPlayers}")
                    numAI = None
    else: 
        numAI = 0

    players = []
    for i in range(1, numPlayers + 1):
        name = input(f"What is player {i}'s name? ")
        players.append(p.Player(name))
    for i in range(1, numAI + 1):
        players.append(p.AI(i))

    for player in players:
        print(f"{player.name} is ready to play.")

    for i in range(0, 13):
        for player in players:
            player.take_turn(i)
    for player in players:
        print(player.print_score_card())

if __name__ == "__main__":
    play_game()