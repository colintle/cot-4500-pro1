import math
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method

number_to_find_root_of = 2
approximated_root = approximation_algorithm(number_to_find_root_of)
print("Approximation Algorithm")
print(f"Approximated square root of {number_to_find_root_of}: {approximated_root}\n")

def function(x):
    return (x**3) + 4*(x**2) - 10

root, iterations = bisection_method(function, a=1, b=2, tol=1e-3)
print("Bisection Method")
print(f"The root found is: {root}")
print("The number of iterations bisection method took is " + str(iterations))
print("\n")

def g1(x):
    return x - x**3 - 4*x**2 + 10

def g2(x):
    return (10 - x**3)**0.5 / 2

initial_guess = 1.5
tolerance = 0.000001

print("Fixed-Point Iteration")
root_a, iterations_a, status_a = fixed_point_iteration(g1, initial_guess, tolerance)
print(f"Root (a): {root_a}, Iterations: {iterations_a}, Status: {status_a}")

root_b, iterations_b, status_b = fixed_point_iteration(g2, initial_guess, tolerance)
print(f"Root (b): {root_b}, Iterations: {iterations_b}, Status: {status_b}")
print("\n")

def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

initial_guess = math.pi / 4
tolerance = 1e-6

print("Newton-Raphson Method")
root, iterations, status = newton_raphson_method(f, df, initial_guess, tolerance)
print(f"Root: {root}, Iterations: {iterations}, Status: {status}")