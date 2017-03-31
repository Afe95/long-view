from __future__ import division

import src.stats as s
import src.portfolio as p

class Kelly(p.Portfolio):

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    super(Kelly, self).__init__(startingBudget, detailedStats, percentageToDeposit)

  def riskAndBet(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
      gain = self.kelly(bet)
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