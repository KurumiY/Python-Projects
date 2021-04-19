from task_1 import my_function

my_function('nyt/states')

#making a plot
import json

from plotly.graph_objs import Bar, Layout
from plotly import offline

filename = 'nyt_states.json'
with open(filename) as f:
    wholedata = json.load(f)

wholedata_dicts = wholedata[:]

latest, stateslist = [], []
for wholedata_dict in wholedata_dicts:
    if wholedata_dict['date'] == '2020-04-25':
        latest.append(wholedata_dict['cases'])
        stateslist.append(wholedata_dict['state'])

data= [{'type': 'bar', 'x': stateslist, 'y': latest}]

my_layout = {'title': '2020-04-25 Coronavirus Cases in US',
             'xaxis_title': 'State Name', 'yaxis_title': 'Number of Cases'}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Program2_plot.html')

