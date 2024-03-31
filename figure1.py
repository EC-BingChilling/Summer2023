"""
Graphs based on Replicator Dynamics paper

N is the number of players

"""
import numpy as np
import matplotlib.pyplot as plt

N = 5
SIGMA = 0.5

<<<<<<< HEAD
"""
# Function to calculate replicator dynamics
def replicator_dynamics(x, pi, avg_payoff):
    return x * (pi - avg_payoff)
"""
    
=======
# Function to calculate replicator dynamics
def replicator_dynamics(x, pi, avg_payoff):
    """
    
    """
    return x * (pi - avg_payoff)

>>>>>>> 1278931fa19e5e06f03784170ad193a577b530d4
def f(z, r):
    """Returns the difference P_d - P_c

    P_d = payoff for defector
    P_c = payoff for cooperator

    Args:
        z (Numpy array): fraction of loners
        r (float): rate of interest between 1 and N
    """
    temp = (1-z**N)/(1-z)
    return 1 + (r - 1)*z**(N-1) - r*temp/N

def average_payoff(z, r, sigma):
    """
    Computes the expected payoff for the population

    Args:
        z (Numpy array): fraction of loners
        r (float): rate of interest between 1 and N
        sigma (float): fixed payoff for loners
    """
    return sigma - ((1 - z) * sigma - (r - 1) * z) * (1 - z**(N - 1))

# Plotting
plt.figure(figsize=(8, 6))
z_values = np.linspace(0, 1, 200)

plt.plot(z_values, f(z_values, r=2.5), label="r > 2")
plt.plot(z_values, f(z_values, r=2.0), label="r = 2")
plt.plot(z_values, f(z_values, r=1.5), label="r < 2")

plt.xlabel('z')
plt.ylabel('F(z)')
plt.title('Variation of P_d - P_c with z')
plt.legend()
plt.show()