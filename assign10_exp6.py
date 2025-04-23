"""The bisection method is a technique for finding solutions (roots) to equations with a single
unknown variable. Given a polynomial function f, try to find an initial interval off by
random probe. Store all the updates in an Numpy array. Plot the root finding process using
the matplotlib/pyplot library."""

import numpy as np
import random

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def find_initial_interval(func, lower=-10, upper=10, max_tries=1000):
    for _ in range(max_tries):
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
        if a > b:
            a, b = b, a
        if func(a) * func(b) < 0:
            return a, b
    raise ValueError("Could not find a valid initial interval")

def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    updates = []
    for i in range(max_iter):
        c = (a + b) / 2.0
        updates.append([i, a, b, c, func(c)])
        print(f"Iter {i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {func(c):.6f}")
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

a, b = find_initial_interval(f)
updates = bisection_method(f, a, b)
