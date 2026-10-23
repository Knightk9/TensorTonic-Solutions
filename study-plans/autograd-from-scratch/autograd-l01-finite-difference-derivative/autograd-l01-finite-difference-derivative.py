import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    output_1 = 0.0
    output_2 = 0.0
    output_3 = 0.0
    i = 0
    for coefficient in coefficients:
        output_1 += coefficient*pow(x,i)
        output_2 += coefficient*pow((x + h),i)
        i = i + 1

    output_3 = (output_2 - output_1)/h
    return (output_1, output_2, output_3)
