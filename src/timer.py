import src.match as match

class Timer(object):

  def __init__(self, database, season, league=None):
    self.db = database
    self.season = season
    self.league = league
    self.listOfMatches = []
    self.timeIndex = 0
    self.getMatches()

  def getMatches(self):
    matches = self.db.getMatches(self.season, self.league)
    for m in matches:
      tmpMatch = match.Match(m)
      self.listOfMatches.append(tmpMatch)

  def isEnded(self):
    return self.timeIndex == len(self.listOfMatches)

  def nextMatch(self):
    if self.timeIndex != len(self.listOfMatches):
      self.timeIndex += 1
      return self.listOfMatches[self.timeIndex - 1]
    return None