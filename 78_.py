class Planet:

    shape = 'square'

    def __init__(self, water, moon):
        self.water = water
        self.moon = moon

    def orbit(self):
        return f'{self.water} and satellible is {self.moon}'

    @classmethod
    def commons(cls):
        return f'all the planets are {cls.shape}'

    @staticmethod
    def spin(speed = '20000m/s speed'):
        return f'Japan is not effected by {speed}'


naboo = Planet('Yes','moon is not present')
print(Planet.shape)
print(Planet.commons())

print('-------------------------------')

print(naboo.orbit())

# @staticmethod 何も入れなければデフォルトのまま。何か入れれば変わる。
print(Planet.spin())