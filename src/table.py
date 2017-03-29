import tableEntry as te

class Table(object):

  def __init__(self, resultQuery):
    self.listOfPositions = []
    self.createEntries(resultQuery)

  def createEntries(self, resultQuery):

    for row in resultQuery:
      entry = te.TableEntry(row)
      self.listOfPositions.append(entry)

  def getNumber(self, num):
    return self.listOfPositions[num]

  def getFirst(self):
    return self.getNumber(1)

  def getLast(self):
    return self.getNumber(-1)