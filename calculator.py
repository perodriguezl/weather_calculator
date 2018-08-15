import sys
from calculations_helper import calculations_helper
from models.planet import planet
from models.day_weather import day_weather
from services.model_services import sqlite_service
from services.planet_services import planet_services


class calculator:
    '''
    Instance designed to handle all the business associated to the weather calculation populator -- 7/9 methods expected to be testeables
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
        self.planet_services = planet_services(sqlite_service(), planet)

    def main(self):
        '''
        Main Business Method
        @param self:
        @return:
        '''
        start_day = 0
        self.planet_services.set_persist(self.would_persist(sys.argv))
        self.set_planets(self.load_planets(self.planet_services.get_planets()))
        last_day = self.helper.calculate_last_day(10, 365, 1)
        self.calculate_weather(self.planets, start_day, last_day)
        self.show_results()

    def would_persist(self, arguments):
        '''
        @param self:
        @param arguments: arguments string array
        @return:
        '''
        if len(arguments) > 1 and arguments[1] == 'populate' and self.persist == None:
            return True
        else:
            return False

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
        @return: planets object array
        '''
        return self.planets

    def load_planets(self, data):
        '''
        @param self:
        @param data: planet object array
        @return: planet object array
        '''
        planets = []
        for i in data:
            planets.append({
                'name': i.get_name(),
                'speed': i.get_speed(),
                'ratio': i.get_ratio()
            })
        return planets

    def calculate_weather(self, planets, start_day, last_day):
        '''
        @param self:
        @param planets: planet object array
        @param start_day: start_day integer
        @param last_day: last_day integer
        @return: day
        '''
        full_weather = []
        for day in range(start_day, last_day):
            weather = self.day_weather_calculation(planets, day)
            full_weather.append(day_weather(day, weather))
            self.planet_services.add_day(day, weather)
        return full_weather

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

    def day_weather_calculation(self, planets, day):
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
    help.main()
