from math import floor
from enum import Enum, unique

import numpy as np
import pandas as pd

@unique
class FracAge(Enum):
    Uniform = 'Uniform'
    Constant = 'Constant'

@unique
class AgeBasis(Enum):
    AgeNextBirthday = 'AgeNextBirthday'
    AgeLastBirthday = 'AgeLastBirthday'
    
class MortalityTable():

    def __init__(
        self, 
        qx_rates, 
        start_age=0, 
        select_rates=None,
        age_basis=AgeBasis.AgeNextBirthday,
        frac_age=FracAge.Uniform,
        *args,
        **kwargs):
        if not isinstance(age_basis, AgeBasis):
            raise TypeError('age_basis must be an instance of AgeBasis Enum')
        if not isinstance(frac_age, FracAge):
            raise TypeError('frac_age must be an instance of FracAge Enum')
        self.age_basis = age_basis
        self.frac_age = frac_age
        self.start_age = start_age
        self.qx = qx_rates
        self.__dict__.update(kwargs)

    def npx(self, n, x):
        if n < 0 or x < 0:
            raise ValueError('n and x cannot be negative')
        if n == 0:
            return 1
        if n < 1:
            if self.force == 'u':
                return 1 - self.qx[x] * n
            elif self.force == 'c':
                return self.px[x] ** n
            else:
                raise ValueError('force must be u (uniform) or c (constant)')
        else:
            remain = n - floor(n)
            n = floor(n)
            x_i = x - self.start_age
            x_end = x_i + n
            if x_i < 0:
                Warning(f'Mortality from age {x} to {self.start_age} assumed to be 0')
                x_i = 0
            if x_end < 0:
                return 1
            return np.product(self.px[x_i:x_end]) * self.npx(remain, x+n)

    def nqx(self, n, x):
        return 1 - self.npx(n, x)

    def ndef_qx(self, n, x):
        return self.npx(n, x) * self.nqx(1, x+n)

    def life_expect(self, x):
        pass

    def mortality_dataframe(self):
        pass

    @property
    def qx(self):
        return self._qx

    @property
    def px(self):
        return 1 - self._qx

    @property
    def ages(self):
        return np.array([self.start_age + i for i in range(len(self.qx))])

    @property
    def df(self):
        return pd.DataFrame({'qx': self.qx, 'px': self.px}, index=self.ages)

    @qx.setter
    def qx(self, rates):
        self._qx = np.array(rates)
        self._px = 1 - self._qx

    @px.setter
    def px(self, rates):
        self._px = np.array(rates)
        self._qx - 1 - self._px

    @classmethod
    def makeham(cls, a, b, c, n=120):
        pass

    @classmethod
    def gompertz(cls, a, b, n=120):
        pass

    @classmethod
    def valid_mortality(cls, rates):
        pass