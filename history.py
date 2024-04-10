import numpy as np
import random
import matplotlib.pyplot as plt
import math
from figure2 import f_dot, z_dot

N = 5
SIGMA = 0.5
R = 1.8

class Contributor:
    def __init__(self, initial_probability):
        self.probability = initial_probability
    
    def update_probability(self, f_dot, z_dot, n, r, sigma, delta_t):
        f = self.probability / (1 - sigma + self.probability * (r - 1))
        f_new = f + f_dot * delta_t
        self.probability = f_new * (1 - self.probability - z_dot * delta_t)
        

class Loner:
    def __init__(self, initial_probability):
        self.probability = initial_probability
    
    def update_probability(self, z_dot, delta_t):
        self.probability += z_dot * delta_t

class Defector:
    def __init__(self, initial_probability):
        self.probability = initial_probability
    
    def update_probability(self, f_dot, delta_t):
        f = self.probability / (1 - self.probability)
        f_new = f + f_dot * delta_t
        self.probability = f_new / (1 + f_new)

def simulate(population, x, y, delta_t=0.001, iterations=200000):
    """_summary_

    Args:
        population (int): total number of participants
        x (float): fraction of cooperators
        y (float): fraction of defectors
        delta_t (float, optional): _description_. Defaults to 0.001.
        iterations (int, optional): _description_. Defaults to 200000.
    """
    actors = []
    for _ in range(population):
        frac = random.random()
        if frac < x:
            actors.append(Contributor())
        elif frac < (x + y):
            actors.append(Defector())
        else:
            actors.append(Loner())
    

    contributor = Contributor(0.5)
    loner = Loner(0.25)
    defector = Defector(0.25)

    contributor_probs = [contributor.probability]
    loner_probs = [loner.probability]
    defector_probs = [defector.probability]

    for _ in range(iterations):
        f_dot_val = f_dot(contributor.probability, defector.probability, loner.probability, N, R)
        z_dot_val = z_dot(contributor.probability, defector.probability, loner.probability, N, R, SIGMA)
        
        contributor.update_probability(f_dot_val, z_dot_val, N, R, SIGMA, delta_t)
        loner.update_probability(z_dot_val, delta_t)
        defector.update_probability(f_dot_val, delta_t)
        
        contributor_probs.append(contributor.probability)
        loner_probs.append(loner.probability)
        defector_probs.append(defector.probability)

    return contributor_probs, defector_probs, loner_probs

if __name__ == "__main__":
    num_steps = 200000
    time_steps = np.arange(num_steps + 1)
    c_probs, d_probs, l_probs = simulate(iterations=num_steps)
    plt.plot(time_steps, c_probs, label='Contributors')
    plt.plot(time_steps, d_probs, label='Defectors')
    plt.plot(time_steps, l_probs, label='Loners')
    plt.title('Replicator Dynamics Simulation')
    plt.xlabel('Time Steps')
    plt.ylabel('Probability')
    plt.legend()
    plt.grid(True)
    plt.show()
