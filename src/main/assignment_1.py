def bisection_method(f, a, b, tol, max_iter=1000):
    i = 0
    left = a
    right = b
    p = left

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2
        if f(left) * f(p) < 0:
            right = p
        else:
            left = p
    
    return p, i

def fixed_point_iteration(g, initial_guess, tol, max_iter=50):
    p0 = initial_guess
    for i in range(1, max_iter + 1):
        try:
            p = g(p0)
            if abs(p - p0) < tol:
                return p, i, "SUCCESS"
        except OverflowError:
            return None, i, "FAILURE -> Overflow encountered"
        except ValueError:
            return None, i, "FAILURE -> Math domain error"
        
        p0 = p

    return None, max_iter, "FAILURE: Reached maximum iterations"

def newton_raphson_method(f, df, x0, tol, max_iter=50):
    for i in range(max_iter):
        f_val = f(x0)
        df_val = df(x0)

        if df_val == 0:
            return None, i, "FAILURE: Derivative is zero"
        
        x1 = x0 - f_val / df_val

        if abs(x1 - x0) < tol:
            return x1, i + 1, "SUCCESS"
        x0 = x1

    return x0, max_iter, "FAILURE: Max iterations reached"

def approximation_algorithm(value, tol=0.00001):
    if value < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    x0 = value
    diff = x0
    x = x0
    iter_count = 0

    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (value / (2 * x))
        diff = abs(x - y)

    return x