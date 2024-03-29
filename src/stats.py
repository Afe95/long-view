import numpy as np
import src.history as s

class Statistic(object):

  def __init__(self, detailedStats):
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

  def getPastBets(self):
    return self.pastBets

  def __str__(self):
    strToPrint = ""

    if self.detailedStats:
      strToPrint += "\033[1m===========================================================================================================================\n"
      strToPrint += "Home Team\t\tAway Team\t\tExpected\tActual\t\tOdds\tFraction    Before\t     After\n"
      strToPrint += "===========================================================================================================================\n\033[0m"
      for b in self.pastBets:
        strToPrint += "{0}\n".format(b)
      strToPrint += "\n"

    xs = []
    xs.append(100)
    for b in self.pastBets:
      xs.append(b.getAccountAfter())

    try:
      i = np.argmax(np.maximum.accumulate(xs) - xs)
      j = np.argmax(xs[:i])
      maxDD = round(xs[j] - xs[i], 2)
    except ValueError:
      maxDD = "None"

    strToPrint += "numBets={0:<2}\twins={1:<2}\tlosts={2:<2}\tmaxDD={3:<5}".format(self.numBets, self.numWins, self.numLoss, maxDD)

    return strToPrint

  def __repr__(self):
    return self.__str__()