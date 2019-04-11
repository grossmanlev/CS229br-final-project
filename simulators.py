import numpy as np
from abc import ABCMeta, abstractmethod


class Simulator(object):
    """ Abstract Class for Simulator """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Simulator, self).__init__()

    @abstractmethod
    def birth(self):
        pass

    @abstractmethod
    def breed(self):
        pass


class WildWestSimulator(Simulator):
    """ Wild and West Simulator """
    def __init__(self, K=1000, num_levels=2, z=[0.5, 0.5], d=1, p=[0.5, 0.5],
                 w_f=[1.5, 1.0], w_m=[3.0, 1.0]):
        """
        K              : number of offspring at each generation
        num_levels (i) : number of distinct patch types
        z_i            : fraction of children being male on patch i
        d              : dispersal probability for females
        p_i            : frequency of patch type i
        w_f_i          : competitive advantage of female type i
        w_m_i          : competitive advantage of male type i

        # TODO: include dynamics of z_i's
        """
        self.K = K
        self.num_levels = num_levels
        self.z = np.array(z)
        self.d = d
        self.p = np.array(p)
        self.w_f = np.array(w_f)
        self.w_m = np.array(w_m)

        self.males = np.zeros(num_levels)
        self.females = np.zeros(num_levels)

    def birth(self):
        self.males = self.K * self.z * self.p
        self.females = self.K * (1 - self.z) * self.p

    def breed(self):
        # TODO: for this model, need to change z_i ratios
        pass
