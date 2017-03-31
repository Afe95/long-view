from __future__ import division

import src.stats as s
import src.portfolio as p

class Kelly(p.Portfolio):

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    super(Kelly, self).__init__(startingBudget, detailedStats, percentageToDeposit)

  def calculate(self, bet):
    bet.updateBefore(self.account)
    if self.account > 0:
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
      super(Kelly, self).riskAndBet(bet, gain)
    else:
      super(Kelly, self).noCashToBet(bet)