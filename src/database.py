import psycopg2 as pg

class Database(object):

  def __init__(self, host, database, user, password):
    self.host = host
    self.database = database
    self.user = user
    self.password = password
    self.conn = None
    self.cur = None
    self.connect()

  def connect(self):
    self.conn = pg.connect(database=self.database, user=self.user, password=self.password, host=self.host)
    self.cur = self.conn.cursor()

  def disconnect(self):
    self.cur.close()
    self.conn.close()

  def getTable(self, season, league=None):
    """
    league, position, club, played, won, drawn, lost
    """
    query = ""

    if league is None:
      query = "SELECT l.abbreviation, s.position, c.full_name, s.played, s.won, s.drawn, s.lost FROM standings s, leagues l, seasons p, clubs c WHERE s.league_id = l.id AND s.season_id = p.id AND s.club_id = c.id AND p.period='{0}' ORDER BY s.position ASC;".format(season)
    else:
      query = "SELECT l.abbreviation, s.position, c.full_name, s.played, s.won, s.drawn, s.lost FROM standings s, leagues l, seasons p, clubs c WHERE s.league_id = l.id AND s.season_id = p.id AND s.club_id = c.id AND p.period='{0}' AND l.abbreviation='{1}' ORDER BY s.position ASC;".format(season, league)

    self.cur.execute(query)
    return self.cur.fetchall()

  def getMatches(self, season, league=None):
    """
    league, date, home, away, fthg, ftag, ftr, hthg, htag, htr, b365h, b365d, b365a, bsh, bsd, bsa, bwh, bwd, bwa, gbh, gbd, gba, iwh, iwd, iwa, lbh, lbd, lba, psh, psd, psa, soh, sod, soa, sbh, sbd, sba, sjh, sjd, sja, syh, syd, sya, vch, vcd, vca, whh, whd, wha
    """
    query = ""

    if league is None:
      query = "SELECT l.abbreviation, m.date, h.full_name, a.full_name, m.fthg, m.ftag, m.ftr, m.hthg, m.htag, m.htr, m.b365h, m.b365d, m.b365a, m.bsh, m.bsd, m.bsa, m.bwh, m.bwd, m.bwa, m.gbh, m.gbd, m.gba, m.iwh, m.iwd, m.iwa, m.lbh, m.lbd, m.lba, m.psh, m.psd, m.psa, m.soh, m.sod, m.soa, m.sbh, m.sbd, m.sba, m.sjh, m.sjd, m.sja, m.syh, m.syd, m.sya, m.vch, m.vcd, m.vca, m.whh, m.whd, m.wha FROM matches m, leagues l, seasons s, clubs h, clubs a WHERE m.league_id = l.id AND m.season_id = s.id AND m.home_id = h.id AND m.away_id = a.id AND s.period='{0}' ORDER BY m.date ASC;".format(season)
    else:
      query = "SELECT l.abbreviation, m.date, h.full_name, a.full_name, m.fthg, m.ftag, m.ftr, m.hthg, m.htag, m.htr, m.b365h, m.b365d, m.b365a, m.bsh, m.bsd, m.bsa, m.bwh, m.bwd, m.bwa, m.gbh, m.gbd, m.gba, m.iwh, m.iwd, m.iwa, m.lbh, m.lbd, m.lba, m.psh, m.psd, m.psa, m.soh, m.sod, m.soa, m.sbh, m.sbd, m.sba, m.sjh, m.sjd, m.sja, m.syh, m.syd, m.sya, m.vch, m.vcd, m.vca, m.whh, m.whd, m.wha FROM matches m, leagues l, seasons s, clubs h, clubs a WHERE m.league_id = l.id AND m.season_id = s.id AND m.home_id = h.id AND m.away_id = a.id AND s.period='{0}' AND l.abbreviation='{1}' ORDER BY m.date ASC;".format(season, league)

    self.cur.execute(query)
    return self.cur.fetchall()