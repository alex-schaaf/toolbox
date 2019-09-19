import numpy as np


def cubify(arr:np.ndarray, newshape:np.ndarray) -> np.ndarray:
    """
    Divide n-dimensional cube into i n-dimensional subcubes.
    
    
    Args:
        arr (np.ndarray): Input ndarray to split up.
        newshape (tuple): Shape of the output cubes. Must divide 
            oldshape evenly or else ValueError will be raised!
    Returns:
        (np.ndarray)
    
    Source:
        https://stackoverflow.com/questions/42297115/numpy-split-cube-into-cubes
    """
    oldshape = np.array(arr.shape)
    repeats = (oldshape / newshape).astype(int)
    tmpshape = np.column_stack([repeats, newshape]).ravel()
    order = np.arange(len(tmpshape))
    order = np.concatenate([order[::2], order[1::2]])
    # newshape must divide oldshape evenly or else ValueError will be raised
    return arr.reshape(tmpshape).transpose(order).reshape(-1, *newshape)