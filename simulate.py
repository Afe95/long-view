#!/usr/local/bin/python

import sys
import src.database as db
import strategies.winnerStrategy as st

if __name__ == "__main__":
  # seasons = ["0001", "0102", "0203", "0304", "0405", "0506", "0607", "0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]

  seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  season = sys.argv[1]
  league = sys.argv[2]

  """
  Initialise strategy
  Initialise brokers

  While matches
    if to bet
      determine risk
      bet
      update portfolio

  print stats
  """

  database = db.Database("localhost", "long-view", "afe", "1bellazio")
  database.connect()

  table = database.getTable(season, league)
  strategy = st.WinnerStrategy()
