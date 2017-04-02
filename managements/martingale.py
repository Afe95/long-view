from __future__ import division

import src.stats as s
import src.portfolio as p
import managements.kelly as k

class Martingale(p.Portfolio):

  def __init__(self, startingBudget, detailedStats, percentageToDeposit=0.67):
    super(Martingale, self).__init__(startingBudget, detailedStats, percentageToDeposit)
    self.kelly = k.Kelly(startingBudget, detailedStats, percentageToDeposit)
    self.losses = 0
    self.fixedWin = 4

  def calculate(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      odds = bet.getOdds()
      amountBet = (self.losses + self.fixedWin) / (odds - 1)
      if amountBet == self.account:
        return self.kelly.calculate(bet)
      bet.updateFraction(amountBet)
      self.account -= amountBet
      gain = round(amountBet * odds, 2)
      if bet.isWin():
        self.martinGoDown()
      else:
        self.martinGoUp(amountBet)
      super(Martingale, self).riskAndBet(bet, gain)
    else:
      super(Martingale, self).noCashToBet(bet)

  def martinGoUp(self, lost):
    self.losses += lost

  def martinGoDown(self):
    self.losses = 0