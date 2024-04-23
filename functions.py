import numpy as np
from scipy.stats import norm

def monte_carlo_option_price(S0, K, r, sigma, T, dt, N):
    num_steps = int(T / dt)
    discount_factor = np.exp(-r * T)
    # Initialize arrays for stock prices
    S = np.full(N, S0)
    # Loop over each time step
    for i in range(num_steps):
        # Generate normal random numbers array 
        z = np.random.randn(N)
        # Calculate stock price changes and update the array 
        dS = r * S * dt + sigma * S * z * np.sqrt(dt) 
        S += dS
    payoffs = np.maximum(S - K, 0)
    option_price = discount_factor * np.mean(payoffs)
    return option_price

def black_scholes(S0, K, r, sigma, T):
    d1 = (np.log(S0 / K) + (r + (sigma**2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    C0 = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return C0
  
def monte_carlo_option_price_2(S0, v0, r, theta, omega, xi, K, T, dt, N):
    num_steps = int(T / dt)
    discount_factor = np.exp(-r * T)
    # Initialize arrays for stock prices and volatility 
    S = np.full(N, S0)
    v = np.full(N, v0)
    # Loop over each time step
    for i in range(1, num_steps):
        # Generate normal random numbers arrays 
        z1 = np.random.normal(0, 1, N)
        z2 = np.random.normal(0, 1, N)
        # Calculate and update the volatilities and stock prices
        dv = theta * (omega - v) * dt + xi * np.sqrt(np.maximum(v, 0)) * z2 * np.sqrt(dt)
        v = np.maximum(v + dv, 0)  # v can't be negative
        dS = r * S * dt + np.sqrt(v) * S * z1 * np.sqrt(dt)
        S += dS
    payoffs = np.maximum(S - K, 0)
    option_price = discount_factor * np.mean(payoffs)   
    return option_price