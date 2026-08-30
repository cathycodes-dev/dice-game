import random as r
import constants as c
from collections import Counter, OrderedDict


class Dice:
    def __init__(self):
        self.die_set = []
        for _ in range(1, 6):
            self.die_set.append(r.randint(1, 6))
        self.die_set.sort()

        self.score_outdated = True
        self.scores = OrderedDict()
        self.zeros = []

    def print_set(self):
        print("---")
        print("DICE ROLL: ")
        for line_num in range(1, 7):
            line = ""
            for y, die_value in enumerate(self.die_set, start=1):
                if line_num == 6:
                    line += f" *Dice #{y}: {die_value}* "
                elif line_num in [1, 5]:
                    line += "  +-------+   "
                else:
                    line += f"  | {c.PIPS[die_value][line_num-2]} |   "
            print(line)
        print("---")

    def roll_dice(self, numSet="12345"):
        for x in range(0, 5):
            if str(x + 1) in numSet:
                self.die_set.pop(x)
                self.die_set.insert(x, r.randint(1, 6))

        self.score_outdated = True
        self.die_set.sort()

    def calculate_score(self):
        self.scores = OrderedDict()

        diceTotal = sum(self.die_set)
        counts = Counter(self.die_set)
        freqs = sorted(counts.values(), reverse=True)
        unique_dice = set(self.die_set)

        # Upper Section (Ones through Sixes)
        for x, category in enumerate(c.UPPER_SECTION, 1):
            if counts.get(x, 0) > 0:
                self.scores[category] = counts[x] * x

        # Three of a kind / Four of a kind / Yahtzee
        if freqs[0] >= 3:
            self.scores["Three of a kind"] = diceTotal
        if freqs[0] >= 4:
            self.scores["Four of a kind"] = diceTotal
        if freqs[0] == 5:
            self.scores["Yahtzee"] = 50

        # Full House (Either a 3-of-a-kind + pair, OR 5-of-a-kind)
        if (len(freqs) >= 2 and freqs[0] == 3 and freqs[1] == 2) or freqs[0] == 5:
            self.scores["Full house"] = 25

        if any(s.issubset(unique_dice) for s in c.SMALL_STRAIGHT):
            self.scores["Small straight"] = 30
        if unique_dice in c.LARGE_STRAIGHT:
            self.scores["Large straight"] = 40

        # Chance
        self.scores["Chance"] = diceTotal

        for category in c.UPPER_SECTION + c.LOWER_SECTION:
            score = self.scores.get(category, None)
            if score is None:
                self.zeros.append(category)

        self.score_outdated = False

    def print_score(self, current_scores):
        i = 1
        for categories in self.scores.keys():
            # current score is empty
            if current_scores.get(categories, None) is None:
                if self.scores[categories]:
                    print(f"#{i} -- {categories}: {self.scores[categories]}")
                    i += 1

        if i == 1:
            print("No available scores. Press 0 to view zero-score options.")
        if len(self.zeros) > 0:
            print("    or #0 -- to view the areas where you can score zero points")

    def print_zeros(self):
        for x, category in enumerate(self.zeros, 1):
            print(f"#{x} -- {category}: 0")
            self.die_set.pop(x)
            self.die_set.insert(x, r.randint(1, 6))
        # Manual roll of dice for code
        # self.setOfDie = [4, 4, 4, 4, 4]  # Example manual roll

        self.score_outdated = True
        self.die_set.sort()
