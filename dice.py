import random as r

PIPS = {
        1: ("     ", "  0  ", "     "),
        2: ("0    ", "     ", "    0"),
        3: ("0    ", "  0  ", "    0"),
        4: ("0   0", "     ", "0   0"),
        5: ("0   0", "  0  ", "0   0"),
        6: ("0   0", "0   0", "0   0"),
    }
class dice:
    def __init__(self):
        self.setOfDie = []
        for _ in range(1, 6):
            self.setOfDie.append(r.randint(1, 6))
        self.setOfDie.sort()

    def print_set(self):
        print("---")
        print("DICE ROLL: ")
        for x in range(1, 7):
            row = ""
            for y, die_value in enumerate(self.setOfDie, start=1):
                pips = ""
                if x == 6:
                    row += f" *Dice #{y}: {die_value}* "
                else: 
                    if x in [1, 5]:
                        row += "  +-------+   "
                    else:
                        row+= f"  | {PIPS[die_value][x-2]} |   "
            print(row)
        print("---")

    def roll_nums(self, numSet="12345"):
        for x in range(0, 5):
            if str(x + 1) in numSet:
                self.setOfDie.pop(x)
                self.setOfDie.insert(x, r.randint(1, 6))
        self.setOfDie.sort()
