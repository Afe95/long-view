class History(object):

  def __init__(self):
    self.wonBets = []
    self.lostBets = []

  def addBets(self, portfolio):
    bets = portfolio.getStatObject().getPastBets()
    for b in bets:
      if b.isWin():
        self.wonBets.append(b)
      else:
        self.lostBets.append(b)