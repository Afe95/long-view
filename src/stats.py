class Statistic(object):

  def __init__(self, detailedStats=False):
    self.numBets = 0
    self.numWins = 0
    self.numLoss = 0
    self.pastBets = []
    self.detailedStats = detailedStats

  def win(self, bet):
    self.numBets += 1
    self.numWins += 1
    self.pastBets.append(bet)

  def loose(self, bet):
    self.numBets += 1
    self.numLoss += 1
    self.pastBets.append(bet)

  def noCash(self, bet):
    self.numBets += 1
    self.pastBets.append(bet)

  def __str__(self):
    strToPrint = ""

    if self.detailedStats:
      strToPrint += "\033[1m=============================================================================================================================\n"
      strToPrint += "Home Team\t\tAway Team\t\tExpected\tActual\t\tOdds\tFraction    Before\t     After\n"
      strToPrint += "=============================================================================================================================\n\033[0m"
      for b in self.pastBets:
        strToPrint += "{0}\n".format(b)
      strToPrint += "\n"

    strToPrint += "numBets={0:<2}\twins={1:<2}\tlosts={2:<2}".format(self.numBets, self.numWins, self.numLoss)

    return strToPrint

  def __repr__(self):
    return self.__str__()