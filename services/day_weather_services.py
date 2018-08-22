
class day_weather_services():
    '''
    Day Weather Services Instance - 1/1 expected to be testeables
    @param object: db_connector
    @param object: planet model
    '''
    def __init__(self, db_connector, day_weather_model):
        '''
        @param self:
        @param db_connector: db_connector_child
        @param day_weather_model: planet model instance
        '''
        self.db_connector = db_connector
        self.day_weather_model = day_weather_model
        self.db_connector.connection()

    def get_day_wheater(self, day):
        '''
        @param self:
        @return None/day_weather model objects array
        '''
        sql = "SELECT * FROM day_weather WHERE day = {0}".format(day)
        query = self.db_connector.query(sql)
        for day_wheather in query:
            return self.day_weather_model(day_wheather[0], day_wheather[1])