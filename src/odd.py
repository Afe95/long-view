class Odd(object):

  def __init__(self, odds):
    self.b365 = (odds[0], odds[1], odds[2])
    self.bs = (odds[3], odds[4], odds[5])
    self.bw = (odds[6], odds[7], odds[8])
    self.gb = (odds[9], odds[10], odds[11])
    self.iw = (odds[12], odds[13], odds[14])
    self.lb = (odds[15], odds[16], odds[17])
    self.ps = (odds[18], odds[19], odds[20])
    self.so = (odds[21], odds[22], odds[23])
    self.sb = (odds[24], odds[25], odds[26])
    self.sj = (odds[27], odds[28], odds[29])
    self.sy = (odds[30], odds[31], odds[32])
    self.vc = (odds[33], odds[34], odds[35])
    self.wh = (odds[36], odds[37], odds[38])

    self.bHome = None
    self.bDraw = None
    self.bAway = None

    self.calcHome()
    self.calcDraw()
    self.calcAway()

  def calcHome(self):
    listOfOdds = [self.b365[0], self.bs[0], self.bw[0], self.gb[0], self.iw[0], self.lb[0], self.ps[0], self.so[0], self.sb[0], self.sj[0], self.sy[0], self.vc[0], self.wh[0]]
    try:
        tmpMax = max(filter(lambda x: x is not None, listOfOdds))
    except ValueError:
        tmpMax = 0
    self.bHome = tmpMax

  def calcDraw(self):
    listOfOdds = [self.b365[1], self.bs[1], self.bw[1], self.gb[1], self.iw[1], self.lb[1], self.ps[1], self.so[1], self.sb[1], self.sj[1], self.sy[1], self.vc[1], self.wh[1]]
    try:
        tmpMax = max(filter(lambda x: x is not None, listOfOdds))
    except ValueError:
        tmpMax = 0
    self.bDraw = tmpMax

  def calcAway(self):
    listOfOdds = [self.b365[2], self.bs[2], self.bw[2], self.gb[2], self.iw[2], self.lb[2], self.ps[2], self.so[2], self.sb[2], self.sj[2], self.sy[2], self.vc[2], self.wh[2]]
    try:
        tmpMax = max(filter(lambda x: x is not None, listOfOdds))
    except ValueError:
        tmpMax = 0
    self.bAway = tmpMax

  def bestHome(self):
    return self.bHome

  def bestDraw(self):
    return self.bDraw

  def bestAway(self):
    return self.bAway

  def best(self):
    return (self.bHome, self.bDraw, self.bAway)