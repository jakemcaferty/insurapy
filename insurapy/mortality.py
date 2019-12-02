

class MortalityTable():

    def __init__(
        self, 
        rates, 
        start_age=0, 
        end_age=None, 
        age_inc=1,
        interp_method='u',
        *args,
        **kwargs):
        if interp_method.lower()[0] not in ['u', 'c']:
            raise ValueError("interp_method must be either u (uniform) or c (constant)")
        else:
            self.interp_method = interp_method.lower()[0]
        self.rates = rates
        self.start_age = start_age
        if end_age is None:
            self.end_age = start_age + age_inc * len(rates)
        else:
            self.end_age = end_age
        self.interp_method = interp_method
        self.__dict__.update(kwargs)

    def npx(self, n, x):
        pass

    def nqx(self, n, x):
        pass

    def ndef_qx(self, n, x):
        pass

    def life_expect(self, x):
        pass

    @classmethod
    def makeham(cls, a, b, c):
        pass

    @classmethod
    def gompertz(cls, a, b):
        pass

    @classmethod
    def valid_mortality(cls, rates):
        pass