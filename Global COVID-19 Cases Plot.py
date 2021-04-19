#import my_function from task 1.py
from task_1 import my_function

my_function('countries')

#This is the one with the countries and then you can plot from here
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'countries.json'
with open(filename) as f:
    wholedata = json.load(f)
    
wholedata_dicts = wholedata[:]

Total, CountryName, lons, lats = [], [], [], []
for wholedata_dict in wholedata_dicts:
    cases = wholedata_dict['cases']
    lon = wholedata_dict['countryInfo']['long']
    lat = wholedata_dict['countryInfo']['lat']
    Total.append(cases)
    lons.append(lon)
    lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]


data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats,
         'marker': {'size': [0.0004*cases for cases in Total],'color': Total,
                    'colorscale': 'Viridis', 'reversescale': True,
                    'colorbar': {'title': 'Total Cases',},},}]

my_layout = Layout(title='Global Coronavirus Cases')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'Program1_plot.html')

