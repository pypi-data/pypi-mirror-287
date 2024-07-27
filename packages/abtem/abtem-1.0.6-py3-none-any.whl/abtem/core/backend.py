from __future__ import annotations

import types
import warnings
from numbers import Number
from typing import Union

import dask.array as da
import numpy as np
import scipy

from abtem.core.config import config

try:
    import cupy as cp
except ModuleNotFoundError:
    cp = None
except ImportError:
    if config.get("device") == "gpu":
        warnings.warn(
            "The CuPy library could not be imported. Please check your installation, or change your configuration to "
            "use CPU."
        )
    cp = None


try:
    import cupyx
except:
    cupyx = None

ArrayModule = Union[types.ModuleType, str]


def check_cupy_is_installed():
    if cp is None:
        raise RuntimeError("CuPy is not installed, GPU calculations disabled")


def xp_to_str(xp):
    if xp is np:
        return "numpy"

    check_cupy_is_installed()

    if xp is cp:
        return "cupy"

    raise ValueError(f"array module must be NumPy or CuPy, not {xp}")


def validate_device(device):
    if device is None:
        return config.get("device")

    return device


def get_array_module(x: np.ndarray | str = None) -> ArrayModule:
    """
    Get the array module (NumPy or CuPy) for a given array or string.

    Parameters
    ----------
    x : numpy.ndarray, cupy.ndarray, dask.array.Array, str, None
        The array or string to get the array module for. If None, the default device is used.
    
    Returns
    -------
    numpy or cupy
        The array module.
    """

    if x is None:
        return get_array_module(config.get("device"))

    if isinstance(x, da.core.Array):
        return get_array_module(x._meta)

    if isinstance(x, str):
        if x.lower() in ("numpy", "cpu"):
            return np

        if x.lower() in ("cupy", "gpu"):
            check_cupy_is_installed()
            return cp

    if isinstance(x, np.ndarray):
        return np

    if x is np:
        return np

    if isinstance(x, Number):
        return np

    if cp is not None:
        if isinstance(x, cp.ndarray):
            return cp

        if x is cp:
            return cp

    raise ValueError(f"array module specification {x} not recognized")


def device_name_from_array_module(xp):
    if xp is np:
        return "cpu"

    if xp is cp:
        return "gpu"

    assert False


def get_scipy_module(x):
    xp = get_array_module(x)

    if xp is np:
        return scipy

    if xp is cp:
        return cupyx.scipy


def get_ndimage_module(x):
    xp = get_array_module(x)

    if xp is np:
        import scipy.ndimage

        return scipy.ndimage

    if xp is cp:
        import cupyx.scipy.ndimage

        return cupyx.scipy.ndimage


def asnumpy(array):
    if cp is None:
        return array

    if isinstance(array, da.core.Array):
        return array.map_blocks(asnumpy)

    return cp.asnumpy(array)


def copy_to_device(array: np.ndarray, device: str):
    """
    Copy an array to a different device (CPU or GPU) using CuPy.

    Parameters
    ----------
    array : numpy.ndarray
        The array to copy.
    device : str
        The device to copy to. Either 'cpu' or 'gpu'.

    Returns
    -------
    numpy.ndarray or cupy.ndarray
        The array copied to the specified device.
    """
    old_xp = get_array_module(array)
    new_xp = get_array_module(device)

    if old_xp is new_xp:
        return array

    if isinstance(array, da.core.Array):
        return array.map_blocks(
            copy_to_device, meta=new_xp.array((), dtype=array.dtype), device=device
        )

    if new_xp is np:
        return cp.asnumpy(array)

    if new_xp is cp:
        return cp.asarray(array)

    raise RuntimeError("Invalid device specified")
