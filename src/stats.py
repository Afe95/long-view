class Statistic(object):

  def __init__(self):
    self.numBets = 0
    self.numWins = 0
    self.numLoss = 0

  def win(self):
    self.numBets += 1
    self.numWins += 1

  def loose(self):
    self.numBets += 1
    self.numLoss += 1

  def __str__(self):
    return "numBets={0}\twins={1}\tlosts={2}".format(self.numBets, self.numWins, self.numLoss)

  def __repr__(self):
    return self.__str__()