#!/usr/local/bin/python

import sys
import numpy as np
import simulate as s

if __name__ == "__main__":

  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  season = sys.argv[1]
  league = None
  fixedRisk = None
  percentile = None
  detailedStats = False

  comparison = []

  for i in np.arange(0,1,0.01):

    cumSum = 0

    for l in leagues:
      cumSum += s.startSimulation(season, l, detailedStats, percentageToDeposit=i)

    print "\033[1m\n\t\t\t\t       {0:>7}\033[0m".format(cumSum)

    comparison.append((round(i,2), round(cumSum,2)))

  print comparison