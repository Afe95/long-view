class Simulation(object):

  def __init__(self, startingBudget, detailedStats):
    self.seasons = ["0910", "1011", "1112", "1213", "1314", "1415", "1516", "1617"]
    self.startingBudget = startingBudget
    self.detailedStats = detailedStats
    self.database = db.Database("localhost", "long-view", "afe", "1bellazio")
    self.season = None
    self.league = None
    self.deposit = None
    self.depth = None     

  def setSeason(self, season):
    self.season = season
    self.deposit = int(self.season[-1])%2

  def setDepth(self, depth):
    self.depth = depth

  def setLeague(self, league):
    self.league = league

  def start(self):
    seasonForStrategy = self.seasons[self.seasons.index(self.season) - 1]
    strategy = st.WinnerStrategy(self.database, seasonForStrategy, self.league, self.depth)
    timer = t.Timer(self.database, self.season, self.league)
    portfolio = k.Kelly(self.startingBudget, self.detailedStats, self.deposit)

    while not timer.isEnded():
      nextMatch = timer.nextMatch()
      bet = strategy.toBet(nextMatch)
      if bet != None:
        portfolio.calculate(bet)

    print(portfolio)

    return portfolio.getCapital()
