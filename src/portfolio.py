from __future__ import division
from abc import ABCMeta, abstractmethod

import math
import scipy.constants as constants
import src.stats as s

class Portfolio(object):

  __metaclass__ = ABCMeta

  def __init__(self, startingBudget, detailedStats, percentageToDeposit):
    self.deposit = 0
    self.percentageToDeposit = percentageToDeposit #0.67
    self.startingBudget = startingBudget
    self.account = startingBudget
    self.stat = s.Statistic(detailedStats)

  def riskAndBet(self, bet, revenue):
    if bet.isWin():
      amountToDeposit = revenue * self.percentageToDeposit
      self.deposit += amountToDeposit
      self.account += revenue - amountToDeposit
      bet.updateAfter(self.account)
      self.stat.win(bet)
    else:
      bet.updateAfter(self.account)
      self.stat.loose(bet)

  def noCashToBet(self, bet):
    bet.updateFraction(0)
    bet.updateAfter(self.account)
    self.stat.noCash(bet)

  @abstractmethod
  def calculate(self, bet):
    raise NotImplementedError("Should implement calculate()")

  def getCapital(self):
    return self.account + self.deposit

  def getStatObject(self):
    return self.stat

  def __str__(self):
    cumSum = self.account + self.deposit
    ratio = round(((cumSum / self.startingBudget) - 1) * self.startingBudget, 2)
    return "{0}\t{1:>7.2f}%\t{2:>10.2f}".format(self.stat, ratio, cumSum)

  def __repr__(self):
    return self.__str__()