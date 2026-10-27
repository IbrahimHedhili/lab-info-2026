import numpy as np
import math
def median(an_array):
    median_value = None
    array_len = len(an_array)
    sorted_array = np.sort(an_array)
    if array_len % 2 == 0: 
        median_value = sorted_array[int(array_len/2)-1] + sorted_array[int(array_len/2)]
        median_value /= 2
    elif array_len % 2 != 0: 
        median_value = sorted_array[int((array_len - 1)/2)]
    return median_value

def percentile25(arr):
    """A function that determines the value under which lies the 25% of the values 
    and the value under wich lies the 25% of the values.

    Args:
        arr (numpy.ndarray): the array for which the median is to be calculated

    Returns:
        float: the value under which lies the 25% of the values
        float: the value above which lies the 25% of the values
    """

    sorted_arr = np.sort(arr)

    top_25 =  sorted_arr[math.floor(len(arr)*3/4)-1]
    bottom_25 = sorted_arr[math.ceil(len(arr)/4)]
    
    return [top_25, bottom_25]

def percentile(arr,x):
    """A function that determines the value under which lies the x% of the values 
    and the value under wich lies the x% of the values.

    Args:
        arr (numpy.ndarray): the array for which the median is to be calculated
        x (float): the %

    Returns:
        float: the value under which lies the x% of the values
        float: the value above which lies the x% of the values
    """

    sorted_arr = np.sort(arr)

    top_x =  sorted_arr[math.floor(len(arr) * (100 - x) / 100)-1]
    bottom_x = sorted_arr[math.ceil(len(arr) * x / 100)]
    
    return [top_x, bottom_x]

def mean(arr):
    """A function that calculates the mean value of the elements in the given array.

    Args:
        arr (numpy.ndarray): the array for which the mean is to be calculated

    Returns:
        float: the mean
    """
    a_mean = 0;
    for i in range(len(arr)):
        a_mean += arr[i] 
    
    a_mean /= len(arr)
    return a_mean

def variance(arr):
    """A function that calculates the variance of the elements in the given array.

    Args:
        arr (numpy.ndarray): the array for which the mean is to be calculated

    Returns:
        float: the variance
    """
    a_mean = mean(arr)
    a_var = 0

    for i in range(len(arr)):
        a_var += (arr[i] - a_mean) * (arr[i] - a_mean)
    
    a_var /= (len(arr) - 1)
    return a_var

def standarddeviation(arr):
    """A function that calculates the standard deviation of the elements in the given array.

    Args:
        arr (numpy.ndarray): the array for which the mean is to be calculated

    Returns:
        float: the variance
    """
    return math.sqrt(variance(arr))

def stdmean(arr):
    """A function that calculates the the standard deviation from the mean of the elements in the given array.

    Args:
        arr (numpy.ndarray): the array for which the mean is to be calculated

    Returns:
        float: the standard deviation from the mean
    """
    return standarddeviation(arr)/math.sqrt(len(arr))

def crea_float_casuali(min_val, max_val, n_elementi, decimali = None, seed = None):
    """
    Genera un array 1D di float casuali distribuiti uniformemente
    con un numero specifico di cifre decimali.
    """
    rng = np.random.default_rng(seed)
    
    # 1. Genera i float casuali nel range stabilito
    array_raw = rng.uniform(min_val, max_val, size=n_elementi)
    
    # 2. Arrotonda al numero di decimali desiderato
    array_arrotondato = np.round(array_raw, decimals=decimali)
    
    return array_arrotondato