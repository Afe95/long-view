import src.tableEntry as te

class Table(object):

  def __init__(self, resultQuery):
    self.listOfPositions = []
    self.createEntries(resultQuery)

  def createEntries(self, resultQuery):

    for row in resultQuery:
      entry = te.TableEntry(row)
      self.listOfPositions.append(entry)

  def getNumber(self, num, league):
    for r in self.listOfPositions:
      if r.getPosition() == num and r.getLeague() == league:
        return r

  def getFirst(self, league):
    return self.getNumber(1, league)