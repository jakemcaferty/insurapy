import numpy as np
import pandas as pd

class MortalityTable():

    def __init__(
        self, 
        qx_rates, 
        start_age=0, 
        select_rates=None,
        age_basis='anb',
        interp_method='u',
        *args,
        **kwargs):
        if interp_method.lower() not in ['u', 'c']:
            raise ValueError("interp_method must be either u (uniform) or c (constant)")
        if age_basis.lower() not in ['anb', 'alb']:
            raise ValueError("age_basis must be either anb (age nearest birthday) or alb (age last birthday)")
        self.age_basis = age_basis
        self.interp_method = interp_method.lower()
        self.start_age = start_age
        self.qx = qx_rates
        self.__dict__.update(kwargs)

    def npx(self, n, x):
        start_index = x - self.start_age
        end_index = start_index + n
        if start_index < 0:
            Warning(f'Mortality from age {x} to {self.start_age} assumed to be 0')
            start_index = 0
        if end_index < 0:
            return 1
        return np.product(self.px[start_index:end_index])

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