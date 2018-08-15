
class planet():
    '''
    Planet model -- 6/6 methods expected to be testeables
    '''
    name = None
    speed = None
    ratio = None
    def __init__(self, name, speed, ratio):
        '''
        @param self:
        @param name: planet name string
        @param speed: speed numeric value
        @param ratio: ratio numeric value
        @return:
        '''
        self.name = name
        self.speed = speed
        self.ratio = ratio

    def set_name(self, name):
        '''
        @param self:
        @param: name string value
        '''
        self.name = name

    def set_speed(self, speed):
        '''
        @param self:
        @param: speed numeric value
        '''
        self.speed = speed

    def set_ratio(self, ratio):
        '''
        @param self:
        @param: ratio numeric value
        '''
        self.ratio = ratio

    def get_name(self):
        '''
        @param self:
        @return: name string value
        '''
        return self.name

    def get_speed(self):
        '''
        @param self:
        @return: speed numeric value
        '''
        return self.speed

    def get_ratio(self):
        '''
        @param self:
        @return: ratio numeric value
        '''
        return self.ratio