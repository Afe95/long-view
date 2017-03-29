#!/usr/local/bin/python

import sys
import simulate as s

if __name__ == "__main__":
  # seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]

  seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  season = sys.argv[1]
  league = None

  try:
    league = sys.argv[2]
  except IndexError:
    pass

  if league != None:
    s.startSimulation(season, league)
  else:
    for l in leagues:
      s.startSimulation(season, l)