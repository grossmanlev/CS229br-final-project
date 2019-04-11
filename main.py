"""
Simulation of Offspring Sex Ratio Evolution

Lev Grossman, Anirudh Suresh
CS229br -- Biology and Complexity
"""

import numpy as np

from simulators import *

"""
TODOs:
1) Code up the simple model found in Wild and West (great author names)
    a) Birth
    b) Maternal Investment
    c) Dispersal
    d) Male-Male Competition
    e) Female-Female Competition
2) Extend, alter the model
    a) Harem-based model -- where a selected male each round mates with all
       females.  Or, variants where selected male for each breeding "patch"
"""


def main():
    sim = WildWestSimulator()
    sim.birth()


if __name__ == '__main__':
    main()
