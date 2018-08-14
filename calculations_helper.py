import math

class calculations_helper:
    '''
    Instance designed to contain all the reusable calculation methods -- Expected 100% test coverage
    '''

    def __init__(self):
        '''
        @param self:
        @return:
        '''
        self.full_cicle = 360
        self.half_cicle = 180
        self.zero_bias_area = 457627328.2 #bias maximum considered value for aligned planets
        self.max_estimated_perimeter = 6262 #perimeter

    def aligned_planets(self, planet_1, planet_2):
        '''
        @param self:
        @param planet_1: planet_1 degree position
        @param planet_2: planet_2 degree position
        @return: Boolean depending if two planets are aligned
        '''
        if planet_1 == planet_2 or planet_1 == planet_2 + self.half_cicle or planet_1 == planet_2 - self.half_cicle:
            return True
        else:
            return False
    def calculate_side(self, planet_1, planet_2):
        '''
        @param self:
        @param planet_1: planet object
        @param planet_2: planet object
        @return: float value with the calculated distance between 2 points
        '''
        inner_sqrt = float(pow(planet_2['x'] - planet_1['x'], 2) + pow(planet_2['y'] - planet_1['y'], 2))
        return float(math.sqrt(inner_sqrt))

    def calculate_perimeter(self, planets):
        '''
        @param self:
        @param planets: planets object array
        @return: object containing perimeter and distance between points
        '''
        d01 = self.calculate_side(planets[0], planets[1])
        d02 = self.calculate_side(planets[0], planets[2])
        d12 = self.calculate_side(planets[1], planets[2])
        return {
            'perimeter': d01 + d02 + d12,
            'sides': [d01, d02, d12]
        }

    def calculate_last_day(self, years, days_per_year, start_day):
        '''
        @param self:
        @param years: years integer
        @param days_per_year: days_per_year integer
        @param start_day: start_day integer
        @return: integer of the last day to be evaluated
        '''
        return (years * days_per_year) + start_day

    def calculate_area(self, sides):
        '''
        @param self:
        @param sides: array containing the distances between points
        @return: calculated area
        '''
        s = sum(sides)/2
        area = s*(s-sides[0])*(s-sides[1])*(s-sides[2])
        return area

    def calculate_x(self, planet):
        '''
        @param self:
        @param planet: planet object
        @return: x position
        '''
        return round(planet['ratio'] * math.cos(math.radians(planet['position'])), 5)

    def calculate_y(self, planet):
        '''
        @param self:
        @param planet: planet object
        @return: y position
        '''
        return round(planet['ratio'] * math.sin(math.radians(planet['position'])), 5)

    def position_calculator_degrees(self, w, day):
        '''
        @param self:
        @param w: angular velocity
        @param day: current day
        @return: current degree
        '''
        return ((w * day) % self.full_cicle)

    def is_sun_included(self, positions):
        '''
        @param self:
        @param positions: degrees angles of planets
        @return: boolean meaning if the sun is included in the triangle
        '''
        positions.sort()
        return max(positions) - min(positions) > self.half_cicle and max(positions) - positions[1] <= self.half_cicle