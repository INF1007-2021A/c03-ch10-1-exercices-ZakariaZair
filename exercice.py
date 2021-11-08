#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    arr = np.linspace(-1.3, 2.5, 64)
    return arr


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    for coord in cartesian_coordinates:
       arr = np.append(arr, [[np.sqrt(coord[0] ** 2 + coord[1] ** 2), np.arctan2(coord[1], coord[0])]], 0)
    
    return arr


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
