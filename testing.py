import numpy as np
import matplotlib.pyplot as plt
KAPPA = 0.1

def logistic(lmbda):
    return 1 / (1 + np.exp(lmbda * KAPPA)) #trying this to resolve too large error 
    #return 1/(1+np.e**(lmbda*KAPPA))

def main():
    x = np.arange(-100, 100, 0.5)
    y = np.apply_along_axis(logistic, 0, x)
    plt.plot(x, y)
    plt.title('Test')
    plt.xlabel('Lamdba')
    plt.ylabel('Logigistic')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    print(logistic(2))
    print(logistic(-50))

    main()