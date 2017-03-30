import stats as s

class Portfolio(object):

  def __init__(self, startingBudget, fixedRisk):
    self.account = startingBudget
    self.fixedRisk = fixedRisk
    self.stat = s.Statistic()

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      amountBet = round(self.account * self.fixedRisk, 2)
      self.account -= amountBet
      if bet.isWin():
        odds = bet.gain()
        self.account += round(amountBet * odds, 2)
        bet.updateAfter(self.account)
        self.stat.win(bet)
      else:
        bet.updateAfter(self.account)
        self.stat.loose(bet)

  def __str__(self):
    return "{0}\t{1:.2f}".format(self.stat, self.account)

  def __repr__(self):
    return self.__str__()