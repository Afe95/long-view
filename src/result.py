class Result(object):

  def __init__(self, results):
    """
    fthg, ftag, ftr, hthg, htag, htr
    """
    self.hthg = results[3]
    self.htag = results[4]
    self.htr = results[5]

    self.fthg = results[0]
    self.ftag = results[1]
    self.ftr = results[2]

  def resultHalfTime(self):
    return self.htr

  def resultFullTime(self):
    return self.ftr

  def halfTime(self):
    return (self.hthg, self.htag, self.htr)

  def fullTime(self):
    return (self.fthg, self.ftag, self.ftr)