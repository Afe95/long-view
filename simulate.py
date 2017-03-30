import src.database as db
import src.timer as t
import src.portfolio as p
import strategies.winnerStrategy as st

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

def startSimulation(season, league):

  seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
  leagues = ["E0", "D1", "I1", "SP1", "F1", "N1", "P1", "G1"]

  database = db.Database("localhost", "long-view", "afe", "1bellazio")
  database.connect()

  seasonForStrategy = seasons[seasons.index(season) - 1]
  strategy = st.WinnerStrategy(database, seasonForStrategy, league)
  timer = t.Timer(database, season, league)
  portfolio = p.Portfolio(100, 0.56)

  while not timer.isEnded():
    nextMatch = timer.nextMatch()
    bet = strategy.toBet(nextMatch)
    if bet != None:
      portfolio.riskAndBet(bet)

  print portfolio
