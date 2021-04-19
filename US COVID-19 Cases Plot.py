#import my_function from task 1.py
from task_1 import my_function

my_function('jhucsse/counties')

#import application
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'jhucsse_counties.json'
with open(filename) as f:
    wholedata = json.load(f)

wholedata_dicts = wholedata[:]

Total, lons, lats = [], [], []
for wholedata_dict in wholedata_dicts:
    cases = wholedata_dict['stats']['confirmed']
    lon = wholedata_dict['coordinates']['longitude']
    lat = wholedata_dict['coordinates']['latitude']
    Total.append(cases)
    lons.append(lon)
    lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]


data = [{'type': 'scattergeo', 'lon': lons, 'lat': lats,
         'marker': {'size': [0.005*cases for cases in Total],'color': Total,
                    'colorscale': 'Viridis', 'reversescale': True,
                    'colorbar': {'title': 'Total Cases',},},}]

my_layout = Layout(title='US Coronavirus Cases',geo_scope='usa')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'Program4_plot.html')


