class Result(object):

  def __init__(self, results):
    self.hthg = results[0]
    self.htag = results[1]
    self.htr = results[2]

    self.fthg = results[3]
    self.ftag = results[4]
    self.ftr = results[5]

  def resultHalfTime(self):
    return self.htr

  def resultFullTime(self):
    return self.ftr

  def halfTime(self):
    return (self.hthg, self.htag, self.htr)

  def fullTime(self):
    return (self.fthg, self.ftag, self.ftr)