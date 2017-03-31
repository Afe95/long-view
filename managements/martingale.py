from __future__ import division

import src.stats as s
import src.portfolio as p

class Martingale(p.Portfolio):

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    super(Martingale, self).__init__(startingBudget, detailedStats, percentageToDeposit)
    self.prog = 10

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      gain = self.martingale(bet)
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

  def martingale(self, bet):
    fraction = self.prog    
    amountBet = min(fraction, self.account)
    if amountBet == self.account:
      return self.kelly(bet)
    bet.updateFraction(amountBet)
    self.account -= amountBet
    odds = bet.gain()
    gain = round(amountBet * odds, 2)
    if bet.isWin():
      self.martinGoDown()
    else:
      self.martinGoUp()
    return gain

  def martinGoUp(self):
    self.prog *= 2

  def martinGoDown(self):
    self.prog = 10