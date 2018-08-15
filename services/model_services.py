from sqlalchemy import create_engine


class db_connector:
    '''
    Parent Class for db_connectors 4/4 testeable methods
    '''
    def __init__(self):
        '''
        @param self:
        '''
        self.db_route = None
        self.conn = None

    def set_db_route(self, route):
        '''
        @param self:
        @param route: db connection command string
        '''
        self.db_route = route

    def get_db_route(self):
        '''
        @param self:
        @return: route: db connection command string
        '''
        return self.db_route

    def connection(self):
        '''
        @param self:
        @raise NotImplementedError
        @return: db cursor
        '''
        raise NotImplementedError
    def query(self, sql):
        '''
        @param self:
        @param sql: string db query
        @raise NotImplementedError
        @return:
        '''
        raise NotImplementedError

class sqlite_service(db_connector):
    '''
    Instance for SQLite DB - Non testeable methods
    '''
    def connection(self):
        '''
        @param self:
        @raise Exception
        '''
        self.set_db_route('sqlite:///weather_predictor')
        db_connect = create_engine(self.get_db_route())
        try:
            self.conn = db_connect.connect()  # connect to database
        except:
            raise Exception('SQLite Connection Error')

    def query(self, sql):
        '''
        @param self:
        @param sql: string db query
        @raise Exception
        @return: MYSQLite cursor
        '''
        try:
            result = self.conn.execute(sql)
        except Exception as e:
            raise Exception('Query Excecution Error: ' + str(e))
        return result