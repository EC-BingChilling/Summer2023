class Player:
    def __init__(self):
        pass

    def Cooperator(self):
        self.type = 1
        self.payoff = 0

    def Defector(self):
        self.type = 2
        self.payoff = 0

    def Loner(self):
        self.type = 3
        self.payoff = 0


if __name__ == "__main__":

    #determine how many in study
    initial_population = 1000
    players = []

    for i in range(int(initial_population*.5)):
        temp = Player()
        players.append(temp.Cooperator())
