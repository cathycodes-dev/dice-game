import player as p
import constants as c


class score:
    def __init__(self, roll):
        self.categories = c.UPPER_SECTION + c.LOWER_SECTION
        self.scores = {x: -1 for x in self.categories}
        self.diceTotal = 0
        for i in roll:
            self.diceTotal += i
        self.pair = False
        self.three = False
        self.straight = 0
        for i in range(1, 7):
            count = roll.count(i)
            if count > 0:
                self.scores[self.categories[i - 1]] = count * i
                self.straight += 1
                if count == 2:
                    self.pair = True
            else:
                self.straight = 0
            if count > 2:
                self.scores["Three of a kind"] = self.diceTotal
                if count > 3:
                    self.scores["Four of a kind"] = self.diceTotal
                    if count == 5:
                        self.scores["Yahtzee"] = 50
                else:
                    self.three = True
            if self.straight > 3:
                self.scores["Small straight"] = 30
                if self.straight == 5:
                    self.scores["Large straight"] = 40
        if self.pair and self.three:
            self.scores["Full house"] = 25
        self.scores["Chance"] = self.diceTotal

    def print_score(self, scoreCard):
        i = 1
        self.zero = []
        for x in self.categories:
            if self.scores[x] > 0 and scoreCard.scores[x] == -1:
                print(f"# {i}-- {x}: {self.scores[x]}")
                i += 1
            else:
                if scoreCard.scores[x] == -1:
                    self.zero.append(x)
        if len(self.zero) > 0:
            print("    or #0-- to view the areas where you can score zero points")
