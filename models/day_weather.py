
class day_weather():
    '''
    Day Weather model -- 4/4 methods expected to be testeables
    '''
    def __init__(self, day, weather):
        '''
        @param self:
        @param day: day value integer
        @param weather: predicted string
        @return:
        '''
        self.day = day
        self.weather = weather

    def get_day(self):
        '''
        @param self:
        @return: day value integer
        '''
        return self.day

    def get_weather(self):
        '''
        @param self:
        @return: weather: predicted string
        '''
        return self.weather

    def set_day(self, day):
        '''
        @param self:
        @param: day value integer
        '''
        self.day = day

    def set_weather(self, weather):
        '''
        @param self:
        @param: weather: predicted string
        '''
        self.weather = weather