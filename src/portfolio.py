from __future__ import division
from abc import ABCMeta, abstractmethod

import math
import scipy.constants as constants
import stats as s

class Portfolio(object):

  __metaclass__ = ABCMeta

  def __init__(self, startingBudget, detailedStats=False, percentageToDeposit=0.67):
    self.deposit = 0
    self.percentageToDeposit = percentageToDeposit #0.67
    self.account = startingBudget
    self.stat = s.Statistic(detailedStats=detailedStats)

  @abstractmethod
  def riskAndBet(self, bet):
    raise NotImplementedError("Should implement riskAndBet()")

  def getCapital(self):
    return self.account + self.deposit

  def __str__(self):
    return "{0}\t{1:>10.2f}".format(self.stat, self.account + self.deposit)

  def __repr__(self):
    return self.__str__()