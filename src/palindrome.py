from typing import Tuple
import numpy as np
import numba as nb

def get_palindromes(digits: str, l: int, stretch_mode: bool = False) -> Tuple[list[int], list[np.ndarray]]:
    """
    Return an array of palindromes subsets from an sequence of digits (string) based on a given length.
    If stretch_mode is True, the function will also return all the palindromes larger than l.

    It returns a tuple of two lists:
    - the first list contains the indexes of the palindromes in the original sequence
    - the second list contains the palindromes themselves
    """

    @nb.njit()
    def finder(arr: np.ndarray, l: int) -> Tuple[list, list]:
        idx = []
        pld = []
        n = arr.shape[0]
        mid = l // 2
        for i in nb.prange(n):
            for j in range(mid):
                if arr[i+j] != arr[i+l-j-1]:
                    break
                if j == mid - 1:
                    idx.append(i)
                    pld.append(arr[i:i+l])
        return idx, pld

    @nb.njit()
    def stretcher(arr: np.ndarray, idx: list[int], pld: list[np.ndarray], l: int) -> Tuple[list, list]:
        new_idx = []
        new_pld = []
        for i in idx:
            new_l = l
            s = True
            while s:
                i -= 1
                new_l += 2
                mid = new_l //2
                for j in range(mid):
                    if arr[i+j] != arr[i+new_l-j-1]:
                        s = False
                        break
                    if j == mid - 1:
                        new_idx.append(i)
                        new_pld.append(arr[i:i+new_l])
        return new_idx + idx, new_pld + pld

    arr = np.array([digits]).view(int)
    idx, pld = finder(arr, l)
    if stretch_mode and len(idx) > 0:
        idx, pld = stretcher(arr, idx, pld, l)
    
    pld = [''.join((p-48).astype(str).tolist()) for p in pld]
    return idx, pld