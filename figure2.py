"""
Code to replicate Figure 2 from the paper.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

# Parameters of the model
N = 5
SIGMA = 0.5
R = 1.8

def f(x, y):
    return x/(x+y)    
    
def f_upper(z, r, n):
    temp = (1 - z**n) / (1 - z)
    return 1 + (r - 1) * z**(n - 1) - r * temp / n

# the function f = x/(x+y)
def f_dot(x, y, z, n, r) ->  float:
    """first derivative of f

    Args:
        x (float): probability of cooperators
        y (float): probability of defectors
        z (float): probabliity of loners
        n (int): sample size 
        r (float): rate of gain
    """
    prop = f(x, y)
    return prop * (1 - prop) * f_upper(z, r, n)

def z_dot(x, y, z, n, r, sigma) -> float:
    """_summary_

    Args:
        x (float): probability of cooperators
        y (float): probability of defectors        
        z (_type_): _description_
        n (_type_): _description_
        r (_type_): _description_
        sigma (_type_): _description_

    Returns:
        float: _description_
    """
    f = x/(x+y)
    z_term = z * (1 - z) * (1 - z**(n - 1))
    f_term = sigma - f * (r - 1)
    return z_term * f_term

if __name__ == "__main__":
    # Define the vertices of the triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])

    # Plot the triangle
    plt.figure(figsize=(8, 6))
    plt.plot(vertices[:, 0], vertices[:, 1], 'k--', linewidth=0.8)  # Plot lines connecting the vertices

    # Label corners
    plt.text(1, 0, r'$\mathbf{e}_c$', fontsize=12, verticalalignment='bottom')
    plt.text(0, 0, r'$\mathbf{e}_d$', fontsize=12, verticalalignment='bottom')
    plt.text(0.5, np.sqrt(3)/2, r'$\mathbf{e}_l$', fontsize=12, verticalalignment='bottom')

    # Define the range of z-values within the triangle
    z_values = np.linspace(0.01, 0.99, 200)


    # Initialize values
    x = 1 / 4
    y = 1 / 4
    z = 1 - (x + y)
    delta_t = 0.001

    # Perform iterations to simulate dynamics
    iterations = 10000
    x_values = [x]
    y_values = [y]
    z_values = [z]

    for _ in range(iterations):
        z_dot_val = z_dot(x, y, z, N, R, SIGMA)
        f_dot_val = f_dot(x, y, z, N, R)
        z += z_dot_val * delta_t
        new_f = f(x, y) + f_dot_val * delta_t
        x = new_f * (1 - z)
        y = 1 - (y + z)

        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

    # Plot the trajectory
    x_coords = [0.5 * x_values[i] + y_values[i] for i in range(len(x_values))]
    y_coords = [math.sqrt(3)/2 * x_values[i] for i in range(len(x_values))]

    plt.plot(x_coords,y_coords, label='x (Cooperators)')
    plt.title('Replicator Dynamics')
    plt.legend()
    plt.grid(True)
    plt.show()
