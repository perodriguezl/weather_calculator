#!/usr/bin/python3
import os
from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from services.model_services import sqlite_service
from services.day_weather_services import day_weather_services
from models.planet import planet
from models.day_weather import day_weather


db_connect = create_engine('sqlite:///weather_predictor')
app = Flask(__name__)
api = Api(app)


class Clima(Resource):
    def get(self):
        '''
        [get] /clima
        parameters: dia={{integer}} required
        response format: json
        https://desolate-beyond-76412.herokuapp.com/clima?dia=999
        [ok]: {"dia": 999, "clima": "Lluvia"}
        https://desolate-beyond-76412.herokuapp.com/clima?dia=-1000
        [bad]: {'error':'resource_not_found'}
        '''
        if 'dia' in request.args:
            day = request.args['dia']
        else:
            day = None
        if day != None:
            dw = day_weather_services(sqlite_service(), day_weather)
            calculated_weather = dw.get_day_wheater(day)
            if calculated_weather:
                return {
                    'dia': calculated_weather.get_day(),
                    'clima': calculated_weather.get_weather()
                }
        return Response("{'error':'resource_not_found'}", status=404)


api.add_resource(Clima, '/clima') # Route_1

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
