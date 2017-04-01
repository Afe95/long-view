import src.strategy as s
import src.table as t
import src.bet as b

class WinnerStrategy(s.Strategy):

  def __init__(self, database, season, league=None, depth=1):
    self.db = database
    self.season = season
    self.league = league
    self.depth = depth + 1
    self.table = None
    self.getTable()

  def getTable(self):
    table = self.db.getTable(self.season, self.league)
    self.table = t.Table(table)

  def toBet(self, match):
    odds = self.isInFavour(match)
    if odds != None:
      return b.Bet(odds, match)
    return None

  def isInFavour(self, match):

    homeTeam = match.getHomeTeam()
    awayTeam = match.getAwayTeam()
    odds = match.getOdds()
    league = match.getLeague()

    for i in range(i, self.depth):
      clubPreviousSeason = self.table.getNumber(i, league)

      clubName = clubPreviousSeason.getClub()
      clubPWin = clubPreviousSeason.pWin()

      if clubName == homeTeam:
        oddsH = odds.bestHome()
        if oddsH > clubPWin:
          return (oddsH, 'H', clubPWin)

      elif clubName == awayTeam:
        oddsA = odds.bestAway()
        if oddsA > clubPWin:
          return (oddsA, 'A', clubPWin)

    return None