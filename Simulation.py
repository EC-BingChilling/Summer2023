import random
import matplotlib.pyplot as plt
import numpy as np
import testing as logi

R = 1.8 #rate
C = 1 #contribution for cooperators
SIGMA = 0.3 #payoff for loners

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
    """find difference in payoff, then find the percentage they change based on logistic func

    Args:
        player1 (Player): player of the class structure Player
        player2 (Player): player of the class structure Player
    """
    temp = player1.payoff - player2.payoff 
    percent_of_change =  logi.logistic(temp)

    if percent_of_change <= random.random():
        player1.type = player2.type

def count(players):
    """shows the total number of players of each type (cooperator, defector, loner)

    Args:
        players (list): list of players from Player class

    Returns:
        list: each count of type of player [c,d,l]
    """
    #set baselines for each type
    count1 = 0
    count2 = 0
    count3 = 0

    #alter baselines based on each player type
    for player in players:
        if player.type == 1:
            count1 += 1
        elif player.type == 2:
            count2 += 1
        else:
            count3 += 1
    list = [count1, count2, count3]
    return list

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


    """for i in range(100):

        #show nums of each type
        print(count(players))

        #playing num rounds to alter payoffs
        sim(100, players, population)

        #shuffle list of players and compare players to change type
        random.shuffle(players)
        for i in range(1,10,2):
            compare(players[i], players[i+1])"""
   
    # Define the vertices of the triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])


    # Plot the triangle
    plt.figure(figsize=(8, 6))
    plt.plot([0, 1, 0.5, 0], [0, 0, np.sqrt(3)/2, 0], 'k-')  # Plot lines connecting the vertices


    #labbeling the corners
    plt.text(0, 0, r'Cooperators', fontsize=12, verticalalignment='top')
    plt.text(1, 0, r'Loners', fontsize=12, verticalalignment='top')
    plt.text(0.5, np.sqrt(3)/2, r'Defectors', fontsize=12, verticalalignment='bottom')


    points = []
    for i in range(35):
        sim(100, players, population)


        random.shuffle(players)
        for i in range(1,10,2):
            compare(players[i], players[i+1])


        counts = count(players)


        percentages = [counts[0]/population, counts[1]/population, counts[2]/population]


        point_position = vertices[0] * percentages[0] + vertices[1] * percentages[1] + vertices[2] * percentages[2]
        points.append(point_position)


    points = np.array(points)
    plt.plot(points[:,0], points[:,1], 'r-', linewidth=2)


    plt.title('Simulation')
    plt.grid(True)
    plt.show()