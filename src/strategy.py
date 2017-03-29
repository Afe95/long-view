from abc import ABCMeta, abstractmethod

class Strategy(object):

  __metaclass__ = ABCMeta

  @abstractmethod
  def toBet(self, *extraParams):
    raise NotImplementedError("Should implement toBet()")