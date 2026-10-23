import numpy as np

def conv2d(image: list, kernel: list, stride: int = 1, padding: int = 0) -> list:
    """
    Returns a two-dimensional list.
    """
    image = np.array(image)
    kernel = np.array(kernel)
    if padding > 0:
        image = np.pad(image, pad_width=padding, mode='constant', constant_values=0)
        
    H, W = image.shape
    kH, kW = kernel.shape
    res_rows = (H - kH) // stride + 1
    res_cols = (W - kW) // stride + 1
    
    res = np.zeros((res_rows, res_cols))
    
    
    for ri in range(res_rows):
        for rj in range(res_cols):
            
            i = ri * stride
            j = rj * stride
            temp_matrix = image[i:i + kH, j:j + kW]
            res[ri, rj] = np.sum(temp_matrix * kernel)
    return res.tolist()