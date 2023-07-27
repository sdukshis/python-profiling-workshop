import time
import argparse

import numpy as np

from game_of_chance import play_game
from workshop.misc import print_stats

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-n", "--num_iterations", type=int, default=1000000, help="Number of iterations to measure")
    args = argparser.parse_args()

    durations = np.zeros(args.num_iterations, dtype=np.int64)

    for i in range(len(durations)):
        start = time.perf_counter_ns()
        play_game()
        end = time.perf_counter_ns()
        durations[i] = end - start

    print(f"Duration statistics (ns)")
    print_stats(durations)

if __name__ == "__main__":
    main()
