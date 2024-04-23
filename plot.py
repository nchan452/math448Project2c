import numpy as np
import matplotlib.pyplot as plt

def CreatePlot(A, B, ln_E, ln_N):
    print(f"A = {A:.12f}")
    print(f"B = {B:.12f}")
    # Use the coefficients to create the line of best fit
    ln_E_fit = A * ln_N + B
    plt.figure(figsize=(10, 6))
    plt.scatter(ln_N, ln_E, color='blue',
                label='Data points')  # Plot the data points
    plt.plot(ln_N,
             ln_E_fit,
             color='red',
             label=f'Least Squares Line: ln|E| = {A:.3f} lnN + {B:.3f}'
             )  # Plot the line of best fit 
    for i, txt in enumerate(ln_E):
      plt.annotate(f'({ln_N[i]:.5f}, {txt:.5f})', (ln_N[i], ln_E[i]),
                   textcoords="offset points",
                   xytext=(0, 10),
                   ha='center') 
    # Label the axes and add a legend
    plt.xlabel('ln(N)')
    plt.ylabel('ln(|E|)')
    plt.title('Least Squares Line for ln(|E|) vs ln(N)')
    plt.legend()
    # Print out the equation of the line
    print(f"The least squares line is given by: ln|E| = {A:.3f} lnN + {B:.3f}\n")
    # Display the plot
    plt.show()