class Statistic(object):

  def __init__(self):
    self.numBets = 0
    self.numWins = 0
    self.numLoss = 0
    self.pastBets = []

  def win(self, bet):
    self.numBets += 1
    self.numWins += 1
    self.pastBets.append(bet)

  def loose(self, bet):
    self.numBets += 1
    self.numLoss += 1
    self.pastBets.append(bet)

  def __str__(self):
    strToPrint = ""

    for b in self.pastBets:
      strToPrint += "{0}\n".format(b)

    strToPrint += "\nnumBets={0}\twins={1}\tlosts={2}".format(self.numBets, self.numWins, self.numLoss)

    return strToPrint

  def __repr__(self):
    return self.__str__()