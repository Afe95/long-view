from __future__ import division

import math
import scipy.constants as constants
import stats as s

class Portfolio(object):

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    self.deposit = 0
    self.index = 2
    self.percentageToDeposit = percentageToDeposit #0.67
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
      bet.updateFraction(0)
      bet.updateAfter(self.account)
      self.stat.noCash(bet)

  def calcFraction(self, bet, mode="kelly"):
    if mode is "kelly":
      return self.kelly(bet)
    elif mode is "fibonacci":
      return self.fibonacci(bet)

  def fibonacci(self, bet):
    fraction = self.fibNumber(self.index)
    bet.updateFraction(fraction)
    amountBet = min(fraction * 5, self.account)
    self.account -= amountBet
    odds = bet.gain()
    gain = round(amountBet * odds, 2)
    if bet.isWin():
      self.fibGoDown()
    else:
      self.fibGoUp()
    return gain

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
    return gain

  def getCapital(self):
    return self.account + self.deposit

  def fibGoUp(self):
    if self.index != 9:
      self.index += 1
    else:
      self.index = 2

  def fibGoDown(self):
    if self.index >= 4:
      self.index -= 2
    if self.index == 3:
      self.index = 2

  def fibNumber(self, n):
    golden = constants.golden
    fib = (math.pow(golden, n) - math.pow(-golden,-n)) / math.sqrt(5)
    return int(fib)

  def __str__(self):
    return "{0}\t{1:>10.2f}".format(self.stat, self.account + self.deposit)

  def __repr__(self):
    return self.__str__()