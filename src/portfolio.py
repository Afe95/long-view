from __future__ import division

import stats as s

class Portfolio(object):

  def __init__(self, startingBudget, fixedRisk=0.56, percentile=3):
    self.account = startingBudget
    self.fixedRisk = fixedRisk
    self.percentile = 3
    self.stat = s.Statistic()

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      fraction = self.calcFraction(bet)
      amountBet = round(self.account * fraction, 2)
      self.account -= amountBet
      if bet.isWin():
        odds = bet.gain()
        self.account += round(amountBet * odds, 2)
        bet.updateAfter(self.account, fraction)
        self.stat.win(bet)
      else:
        bet.updateAfter(self.account, fraction)
        self.stat.loose(bet)
    else:
      bet.updateAfter(self.account, 0)
      self.stat.noCash(bet)

  def calcFraction(self, bet, useFixedRisk=False):
    if not useFixedRisk:
      b = bet.gain() - 1
      p = 2 - bet.getPrior()
      fraction = abs((b*p - (1-p)) / b)
      if fraction >= 0.45:
        return fraction / 2
      return fraction
    return self.fixedRisk

  def __str__(self):
    return "{0}\t{1:.2f}".format(self.stat, self.account)

  def __repr__(self):
    return self.__str__()