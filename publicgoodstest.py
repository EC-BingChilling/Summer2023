"""
Graphs based on Replicator Dynamics paper

N is the number of players

"""
import numpy as np
import matplotlib.pyplot as plt

N = 5
SIGMA = 0.5

# Function to calculate replicator dynamics
def replicator_dynamics(x, pi, avg_payoff):
    """
    
    """
    return x * (pi - avg_payoff)

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


"""
# User input for parameters
dt = 0.01
num_steps = 500

# Initialize arrays to store results
time_points = np.arange(0, num_steps * dt, dt)
strategy_frequencies = np.zeros((num_steps, N))

# Random initial frequencies
x_initial = np.random.rand(N)
x_initial /= np.sum(x_initial)

# Run the replicator dynamics simulation
current_frequencies = x_initial.copy()
for step in range(num_steps):
    strategy_frequencies[step, :] = current_frequencies
    avg_payoff = average_payoff(current_frequencies, sigma, r)
    current_frequencies += dt * replicator_dynamics(current_frequencies, sigma, avg_payoff)
"""
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

"""
# Plot simplex boundary lines
plt.plot([0, 1, 0.5, 0], [0, 0, np.sqrt(3)/2, 0], 'k--', linewidth=0.8)

# Plot trajectory on the simplex
plt.plot(strategy_frequencies[:, 0], strategy_frequencies[:, 1], label='Strategy Trajectory', color='blue')

# Label corners
plt.text(1, 0, r'$\mathbf{e}_c$', fontsize=12, verticalalignment='bottom')
plt.text(0, 0, r'$\mathbf{e}_d$', fontsize=12, verticalalignment='bottom')
plt.text(0.5, np.sqrt(3)/2, r'$\mathbf{e}_l$', fontsize=12, verticalalignment='bottom')

plt.xlabel('Strategy 1')
plt.ylabel('Strategy 2')
plt.title('Dynamics Theory Simplex in Game Theory')
plt.legend()
plt.grid(True)
plt.show()
"""