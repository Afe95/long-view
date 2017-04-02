#!/usr/local/bin/python

from __future__ import division

import sys
import simulate
import src.history as h
import matplotlib.pyplot as plt

def runSimulation(season, league, startingBudget, detailedStats):
  return simulate.startSimulation(season, league, startingBudget, detailedStats)

if __name__ == "__main__":
  # seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]

  # seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  seasons = ["1314", "1415", "1516", "1617"]
  leagues = ["D1", "I1", "SP1", "F1", "N1", "P1", "G1"]
  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  season = None
  league = None
  detailedStats = True
  startingBudget = 100

  try:
    season = sys.argv[1]
  except IndexError:
    detailedStats = False

  try:
    league = sys.argv[2]
  except IndexError:
    detailedStats = False

  if league != None and season != None:
    print("\033[1m{0} {1}\n\033[0m".format(season, league))
    runSimulation(season, league, startingBudget, detailedStats)

  else:

    if league is not None:
      leagues = [league]
    if season is not None:
      seasons = [season]

    history = h.History()

    print("\033[1m{0}\n{1}\n\033[0m".format(seasons, leagues))

    for s in seasons:
      cumSum = 0

      for l in leagues:
        portfolio = runSimulation(s, l, startingBudget, detailedStats)

        print(portfolio)

        history.addBets(portfolio)
        cumSum += portfolio.getCapital()

      startBudget = len(leagues) * startingBudget
      ratio = round(((cumSum / startBudget) - 1) * startingBudget, 2)
      print("\033[1m\n\t\t\t\t\t\t\t {0:>6.2f}%\t{1:>10.2f}\033[0m".format(ratio, cumSum))

    history.createHistogramWins()
    history.createHistogramLosts()
    plt.show()