from __future__ import division

import math
import scipy.constants as constants
import stats as s

class Portfolio(object):

  def __init__(self, startingBudget, fixedRisk=0.56, detailedStats=False, percentageToDeposit=0):
    self.deposit = 0
    self.index = 2
    self.percentageToDeposit = percentageToDeposit
    self.account = startingBudget
    self.stat = s.Statistic(detailedStats=detailedStats)

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      gain = self.calcFraction(bet, "kelly")
      if bet.isWin():
        amountToDeposit = gain * self.percentageToDeposit
        self.deposit += amountToDeposit
        self.account += gain - amountToDeposit
        bet.updateAfter(self.account)
        self.stat.win(bet)
      else:
        bet.updateAfter(self.account)
        self.stat.loose(bet)
    else:
      bet.updateAfter(self.account, 0)
      self.stat.noCash(bet)

  def calcFraction(self, bet, mode="kelly"):
    if mode is "kelly":
      return self.kelly(bet)

  def kelly(self, bet):
    b = bet.gain() - 1
    p = 2 - bet.getPrior()
    fraction = abs((b*p - (1-p)) / b)
    if fraction >= 0.45:
      fraction = fraction / 2
    bet.updateFraction(fraction)
    amountBet = round(self.account * fraction, 2)
    self.account -= amountBet    
    odds = bet.gain()
    gain = round(amountBet * odds, 2)
    amountToDeposit = gain * self.percentageToDeposit

    return gain

  def getCapital(self):
    return self.account + self.deposit

  def fibNumber(self, n):
    golden = constants.golden
    fib = (math.pow(golden, n) - math.pow(-golden,-n)) / math.sqrt(5)
    return fib

  def __str__(self):
    return "{0}\t{1:>6.2f}".format(self.stat, self.account + self.deposit)

  def __repr__(self):
    return self.__str__()