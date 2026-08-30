import dice as d
import score as s
import constants as c

class Player:
    def __init__(self, name):
        self.name = name
        self.die = d.Dice()
        self.scores = {x: None for x in c.UPPER_SECTION + c.BONUS + c.LOWER_SECTION}
        self.total = 0
        self.dieScore = s.score(self.die.setOfDie)

    def total_score(self):
        self.total = 0
        for x in c.UPPER_SECTION:
            self.total += self.scores.get(x, 0)
        if self.total > 63:
            self.scores["upper_bonus"] = 35

        for x in c.BONUS + c.LOWER_SECTION:
            self.total += self.scores.get(x, 0)
        return self.total

    def print_score_card(self):
        print("---")
        for x in self.scores.keys():
            if self.scores[x] is None:
                print(f"{x}:  ---")
            else:
                print(f"{x}:  {self.scores[x]}")
        print(self.total)
        print("---")

    def take_turn(self, turn):
        print(f" It is now turn {turn + 1} for {self.name}.")
        self.die.print_set()
        self.select_die()
        self.die.print_set()
        self.select_die()
        self.die.print_set()
        self.dieScore = s.score(self.die.setOfDie)

        # check if bonus Yahtzee
        if (
            self.die.setOfDie.count(self.die.setOfDie[1]) == 5
            and self.scores["Yahtzee"] == 50
        ):
            if self.scores["five_bonus"] == None:
                self.scores["five_bonus"] = 100
            else:
                self.scores["five_bonus"] += 100

        self.select_score()
        self.print_score_card()
        self.die.roll_dice()

    def select_die(self):
        nums = input(
            "Which dice do you want to re-roll?  (press enter to not re-roll any die)"
        )
        self.die.roll_dice(nums)

    def select_score(self):
        scored = False
        while not scored:
            print("You can score ---")
            self.dieScore.print_score(self)
            try:
                category = int(input("Which do you want to score?"))
            except ValueError as e:
                print("Error must type in a number value")
                category = None

            if category == 0:
                j = 1
                for x in self.dieScore.zero:
                    print(f"# {j} -- {x}")
                    j += 1
                try:
                    int_for_zero = int(
                        input(
                            "Which do you want to score? (0 to return to other scoring options)"
                        )
                    )
                except ValueError as e:
                    print("Error must type in a number value")
                    int_for_zero = None
                j = 1
                for x in self.dieScore.zero:
                    if int_for_zero == j:
                        self.scores[x] = 0
                        scored = True
                        break
                    j += 1
            i = 1
            if category is not None and category > 0:
                for x in self.dieScore.categories:
                    if self.dieScore.scores.get(x, 0) > 0:
                        if category == i:
                            self.scores[x] = self.dieScore.scores[x]
                            scored = True
                            break
                        i += 1


class AI(Player):
    def __init__(self, ai_num):
        super().__init__(f"AI {ai_num}")

    def select_die(self):
        self.die.roll_dice()
