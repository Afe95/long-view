from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

class History(object):

  def __init__(self):
    self.wonBets = []
    self.lostBets = []

  def addBets(self, portfolio):
    bets = portfolio.getStatObject().getPastBets()
    for b in bets:
      if b.isWin():
        self.wonBets.append(b)
      else:
        self.lostBets.append(b)

  def createHistogramWins(self):
    freq = {}
    historyOfOdds = []

    for b in self.wonBets:
      historyOfOdds.append(round(b.getOdds(),2))
      odds = int(round(b.getOdds(),2) * 100)

      if odds in freq:
        freq[odds] += 1
      else:
        freq[odds] = 1

    avg = round(np.mean(historyOfOdds), 2)
    sdev = round(np.std(historyOfOdds), 3)
    print("Wins  avg={0}\tst.dev={1}".format(avg, sdev))
    width = 4.0
    plt.bar(list(freq.keys()), freq.values(), width)
    plt.draw()

  def createHistogramLosts(self):
    freq = {}
    historyOfOdds = []

    for b in self.lostBets:
      historyOfOdds.append(round(b.getOdds(),2))
      odds = int(round(b.getOdds(),2) * 100)

      if odds in freq:
        freq[odds] += 1
      else:
        freq[odds] = 1

    avg = round(np.mean(historyOfOdds), 2)
    sdev = round(np.std(historyOfOdds), 3)
    print("Losts avg={0}\tst.dev={1}".format(avg, sdev))
    width = 4.0
    plt.bar(list(freq.keys()), freq.values(), width)
    plt.draw()

  def normalise(self, array):
    avg = np.mean(array)
    sdev = np.std(array)

    arrayNormalised = []

    for n in array:
      val = (n-avg)/sdev
      arrayNormalised.append(val)

    return arrayNormalised