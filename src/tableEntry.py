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

    self.probWin = None
    self.probDraw = None
    self.probLoose = None
    self.getProbabilities()

  def getLeague(self):
    return self.league

  def getPosition(self):
    return self.position

  def getClub(self):
    return self.club

  def pWin(self):
    return self.probWin

  def getProbabilities(self):
    self.probWin = 2 - (self.won / self.played)
    self.probWin = round(self.probWin + self.increment, 2)

    self.probDraw = 2 - (self.drawn / self.played)
    self.probDraw = round(self.probDraw + self.increment, 2)

    self.probLoose = 2 - (self.lost / self.played)
    self.probLoose = round(self.probLoose + self.increment, 2)