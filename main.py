import numpy as np
import matplotlib.pyplot as plt
# Import my functions from my other files
from plot import CreatePlot
from functions import black_scholes
from functions import monte_carlo_option_price
from functions import monte_carlo_option_price_2

# Define parameters
S0 = 10.0  
K = 10.0  
r = 0.02  
sigma = 0.25  
T = 0.25  
dt = 0.025  
# For problem 2
v0 = 0.0625  
theta = 3.0  
omega = 0.0625 
xi = 0.1 

# Calculating the option prices with different numbers of simulations
n10 = monte_carlo_option_price(S0, K, r, sigma, T, dt, 10)
n100 = monte_carlo_option_price(S0, K, r, sigma, T, dt, 100)
n1000 = monte_carlo_option_price(S0, K, r, sigma, T, dt, 1000)
n10000 = monte_carlo_option_price(S0, K, r, sigma, T, dt, 10000)
# Compute using black scholes method
bs = black_scholes(S0, K, r, sigma, T)

# Calculating the errors
E10 = np.abs(n10 - bs)
E100 = np.abs(n100 - bs)
E1000 = np.abs(n1000 - bs)
E10000 = np.abs(n10000 - bs)

# Printing the results in a table
print("\nBlack-Scholes: ")
print(f"\t{bs}\n")
print("Monte Carlo method: ")
print(f"{'Number of Simulations':<25}|{'Monte Carlo Method':<25}|{'|E|':>10}")
print("-" * 64)
print(f"{'N = 10':<25}|{n10:<25.12f}|{E10:>10.12f}")
print(f"{'N = 100':<25}|{n100:<25.12f}|{E100:>10.12f}")
print(f"{'N = 1000':<25}|{n1000:<25.12f}|{E1000:>10.12f}")
print(f"{'N = 10000':<25}|{n10000:<25.12f}|{E10000:>10.12f}\n")

# Create the graph for problem 1b
# Create arrays for N trials and E values
N = np.array([10, 100, 1000, 10000])
E = np.array([E10, E100, E1000, E10000])
# Take the natural log of N and E
ln_N = np.log(N)
ln_E = np.log(E)
# Linear regression to find the best fit line
A, B = np.polyfit(ln_N, ln_E, 1)
CreatePlot(A, B, ln_E, ln_N)

# Calculating the option prices with the second method
n10 = monte_carlo_option_price_2(S0, v0, r, theta, omega, xi, K, T, dt, 10)
n100 = monte_carlo_option_price_2(S0, v0, r, theta, omega, xi, K, T, dt, 100)
n1000 = monte_carlo_option_price_2(S0, v0, r, theta, omega, xi, K, T, dt, 1000)
n10000 = monte_carlo_option_price_2(S0, v0, r, theta, omega, xi, K, T, dt, 10000)

# Printing the results in a table
print("Monte Carlo method 2: ")
print(f"{'Number of Simulations':<25}|{'Monte Carlo Method':<25}")
print("-" * 64)
print(f"{'N = 10':<25}|{n10:<25.12f}")
print(f"{'N = 100':<25}|{n100:<25.12f}")
print(f"{'N = 1000':<25}|{n1000:<25.12f}")
print(f"{'N = 10000':<25}|{n10000:<25.12f}\n")