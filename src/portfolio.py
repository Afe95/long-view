import stats as s

class Portfolio(object):

  def __init__(self, startingBudget, fixedRisk):
    self.account = startingBudget
    self.fixedRisk = fixedRisk
    self.stat = s.Statistic()

  def riskAndBet(self, bet):
    if self.account > 0:
      amountBet = round(self.account * self.fixedRisk, 2)
      self.account -= amountBet
      if bet.isWin():
        odds = bet.gain()
        self.account += round(amountBet * odds, 2)
        self.stat.win()
      else:
        self.stat.loose()

  def __str__(self):
    return "{0}\t\t{1}".format(self.account, self.stat)

  def __repr__(self):
    return self.__str__()