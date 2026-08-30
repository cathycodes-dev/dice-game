import dice as d
import constants as c


class Player:
    def __init__(self, name):
        self.name = name
        self.die = d.Dice()
        self.scores = {}
        self.total = 0

    def total_score(self):
        self.total = 0

        for x in c.UPPER_SECTION:
            self.total += self.scores.get(x, 0)

        if self.total > 63 and not self.scores["upper_bonus"]:
            self.scores["upper_bonus"] = 35

        for x in c.BONUS + c.LOWER_SECTION:
            self.total += self.scores.get(x, 0)
        return self.total

    def print_score_card(self):
        print("---")
        for x in c.UPPER_SECTION + c.LOWER_SECTION:
            if self.scores.get(x, None) is None:
                print(f"{x}:  ---")
            else:
                print(f"{x}:  {self.scores[x]}")
        print(self.total)
        print("---")

    def take_turn(self, turn):
        print(f" It is now turn {turn + 1} for {self.name}.")

        print(f"Roll 1 for {self.name}")
        self.die.print_set()
        self.reroll_die()

        print(f"Roll 2 for {self.name}")
        self.die.print_set()
        self.reroll_die()

        print(f"Roll 3 for {self.name}")
        self.die.print_set()
        self.die.calculate_score()

        self.select_score()
        self.print_score_card()
        self.die.roll_dice()

    def reroll_die(self):
        nums = input(
            "Which dice do you want to re-roll?  (press enter to not re-roll any die)"
        )
        self.die.roll_dice(nums)

    def select_score(self):
        scored = False
        while not scored:
            print("You can score ---")
            self.die.print_score(self.scores)

            try:
                num_category = int(input("Which do you want to score?"))
            except ValueError as _:
                print("Error must type in a number value")
                num_category = None

            if num_category == 0:
                j = 1
                for x in self.die.zeros:
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
                    int_for_zero = 0
                if int_for_zero != 0:
                    category = self.die.zeros[int_for_zero - 1]
                    self.scores[category] = 0
                    scored = True
            else:
                i = 1
                for x in self.die.scores.keys():
                    if self.scores.get(x, None) is None:
                        if num_category == i:
                            self.scores[x] = self.die.scores[x]
                            self.total += self.die.scores[x]
                            scored = True
                            break
                        i += 1


class AI(Player):
    def __init__(self, ai_num):
        super().__init__(f"AI {ai_num}")

    def reroll_die(self):
        self.die.roll_dice()

    def select_score(self):
        self.die.calculate_score()
        max_score = 0
        max_category = None
        for category, score in self.die.scores.items():
            if self.scores.get(category, None) is None:
                print(f"{self.name} considers scoring {score} in {category}")
                if category == "Chance":
                    if max_score != 0:
                        continue
                if score >= max_score:
                    max_score = score
                    max_category = category
            
        if max_category is not None:
            print(f"AI {self.name} scores {max_score} in {max_category}")
            self.scores[max_category] = max_score
            self.total += max_score
        else:
            print("No available scores for AI.")
            for category in self.die.zeros:
                if self.scores.get(category, None) is None:
                    print(f"{self.name} scores 0 in {category}")
                    self.scores[category] = 0
            