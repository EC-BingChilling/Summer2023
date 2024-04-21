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

    #cooperator
    for i in range(int(initial_population*.5)):
        temp = Player()
        temp.Cooperator()
        players.append(temp)

    #defectors
    for i in range(int(initial_population*.25)):
        temp = Player()
        temp.Defector()
        players.append(temp)
    
    #loners
    for i in range(int(initial_population*.25)):
        temp = Player()
        temp.Loner()
        players.append(temp)

    for _ in players:
        print(_.type)

    
