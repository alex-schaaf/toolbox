import numpy as np
from typing import Iterable

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


def get_regular_grid_coords(extent: Iterable, shape: Iterable) -> np.ndarray:
    """Generate regular grid cell coordinates given an extent
    and the desired output shape.

    Args:
        extent (Iterable): (x, X, y, Y, z, Z)
        shape (Iterable): (nx, ny, nz)

    Returns:
        (np.ndarray) Coordinate array shaped (3, ...)
    """
    X = np.linspace(extent[0], extent[1], shape[0])
    Y = np.linspace(extent[2], extent[3], shape[1])
    Z = np.linspace(extent[4], extent[5], shape[2])

    cell_coords = []
    for x in X:
        for y in Y:
            for z in Z:
                cell_coords.append([x, y, z])

    return np.array(cell_coords)