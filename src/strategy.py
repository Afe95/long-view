from abc import ABCMeta, abstractmethod

  class Strategy(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def toBet(self, match, *extraParams):
      raise NotImplementedError("Should implement toBet()")