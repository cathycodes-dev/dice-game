UPPER_SECTION = ["ones", "twos", "threes", "fours", "fives", "sixes"]
LOWER_SECTION = [
    "Three of a kind",
    "Four of a kind",
    "Full house",
    "Small straight",
    "Large straight",
    "Chance",
    "Yahtzee",
]
BONUS = ["upper_bonus", "five_bonus"]

SMALL_STRAIGHT = ({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6})
LARGE_STRAIGHT = ({1, 2, 3, 4, 5}, {2, 3, 4, 5, 6})

PIPS = {
    1: ("     ", "  0  ", "     "),
    2: ("0    ", "     ", "    0"),
    3: ("0    ", "  0  ", "    0"),
    4: ("0   0", "     ", "0   0"),
    5: ("0   0", "  0  ", "0   0"),
    6: ("0   0", "0   0", "0   0"),
}
