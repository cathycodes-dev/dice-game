import random as r
import constants as c
class Dice:
    def __init__(self):
        self.setOfDie = []
        for _ in range(1, 6):
            self.setOfDie.append(r.randint(1, 6))
        self.setOfDie.sort()

    def print_set(self):
        print("---")
        print("DICE ROLL: ")
        for line_num in range(1, 7):
            line = ""
            for y, die_value in enumerate(self.setOfDie, start=1):
                if line_num == 6:
                    line += f" *Dice #{y}: {die_value}* "
                elif line_num in [1, 5]:
                    line += "  +-------+   "
                else:
                    line+= f"  | {c.PIPS[die_value][line_num-2]} |   "
            print(line)
        print("---")

    def roll_dice(self, numSet="12345"):
        for x in range(0, 5):
            if str(x + 1) in numSet:
                self.setOfDie.pop(x)
                self.setOfDie.insert(x, r.randint(1, 6))
        self.setOfDie.sort()
