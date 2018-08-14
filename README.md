# Weather Calculator

This code can be used to calculate the weather in a specific day for the solar a solar system where there are 3 planets with perfectly circular orbit, they have different angular velocities and different distances among the sun.

please use: 
```sh
python calculator.py
```
To try out the calculations and
```sh
python calculator.py populate
```
to persist all the data in a sqlite db located at weather_predictor file


For Running tests:
```sh
python -m unittest ttests.test_calculations_helper
```
```sh
python -m unittest tests.test_calculator
```

To start Web Service:
```sh
python server.py
```

Trying service:
```sh
http://0.0.0.0:5000/clima?dia=10
```