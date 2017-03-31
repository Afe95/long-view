import src.result as r
import src.odd as o

class Match(object):

  def __init__(self, row):
    """
    league, date, home, away, fthg, ftag, ftr, hthg, htag, htr, (b365h, b365d, b365a, bsh, bsd, bsa, bwh, bwd, bwa, gbh, gbd, gba, iwh, iwd, iwa, lbh, lbd, lba, psh, psd, psa, soh, sod, soa, sbh, sbd, sba, sjh, sjd, sja, syh, syd, sya, vch, vcd, vca, whh, whd, wha)
    """
    self.league = row[0]
    self.data = row[1]
    self.homeTeam = row[2]
    self.awayTeam = row[3]
    self.result = r.Result(row[4:10])
    self.odds = o.Odd(row[10:])

  def getOdds(self):
    return self.odds

  def getHomeTeam(self):
    return self.homeTeam

  def getAwayTeam(self):
    return self.awayTeam

  def teamsPlaying(self):
    return (self.homeTeam, self.awayTeam)

  def getLeague(self):
    return self.league

  def getResult(self):
    return self.result.resultFullTime()

  def __str__(self):
    return "{0}\t{1}\t{2:<15}\t{3:<15}\t\t{4}\t{5}".format(self.league, self.data, self.homeTeam, self.awayTeam, self.result.resultFullTime(), self.odds.best())

  def __repr__(self):
    return self.__str__()