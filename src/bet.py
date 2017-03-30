class Bet(object):

  def __init__(self, odds, match):
    self.odds = odds[0]
    self.expectedResult = odds[1]
    self.match = match
    self.accountBefore = None
    self.accountAfter = None

  def isWin(self):
    return self.match.getResult() == self.expectedResult

  def gain(self):
    return self.odds

  def updateBefore(self, before):
    self.accountBefore = before

  def updateAfter(self, after):
    self.accountAfter = after

  def __str__(self):
    if self.expectedResult != self.match.getResult():
      return "{0:<20}\t{1:<20}\t\t{2}\t{3}\t\t{4}\t{5}".format(self.match.homeTeam, self.match.awayTeam, self.expectedResult, self.match.getResult(), self.accountBefore, self.accountAfter)
    return "{0:<20}\t{1:<20}\t\t\t\t\t{2}\t{3}".format(self.match.homeTeam, self.match.awayTeam, self.accountBefore, self.accountAfter)
    
  def __repr__(self):
    return self.__str__()