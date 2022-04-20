import random


def unique(n):
    for j in str(n)[1:]:
        if str(n)[0] == j:
            return False

    return True


def validate(s: str):
    if len(s) != 4:
        return False

    a = ['F', 'V', 'D']
    for i in s:
        if i not in a:
            return False

    return True


class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    GOLD = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Game:
    def __init__(self):
        self.left_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.move = []  # [['1', 3]], ['2', 2]]]
        self.true = []  # [['0', 1]]
        self.false = []
        self.last_input = ""
        self.output = ""
        self.choices = []
        self.bot_number = ''.join([str(random.choice(range(0, 10))) for _ in range(4)])
        self.combine()
        self.predict_number = random.choice(self.choices)
        self.dates = range(1900, 2050)
        self.route = [self.predict_number]

    def check_number(self, n):
        for number, index in self.move:
            if n[index] == number:
                return False
            count = 0
            for i in n:
                if i == number:
                    count += 1

            if count == 0:
                return False

        for number, index in self.true:
            if n[index] != number:
                return False

        for number, index in self.false:
            if number in n:
                return False

        return True

    def combine(self):
        self.choices = []
        for i in range(1000, 10000):
            if self.check_number(str(i)):
                self.choices.append(str(i))

    def addMove(self, n, index):
        if [n, index] not in self.move:
            self.move.append([n, index])

    def addTrue(self, n, index):
        if [n, index] not in self.true:
            self.true.append([n, index])

    def addFalse(self, n, index):
        if [n, index] not in self.false:
            self.false.append([n, index])

    def worker(self):
        if len(self.true) == 4:
            return ''.join([i for i, _ in self.true])
        else:
            S = ["*"] * 4
            for i, j in self.true:
                S[j] = i

            return ''.join(S)

    def choose_number(self):
        for i in self.choices:
            if i in self.dates:
                self.predict_number = i
                return 0
        self.predict_number = random.choice(self.choices)
        self.route.append(self.predict_number)

    def check_prediction(self, p: str):
        if len(p) != 4:
            return "Please Check Your Number!"
        answer = ['F'] * 4
        for i in range(len(p)):
            if self.bot_number[i] == p[i]:
                answer[i] = "V"
            elif p[i] in self.bot_number:
                answer[i] = "D"

        return ''.join(answer)

    def next(self, p: str):
        if validate(p):
            for i in range(len(p)):
                if p[i] == "F":
                    self.addFalse(self.predict_number[i], i)
                    try:
                        self.left_numbers.remove(self.predict_number[i])
                    except ValueError as v:
                        pass # 2238
                elif p[i] == "D":
                    self.addMove(self.predict_number[i], i)
                elif p[i] == "V":
                    self.addTrue(self.predict_number[i], i)

            self.combine()
            if len(self.choices) == 0:
                return "Check Your Solving!"
            self.choose_number()

        else:
            return "Check Your Solving! You missed something."
