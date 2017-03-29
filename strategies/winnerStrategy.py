import src.strategy as s
import src.table as t

class WinnerStrategy(s.Strategy):

  def __init__(self, database, season, league=None):
    self.db = database
    self.season = season
    self.league = league
    self.table = None
    self.getTable()

  def getTable(self):
    table = self.db.getTable(self.season, self.league)
    self.table = t.Table(table)

  def toBet(self, match):
    pass