import result as r
import odd as o

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