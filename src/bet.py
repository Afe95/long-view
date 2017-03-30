import bcolors

class Bet(object):

  def __init__(self, odds, match):
    self.odds = odds[0]
    self.expectedResult = odds[1]
    self.pWin = odds[2]
    self.match = match
    self.accountBefore = None
    self.accountAfter = None
    self.fraction = None

  def getPrior(self):
    return self.pWin

  def isWin(self):
    return self.match.getResult() == self.expectedResult

  def gain(self):
    return self.odds

  def updateBefore(self, before):
    self.accountBefore = before

  def updateAfter(self, after):
    self.accountAfter = after

  def updateFraction(self, fraction):
    self.fraction = fraction

  def getAccountAfter(self):
    return self.accountAfter

  def __str__(self):
    if self.expectedResult != self.match.getResult():
      return "\033[91m{0:<20}\t{1:<20}\t{2:>5}\t\t{3:>3}\t\t{4:.2f}\t{5:>6.2f}\t{6:>10.2f}\t{7:>10.2f}\033[0m".format(self.match.homeTeam, self.match.awayTeam, self.expectedResult, self.match.getResult(), self.odds, self.fraction, self.accountBefore, self.accountAfter)
    return "\033[92m{0:<20}\t{1:<20}\t\t\t\t\t{2:.2f}\t{3:>6.2f}\t{4:>10.2f}\t{5:>10.2f}\033[0m".format(self.match.homeTeam, self.match.awayTeam, self.odds, self.fraction, self.accountBefore, self.accountAfter)
    
  def __repr__(self):
    return self.__str__()