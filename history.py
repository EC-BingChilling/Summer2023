import numpy as np
import matplotlib.pyplot as plt
import math
from figure1 import f_dot
f_dot_val = f_dot(contributor.probability, defector.probability, loner.probability, N, R)


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

N = 5
SIGMA = 0.5
R = 1.8
delta_t = 0.001
iterations = 200000

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

time_steps = np.arange(iterations + 1)
plt.plot(time_steps, contributor_probs, label='Contributors')
plt.plot(time_steps, defector_probs, label='Defectors')
plt.plot(time_steps, loner_probs, label='Loners')
plt.title('Replicator Dynamics Simulation')
plt.xlabel('Time Steps')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()
