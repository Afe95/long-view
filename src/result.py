class Result(object):

  def __init__(self,
                fthg, ftag, ftr,
                hthg, htag, htr):
    self.halfTime = (hthg, htag, htr)
    self.fullTime = (fthg, ftag, ftr)

  def resultHalfTime(self):
    pass

  def resultFullTime(self):
    pass