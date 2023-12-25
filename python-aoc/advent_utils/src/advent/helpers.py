'''
Different somewhat generic helper functions and structures

Intended to be used as `from advent.helpers import *` while solving, ofc cleaning up later
'''

# Imports, some for namespace, some for type hints

from typing import List, Tuple, Dict, Set, Union, Any, Annotated, Iterator
from itertools import product, chain
from collections import defaultdict
from functools import reduce, cache
from pprint import pprint
import numpy as np
import networkx as nx
from networkx.algorithms.connectivity.cuts import minimum_edge_cut


# Strucutres
text_number_tr = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

number_text_tr = {value: key for key, value in text_number_tr.items()}

# direction tuples

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

# Functions
def prod(foo):
    return reduce(lambda x, y: x*y, foo)

def print_grid(grid):
    '''Prints out a 2D grid, no assumptions about the value type'''
    for i in grid:
        print(i)

def iter_grid(grid: List[List[Any]]) -> Iterator[Tuple[int, int, Any]]:
    '''Iterates over a grid, yielding x, y, value'''
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            yield x, y, value

def iter_neigbours(dim: int) -> List[Tuple[int,...]]:
    '''Returns a list of neighbours cells for a given grid of n dimensions'''
    return list(product([-1, 0, 1], repeat=dim))

def iter_ud_neigbours(dim: int) -> List[Tuple[int,...]]:
    '''Returns a list of Von Neumann neighbours (UDLR) for a given grid of n dimensions'''
    return list(filter(lambda x: (0 in x) and (x != [0]*dim), list(product([-1, 0, 1], repeat=dim))))

def grid_neigbours(pos: Tuple[int, ...]) -> List[Tuple[int,...]]:
    '''Returns a list of neighbours for a given position in a n dim grid'''
    neigbours = [tuple(map(sum, zip(pos, i))) for i in iter_neigbours(len(pos))]
    neigbours.remove(pos) # remove self
    return  neigbours

def grid_ud_neigbours(pos: Tuple[int, ...]) -> List[Tuple[int,...]]:
    '''Returns a list of neighbours for a given position in a n dim grid'''
    neigbours = [tuple(map(sum, zip(pos, i))) for i in iter_ud_neigbours(len(pos))]
    return  neigbours

def transpose_grid(grid: List[List[Any]]) -> List[List[Any]]:
    '''Transposes a grid

    [[1, 2, 3], [4, 5, 6]]

    becomes
    
    [[1, 4],
    [2, 5],
    [3, 6]]
    '''
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

def rotate_grid_cw(grid: List[List[Any]]) -> List[List[Any]]:
    '''Rotates a grid 90 degrees clockwise'''
    return list(map(list,zip(*grid[::-1])))

def rotate_grid_ccw(grid: List[List[Any]]) -> List[List[Any]]:
    '''Rotates a grid 90 degrees counter clockwise'''
    return list(map(list,zip(*grid)))[::-1]