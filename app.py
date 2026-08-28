import player as p

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
numAI = -1
if not numPlayers > 3:
    while not 0 <= numAI <= (4 - numPlayers):
        try:
            numAI = int(
                input(
                    "How many AI's do you want to play against?  (choose a number 0-%i): "
                    % (4 - numPlayers)
                )
            )
        except ValueError:
            print("Error must type in a number value")
        else:
            if not 0 <= numAI <= (4 - numPlayers):
                print("Please enter a number between 0 and %i" % (4 - numPlayers))
else:
    numAI = 0
players = []
for i in range(1, numPlayers + 1):
    name = input("What is player %i's name? " % i)
    players.append(p.Player(name))
for i in range(1, numAI + 1):
    players.append(p.AI("", i))
for i in range(0, 13):
    for player in players:
        player.take_turn(i)
for player in players:
    print(player.print_score_card())
