"""import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

# parameters of the model
N = 5
SIGMA = 0.5
R = 1.8


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


def f_upper(z, r, n):
    temp = (1-z**n)/(1-z)
    return 1 + (r - 1)*z**(n-1) - r*temp/n

for r, color in zip([2.5, 2.0, 1.5], ['blue', 'red', 'green']):
    F_values = f(z_values, r)
    
    # Create a closed loop within the triangle's boundaries
    points = np.column_stack((z_values, F_values))
    inside_triangle = Path(vertices).contains_points(points)
    inside_points = points[inside_triangle]
    
    # Sort the points in a spiraling order
    sorted_indices = np.argsort(np.arctan2(inside_points[:, 1], inside_points[:, 0]))
    inside_points = inside_points[sorted_indices]
    
    plt.plot(inside_points[:, 0], inside_points[:, 1], label=f"r = {r}", color=color)

def f_dot(x, y, z, n, r):
    f = x/(x+y)
    return f * (1-f) * f_upper(z, r, n)

def z_dot(f, n, r, sigma):
    z_term = z*(1-z)*(1-z**(n-1))
    f_term = sigma - f*(r-1)
    return z_term * f_term

plt.xlabel('z')
plt.ylabel('F(z)')
plt.title('Variation of P_d - P_c with z and Triangle')
plt.legend()

# Fill the triangle with white color
plt.fill(vertices[:, 0], vertices[:, 1], color='white')

plt.grid(True)
plt.axis('equal')  # Equal aspect ratio
plt.show()

# N = 5, r = 1.8, sigma = 0.5
#plug into eq 9

if __name__ == "__main__":
    x = 1/3
    y = 1/3
    z = 1-(x+y)
    delta_t = 0.001
    z_t = z + z_dot(z, N, R, SIGMA)
    denominator = 1- z_t #xt + yt
    f_t = x/(x+y) + f_dot(x, y, z, N, R) * delta_t
    x_t = f_t *  denominator
    y_t = 1 - (x_t + z_t)
    #print(x/(x+y), f_dot(x, y, z, N, R))
    #print(z, z_dot(z, N, R, SIGMA))
    print(x, y, z)
    print(x_t, y_t, z_t)"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Parameters of the model
N = 5
SIGMA = 0.5
R = 1.8

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


# Initialize values
x = 1 / 2
y = 1 / 4
z = 1 - (x + y)
delta_t = 0.001

# Perform iterations to simulate dynamics
iterations = 200000
x_values = [x]
y_values = [y]
z_values = [z]

for _ in range(iterations):
    z_dot_val = z_dot(x, y, z, N, R, SIGMA)
    f_dot_val = f_dot(x, y, z, N, R)
    z += z_dot_val * delta_t
    new_f = f(x, y) + f_dot_val * delta_t
    x = new_f * (1 - z)
    y = 1 - (x + z)

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
