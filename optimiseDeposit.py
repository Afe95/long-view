#!/usr/local/bin/python

import sys
import numpy as np
import simulate
import matplotlib.pyplot as plt

def runSimulation(season, league, startingBudget, detailedStats, threshold):
  return simulate.startSimulation(season, league, startingBudget, detailedStats, threshold)

if __name__ == "__main__":

  seasons = ["1415", "1617"]
  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  league = None
  fixedRisk = None
  percentile = None
  detailedStats = False
  startingBudget = 100
  comparison = []

  for i in np.arange(1.5,7,0.1):

    totalSum = 0

    for s in seasons:
      cumSum = 0

      for l in leagues:
        portfolio = runSimulation(s, l, startingBudget, detailedStats, i)

        print(portfolio)

        cumSum += portfolio.getCapital()

      totalSum += cumSum

      startBudget = len(leagues) * startingBudget
      ratio = round(((cumSum / startBudget) - 1) * startingBudget, 2)
      print("\033[1m\n\t\t\t\t\t\t\t {0:>6.2f}%\t{1:>10.2f}\033[0m".format(ratio, cumSum))

    comparison.append((round(i,2), round(totalSum,2)))

  print(comparison)