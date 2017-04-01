from __future__ import division

import src.stats as s
import src.portfolio as p
import managements.kelly as k

class Martingale(p.Portfolio):

  def __init__(self, startingBudget, detailedStats, percentageToDeposit=0.67):
    super(Martingale, self).__init__(startingBudget, detailedStats, percentageToDeposit)
    self.kelly = k.Kelly(startingBudget, detailedStats, percentageToDeposit)
    self.prog = 10

  def calculate(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      fraction = self.prog    
      amountBet = fraction * 0.01 * self.account #min(fraction, self.account)
      if amountBet == self.account:
        return self.kelly.calculate(bet)
      bet.updateFraction(amountBet)
      self.account -= amountBet
      odds = bet.gain()
      gain = round(amountBet * odds, 2)
      if bet.isWin():
        self.martinGoDown()
      else:
        self.martinGoUp()
      super(Martingale, self).riskAndBet(bet, gain)
    else:
      super(Martingale, self).noCashToBet(bet)

  def martinGoUp(self):
    self.prog *= 2

  def martinGoDown(self):
    self.prog = 10