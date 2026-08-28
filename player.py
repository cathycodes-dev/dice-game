import dice as d
import score as s


class Player:
    def __init__(self, name="", ai_num=0):
        self.name = name
        self.die = d.dice()
        if self.name == "":
            self.name = "AI "
            self.name += str(ai_num)
        self.categories = [
            "ones",
            "twos",
            "threes",
            "fours",
            "fives",
            "sixes",
            "bonus",
            "Three of a kind",
            "Four of a kind",
            "Full house",
            "Small straight",
            "Large straight",
            "Chance",
            "Yahtzee",
        ]
        self.scores = {x: -1 for x in self.categories}
        self.total = 0
        self.dieScore = s.score(self.die.setOfDie)
        self.topHalfTotal = 0

    def total_score(self):
        self.total = 0
        for x in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
            if self.scores[x] != -1:
                self.total += self.scores[x]
        if self.total > 63:
            if self.scores["bonus"] == -1:
                self.scores["bonus"] = 35
            else:
                self.scores["bonus"] += 35
        for x in [
            "bonus",
            "Three of a kind",
            "Four of a kind",
            "Full house",
            "Small straight",
            "Large straight",
            "Chance",
            "Yahtzee",
        ]:
            if self.scores[x] != -1:
                self.total += self.scores[x]
        return self.total

    def print_score_card(self):
        print("---")
        for x in self.categories:
            if self.scores[x] == -1:
                print("%s:  ---" % (x))
            else:
                print("%s:  %i" % (x, self.scores[x]))
        print(self.total)
        print("---")

    def take_turn(self, turn):
        print(" It is now turn %i for %s." % (turn + 1, self.name))
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
            if self.scores["bonus"] == -1:
                self.scores["bonus"] = 100
            else:
                self.scores["bonus"] += 100
        self.select_score()
        self.print_score_card()
        self.die.roll_nums()

    def select_die(self):
        nums = input(
            "Which dice do you want to re-roll?  (press enter to not re-roll any die)"
        )
        self.die.roll_nums(nums)

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
                    print("#%i -- %s" % (j, x))
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
            for x in self.dieScore.categories:
                if self.dieScore.scores[x] > 0 and self.scores[x] == -1:
                    if category == i:
                        self.scores[x] = self.dieScore.scores[x]
                        scored = True
                        self.total += self.dieScore.scores[x]
                        if category in [
                            "ones",
                            "twos",
                            "threes",
                            "fours",
                            "fives",
                            "sixes",
                        ]:
                            if self.topHalfTotal < 63:
                                self.topHalfTotal += self.dieScore.scores[x]
                                if self.topHalfTotal < 63:
                                    if self.scores["bonus"] == -1:
                                        self.scores["bonus"] = 35
                                    else:
                                        self.scores["bonus"] += 35
                        break
                    i += 1


class AI(Player):
    def select_die(self):
        self.die.roll_nums()
