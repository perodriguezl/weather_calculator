
class planet_services():
    '''
    Planet Services Instance - 5/5 expected to be testeables
    @param object: db_connector
    @param object: planet model
    '''
    def __init__(self, db_connector, planet_model):
        '''
        @param self:
        @param db_connector: db_connector_child
        @param planet_model: planet model instance
        '''
        self.db_connector = db_connector
        self.planet_model = planet_model
        self.db_connector.connection()
        self.persist = False

    def clean_repository(self):
        '''
        @param self:
        '''
        if self.persist == True:
            sql = "DELETE FROM day_weather"
            self.db_connector.query(sql)

    def get_planets(self):
        '''
        @param self:
        @return None/planet model objects array
        '''
        sql = "SELECT * FROM planets"
        query = self.db_connector.query(sql)
        planets = []
        for planet in query:
            planets.append(self.planet_model(planet[0], planet[1], planet[2]))
        return planets

    def add_day(self, day, weather):
        '''
        @param self:
        '''
        if self.persist == True:
            self.db_connector.query("INSERT INTO day_weather VALUES('{0}','{1}')".format(day, weather))

    def set_persist(self, state):
        '''
        @param self:
        @param state:
        '''
        self.persist = state
        if state == True:
            self.clean_repository()

    def get_persist(self):
        '''
        @param self:
        @return persist: boolean value
        '''
        return self.persist