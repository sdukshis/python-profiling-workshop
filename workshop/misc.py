import numpy as np


def print_stats(a: np.array) -> None:
    print(f"{'Min:':<10} {np.min(a):10.0f}")
    print(f"{'10-perc:':<10} {np.percentile(a, q=10):10.0f}")
    print(f"{'25-perc:':<10} {np.percentile(a, q=25):10.0f}")
    print(f"{'Median:':<10} {np.median(a):10.0f}")
    print(f"{'Mean:':<10} {np.mean(a):10.0f}")
    print(f"{'75-perc:':<10} {np.percentile(a, q=75):10.0f}")
    print(f"{'90-perc:':<10} {np.percentile(a, q=90):10.0f}")
    print(f"{'Max:':<10} {np.max(a):10.0f}")

