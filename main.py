#!/usr/local/bin/python

import sys
import simulate as s

if __name__ == "__main__":
  # seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]

  seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  leagues = ["D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  season = sys.argv[1]
  league = None
  detailedStats = True

  try:
    league = sys.argv[2]
  except IndexError:
    detailedStats = False

  if league != None:
    s.startSimulation(season, league, detailedStats)
  else:
    cumSum = 0

    for l in leagues:
      cumSum += s.startSimulation(season, l, detailedStats)

    print "\033[1m\n\t\t\t\t\t\t        {0:>10.2f}\033[0m".format(cumSum)