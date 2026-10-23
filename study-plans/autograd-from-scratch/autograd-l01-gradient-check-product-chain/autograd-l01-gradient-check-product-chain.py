import numpy as np

def gradient_check_product_chain(
    a: float,
    b: float,
    c: float,
    f: float,
    h: float,
) -> tuple[float, list, list, float]:
    """
    Returns loss, analytic gradients, numerical gradients, and maximum error.
    """
    e = float(a * b + c)
    L = float(e * f)
    
    # 1. Đạo hàm giải tích (ép kiểu float từng phần tử)
    da_analytic = float(f * b)
    db_analytic = float(f * a)
    dc_analytic = float(f)
    df_analytic = float(e)
    list_analytic_gradient = [da_analytic, db_analytic, dc_analytic, df_analytic]
    
    # 2. Đạo hàm số (ép kiểu float từng phần tử)
    e_a = (a + h) * b + c
    da_numerical = float(((e_a * f) - L) / h)
    
    e_b = a * (b + h) + c
    db_numerical = float(((e_b * f) - L) / h)
    
    e_c = a * b + (c + h)
    dc_numerical = float(((e_c * f) - L) / h)
    
    df_numerical = float(((e * (f + h)) - L) / h)
    
    list_numerical_gradient = [da_numerical, db_numerical, dc_numerical, df_numerical]
    
    # 3. Tính sai lệch lớn nhất dưới dạng float
    analytic_arr = np.array(list_analytic_gradient)
    numerical_arr = np.array(list_numerical_gradient)
    the_largest_loss = float(np.max(np.abs(analytic_arr - numerical_arr)))
    
    return (L, list_analytic_gradient, list_numerical_gradient, the_largest_loss)