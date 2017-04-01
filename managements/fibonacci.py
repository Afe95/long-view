from __future__ import division

import math
import scipy.constants as constants
import src.stats as s
import src.portfolio as p
import managements.kelly as k

class Fibonacci(p.Portfolio):

  def __init__(self, startingBudget, detailedStats, percentageToDeposit=0.67):
    super(Fibonacci, self).__init__(startingBudget, detailedStats, percentageToDeposit)
    self.kelly = k.Kelly(startingBudget, detailedStats, percentageToDeposit)
    self.index = 2

  def calculate(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      fraction = self.fibNumber(self.index)    
      amountBet = fraction * 0.01 * 5 * self.account #min(fraction * 5, self.account)
      if amountBet == self.account:
        return self.kelly.calculate(bet)
      bet.updateFraction(amountBet)
      self.account -= amountBet
      odds = bet.gain()
      gain = round(amountBet * odds, 2)
      if bet.isWin():
        self.fibGoDown()
      else:
        self.fibGoUp()
      super(Fibonacci, self).riskAndBet(bet, gain)
    else:
      super(Fibonacci, self).noCashToBet(bet)

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