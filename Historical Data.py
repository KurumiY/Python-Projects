#import function 
from task_1 import my_function

my_function('historical/all')


#making a plot
import json

from plotly import graph_objects as go
from plotly import offline

filename = 'historical_all.json'
with open(filename) as f:
    wholedata = json.load(f)
#Create lists for plotly
pastcase_dicts = wholedata['cases']
pastdeath_dicts = wholedata['deaths']
pastrecover_dicts = wholedata['recovered']

dates, num_cases = [], []
for date, numcase in pastcase_dicts.items():
    dates.append(date)
    num_cases.append(numcase)

num_deaths = []
for date2, numdeaths in pastdeath_dicts.items():
    num_deaths.append(numdeaths)

num_recovered = []
for date3, numrecovered in pastrecover_dicts.items():
    num_recovered.append(numrecovered)

#plotlycode
fig1 = go.Figure(
    data = [
        go.Bar(
            name = 'cases', x = dates, y = num_cases, offsetgroup = 0,
            ),
        go.Bar(
            name = 'deaths', x = dates, y = num_deaths, offsetgroup = 1,
            ),
        go.Bar(
            name = 'recovered', x = dates, y = num_recovered, offsetgroup = 2,
            ),
        go.Scatter(
            name = 'trend of cases', x = dates, y = num_cases, mode = 'lines'
            ),
        go.Scatter(
            name = 'trend of deaths', x = dates, y = num_deaths, mode = 'lines'
            ),
        go.Scatter(
            name = 'trend of cases', x = dates, y = num_recovered, mode = 'lines'
            ), 
        ],
        layout = go.Layout(
            title = "Historical Data", xaxis_title="date",
            yaxis_title="numbers",))

offline.plot(fig1, filename= 'Program5_plot.html')


