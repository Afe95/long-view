import src.strategy as s
import src.table as t
import src.bet as b

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
    league = match.getLeague()
    firstPreviousSeason = self.table.getNumber(1, league)
    secondPreviousSeason = self.table.getNumber(2, league)
    odds = self.isInFavour(match, firstPreviousSeason, secondPreviousSeason)
    if odds != None:
      return b.Bet(odds, match)
    return None

  def isInFavour(self, match, rowFirst, rowSecond):
    firstTeam = rowFirst.getClub()
    secondTeam = rowSecond.getClub()

    pWinFirst = rowFirst.pWin()
    pWinSecond = rowSecond.pWin()

    homeTeam = match.getHomeTeam()
    awayTeam = match.getAwayTeam()
    odds = match.getOdds()

    if firstTeam == homeTeam:
      odds = odds.bestHome()
      if odds > pWinFirst:
        return (odds, 'H', pWinFirst)

    elif firstTeam == awayTeam:
      odds = odds.bestAway()
      if odds > pWinFirst:
        return (odds, 'A', pWinFirst)

    elif secondTeam == homeTeam:
      odds = odds.bestHome()
      if odds > pWinSecond:
        return (odds, 'H', pWinSecond)

    elif secondTeam == awayTeam:
      odds = odds.bestAway()
      if odds > pWinSecond:
        return (odds, 'A', pWinSecond)

    return None