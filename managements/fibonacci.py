from __future__ import division

import math
import scipy.constants as constants
import src.stats as s
import src.portfolio as p

class Fibonacci(p.Portfolio):

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    super(Fibonacci, self).__init__(startingBudget, detailedStats, percentageToDeposit)
    self.index = 2

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      gain = self.fibonacci(bet)
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

  def fibonacci(self, bet):
    fraction = self.fibNumber(self.index)    
    amountBet = min(fraction * 5, self.account)
    if amountBet == self.account:
      return self.kelly(bet)
    bet.updateFraction(amountBet)
    self.account -= amountBet
    odds = bet.gain()
    gain = round(amountBet * odds, 2)
    if bet.isWin():
      self.fibGoDown()
    else:
      self.fibGoUp()
    return gain

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