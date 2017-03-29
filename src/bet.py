class Bet(object):

  def __init__(self, odds, match):
    self.odds = odds[0]
    self.expectedResult = odds[1]
    self.result = match.getResult()

  def isWin(self):
    return self.result == self.expectedResult

  def gain(self):
    return self.odds