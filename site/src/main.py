import player as p
import asyncio

from async_helper import input_async


async def play_game():
    print("Welcome to the Dice Game!")

    numPlayers = -1
    while not 0 <= numPlayers <= 4:
        try:
            val = await input_async("How many human players are there?  (choose a number 0-4): ")
            numPlayers = int(val)
        except ValueError:
            print("Error must type in a number value")
        else:
            if not 0 <= numPlayers <= 4:
                print("Please enter a number between 0 and 4")

    numAI = None
    maxAI = 4 - numPlayers
    if maxAI > 0:
        while numAI is None:
            try:
                val = await input_async(f"How many AI's do you want to play against?  (choose a number 0-{maxAI}): ")
                numAI = int(val)
            except ValueError:
                print("Error must type in a number value")
            else:
                if numAI > maxAI or numAI < 0:
                    print(f"Please enter a number between 0 and {maxAI}")
                    numAI = None
    else: 
        numAI = 0

    players = []
    for i in range(1, numPlayers + 1):
        name = await input_async(f"What is player {i}'s name? ")
        players.append(p.Player(name))
    for i in range(1, numAI + 1):
        players.append(p.AI(i))

    for player in players:
        print(f"{player.name} is ready to play.")
        await asyncio.sleep(0.1)

    for i in range(0, 13):
        for player in players:
            await player.take_turn(i)
    print("Game over!")

    for player in players:
        print(f"Final score for {player.name}:")
        print(player.print_score_card())

if __name__ == "__main__":
    asyncio.run(play_game())