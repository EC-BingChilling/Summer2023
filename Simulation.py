import random
#import testing

R = 1.8 #rate
C = 1 #contribution for cooperators
SIGMA = 0.3 #payoff for loners
KAPPA = 0.1


class Player:
    #1 is for coop, 2 for def, 3 for loner, use numbers to easily compare type and change in future 

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


def sim(rounds, players, n):
    """runs a simulation of the game and updates payoffs for each players

    Args:
        rounds (int): number of times to run simulation
        players (array): list of contributer, loners, defectors aka players in game
        n (int): total num of players in game 
    """
    total_payoff = 0
    for i in range(rounds):
        for _ in players:
            if _.type == 1:     #if contributer they contriubte 1
                total_payoff += C
                _.payoff += (R * ((n*C) / (n))-1)  #formular for payoff

            if _.type == 2:
                _.payoff += (R * ((n*C) / n))
        
            if _.type == 3:
                _.payoff += SIGMA   #set payoff given

def compare(player1, player2):
    #confused how to involve this formula below
    #1/(1+np.e**(lmbda*KAPPA))  if that over a threshhold change type
    pass


if __name__ == "__main__":

    #determine how many in study
    population = 1000
    players = []

    #cooperator
    for i in range(int(population*.5)):
        temp = Player()
        temp.Cooperator()
        players.append(temp)

    #defectors
    for i in range(int(population*.25)):
        temp = Player()
        temp.Defector()
        players.append(temp)
    
    #loners
    for i in range(int(population*.25)):
        temp = Player()
        temp.Loner()
        players.append(temp)

    for _ in players:
        print(_.type)

    #playing num rounds to alter payoffs
    sim(100, players, population)

    #shuffle list of players
    random.shuffle(players)

    