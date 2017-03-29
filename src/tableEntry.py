from __future__ import division

class TableEntry(object):

  def __init__(self, row):
    # league, position, club, played, won, drawn, lost
    self.league = row[0]
    self.position = row[1]
    self.club = row[2]
    self.played = row[3]
    self.won = row[4]
    self.drawn = row[5]
    self.lost = row[6]

    self.increment = 0.01

    self.pWin = None
    self.pDraw = None
    self.pLoose = None
    self.getProbabilities()

  def getProbabilities(self):
    self.pWin = 1 - (self.won / self.played)
    self.pWin = round(self.pWin + self.increment, 2)

    self.pDraw = 1 - (self.drawn / self.played)
    self.pDraw = round(self.pDraw + self.increment, 2)

    self.pLoose = 1 - (self.lost / self.played)
    self.pLoose = round(self.pLoose + self.increment, 2)