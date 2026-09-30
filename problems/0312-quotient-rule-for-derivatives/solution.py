import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    gpowers = len(g_coeffs) - 1
    hpowers = len(h_coeffs) - 1
    yg = 0
    yh = 0
    dyg = 0
    dyh = 0
    for i in range(gpowers+1):
        yg += g_coeffs[i]*x**gpowers
        if gpowers == 0:
            dyg += 0
        else:
            gpowers -= 1
            dyg += ((gpowers+1)*g_coeffs[i])*x**gpowers
    for b in range(hpowers+1):
        yh += h_coeffs[b]*x**hpowers
        if hpowers == 0:
            dyh += 0
        else:
            hpowers -= 1
            dyh += ((hpowers+1)*h_coeffs[b])*x**hpowers
    return (dyg*yh - yg*dyh) / (yh**2)