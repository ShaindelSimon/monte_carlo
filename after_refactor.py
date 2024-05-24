import random


def get_random_values(a, b, N):
    """Return list of N uniform-random number in [a, b]."""
    return [random.uniform(a, b) for _ in range(N)]


def apply_function_on_points(points, f):
    """Return list of function values at given points."""
    return [f(x) for x in points]


def monte_carlo_integration(f, a, b, N):
    """
    Estimate the integral of function f, in range [a,b], using Monte Carlo methods
    with N samples.
    """

    points = get_random_values(a, b, N)
    samples = apply_function_on_points(points, f)

    # Compute the average of these function evaluations
    average = sum(samples) / N

    # Multiply the average by the width of the interval (b - a) to approximate the integral
    integral_approximation = (b - a) * average

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
