import random


def monte_carlo_integration(f, a, b, N):
    """
    Estimate the integral of function f, in range [a,b], using Monte Carlo methods
    with N samples.

    Parameters:
    f (function): The function to integrate.
    a (float): The lower bound of the integration interval.
    b (float): The upper bound of the integration interval.
    N (int): The number of random samples to generate.

    Returns:
    float: The approximate value of the integral.
    """

    total_sum = 0

    # Generate N random samples uniformly distributed between a and b
    for _ in range(N):
        x = random.uniform(a, b)
        total_sum += f(x)

    # Compute the average of these function evaluations
    average_value = total_sum / N

    # Multiply the average by the width of the interval (b - a) to approximate the integral
    integral_approximation = (b - a) * average_value

    return integral_approximation


# Example usage

# Define the function to integrate
def f(x):
    return x ** 2  # Example function x^2


# Integration bounds
a = 0
b = 1

# Number of samples
N = 1000

# Compute the integral
result = monte_carlo_integration(f, a, b, N)
print(f"The approximate value of the integral is: {result}")
