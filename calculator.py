from sqlalchemy import create_engine
import math
import sys
from calculations_helper import calculations_helper


class calculator:
    '''
    Instance designed to handle all the business associated to the weather calculation populator -- 5 methods expected to be testeables
    '''
    planets = None
    persist = None

    def __init__(self):
        '''
        @param self:
        @return:
        '''
        self.helper = calculations_helper()
        self.max_perimeter = self.max_area = self.dry_count = self.monsoon_count = self.rain_count = self.perfect_count = 0
        self.monsoon_days = self.perfect_days = self.dry_days = []
        self.min_area = None
        # (populate) value for first argument if all info need to be populated

    def populator(self):
        '''
        @param self:
        @return:
        '''
        db_connect = create_engine('sqlite:///weather_predictor')
        self.conn = db_connect.connect()  # connect to database
        arguments = sys.argv
        if len(arguments) > 1 and arguments[1] == 'populate' and self.persist == None:
            self.persist = True
            self.clean_table()
        else:
            self.persist = False
        self.set_planets(self.load_planets(self.query_planets().cursor))
        start_day = 0
        last_day = self.helper.calculate_last_day(10, 365, 1)
        self.calculate_weather(self.planets, start_day, last_day)
        self.show_results()

    def clean_table(self):
        '''
        @param self:
        @return:
        '''
        query = self.conn.execute(
            "DELETE FROM day_weather WHERE day >= 0")  # cleaning day_weather table before populating

    def set_planets(self, planets):
        '''
        @param self:
        @param planets: planet object array
        @return:
        '''
        self.planets = planets

    def get_planets(self):
        '''
        @param self:
        @return:
        '''
        return self.planets

    def query_planets(self):
        '''
        @param self:
        @return: MySQLi Cursor containing planets in table
        '''
        return self.conn.execute("select * from planets")

    def load_planets(self, data):
        '''
        @param self:
        @param data: planets in MySQLi Cursor
        @return: planet object array
        '''
        planets = []
        for i in data:
            planets.append({
                'name': i[0],
                'speed': i[1],
                'ratio': i[2]
            })
        return planets

    def calculate_weather(self, planets, start_day, last_day):
        '''
        @param self:
        @param planets: planet object array
        @param start_day: start_day integer
        @param last_day: last_day integer
        @return:
        '''
        current_weather = []
        for day in range(start_day, last_day):
            weather = self.day_weather(planets, day)
            current_weather.append(weather)
            if self.persist:  # verify if parameter to populate is sent
                self.conn.execute("insert into day_weather values('{0}','{1}')".format(day, weather))

    def show_results(self):
        '''
        @param self:
        @return:
        '''
        print("Periodos de Sequia:" + str(self.dry_count))
        print("Periodos de Lluvia Intensa: " + str(self.monsoon_count))
        print("Dias de Lluvia Intensa: " + str(self.monsoon_days))
        print("Periodos de Lluvia: " + str(self.rain_count))
        print("Periodos Optimos de Presion y Temperatura: " + str(self.perfect_count))
        if self.persist:  # verify if parameter to populate is sent
            print("Database Populated")

    def day_weather(self, planets, day):
        '''
        @param self:
        @param planets: planet object array
        @param day: day integer
        @return: day_weather string
        '''
        day_weather = "Indeterminado"
        last_planet = None
        dry = True
        positions = []
        for planet in planets:
            planet['position'] = self.helper.position_calculator_degrees(planet['speed'], day)
            planet['x'] = self.helper.calculate_x(planet)
            planet['y'] = self.helper.calculate_y(planet)
            if last_planet != None and not self.helper.aligned_planets(last_planet, planet['position']):
                dry = False
            positions.append(planet['position'])
            last_planet = planet['position']
        calculated_area = self.helper.calculate_area(self.helper.calculate_perimeter(planets)['sides'])
        perimeter = self.helper.calculate_perimeter(planets)['perimeter']
        if dry:
            self.dry_days.append(day)
            self.dry_count = self.dry_count + 1
            day_weather = "Sequia"
        elif calculated_area <= self.helper.zero_bias_area:  # assuming the maximum acceptance for area to be considered aligned
            self.perfect_days.append(day)
            self.perfect_count = self.perfect_count + 1
            day_weather = "Presion y Temperatura Optima"
        else:
            if self.helper.is_sun_included(positions):
                day_weather = "Lluvia"
                if perimeter >= self.helper.max_estimated_perimeter:  # due to rounding limitations all perimeter over this value are at the same perimeter length
                    self.monsoon_count = self.monsoon_count + 1
                    self.monsoon_days.append(day)
                    day_weather = day_weather + " Intensa"
                self.rain_count = self.rain_count + 1
        return day_weather


if __name__ == '__main__':
    help = calculator()
    help.populator()
