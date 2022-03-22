from aima.search import *
from gui import NQueensGUI

import time
import matplotlib.pyplot as plt


def perform(func, *args):
    return func(*args)

def run(algos, N, show=False):
    answers = []
    exe_times = []

    print('Execution times ({}):'.format(N))
    for algo in algos:
        start = time.time()
        answers.append(perform(algo, (NQueensProblem(N))).state)
        exe_time = float(time.time()-start)
        print('\t', algo.__name__, '\t\t', exe_time, sep='')
        exe_times.append(exe_time)

    if show:
        coords = []
        for answer in answers:
            coords.append([(answer[i], i) for i in range(len(answer))])
        for i in range(len(coords)):
            gui = NQueensGUI(coords[i], N)
    
    return exe_times

def sweep_N(N_start, N_end, algos, show=False):
    times = []
    for n in range(N_start, N_end+1):
        times.append([n, run(algos, n, show=show)])
    return times


# Measure execution time old way or make a wrapper function
N = 8

'''
algos = [
    depth_first_tree_search,
    breadth_first_graph_search,
    uniform_cost_search
]'''

algos = [depth_first_tree_search]

times = sweep_N(4, 16, algos, show=True)


    

print()

