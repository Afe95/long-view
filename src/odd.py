class Odd(object):

  def __init__(self,
                b365h, b365d, b365a,
                bsh, bsd, bsa,
                bwh, bwd, bwa,
                gbh, gbd, gba,
                iwh, iwd, iwa,
                lbh, lbd, lba,
                psh, psd, psa,
                soh, sod, soa,
                sbh, sbd, sba,
                sjh, sjd, sja,
                syh, syd, sya,
                vch, vcd, vca,
                whh, whd, wha):
    self.b365 = (b365h, b365d, b365a)
    self.bs = (bsh, bsd, bsa)
    self.bw = (bwh, bwd, bwa)
    self.gb = (gbh, gbd, gba)
    self.iw = (iwh, iwd, iwa)
    self.lb = (lbh, lbd, lba)
    self.ps = (psh, psd, psa)
    self.so = (soh, sod, soa)
    self.sb = (sbh, sbd, sba)
    self.sj = (sjh, sjd, sja)
    self.sy = (syh, syd, sya)
    self.vc = (vch, vcd, vca)
    self.wh = (whh, whd, wha)

  def bestHome(self):
    pass

  def bestDraw(self):
    pass

  def bestAway(self):
    pass
