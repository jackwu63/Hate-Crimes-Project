"""
Title: Hate Crimes in NYC
URL: https://jackwu63.github.io/cs-39542/
Resources: https://crime-data-explorer.fr.cloud.gov/pages/explorer/crime/hate-crime 
           https://data.cityofnewyork.us/Public-Safety/NYPD-Hate-Crimes/bqiq-cu78
"""

from folium.map import FitBounds
import pandas as pd
import json
import math
import numpy as np
import folium
import plotly
import plotly.express as px 
import plotly.io as pio 
pio.renderers.default = 'browser'

precinctMap = json.load(open("Police Precincts.geojson", 'r'))
df = pd.read_csv('HC-2019.csv')
precinct_id_map = {}
for feature in precinctMap['features']:
    feature['id'] = feature['properties']['precinct']
    precinct_id_map[feature['properties']['precinct']] = feature['id']

fig = px.choropleth_mapbox(df, locations='Precinct',
                    geojson=precinctMap,
                    color='Occurrences',
                    hover_name='Area',
                    hover_data=['Percentage'],
                    mapbox_style="open-street-map",
                    center={'lat': 40.7128, 'lon': -74.0060},
                    zoom=9.5,
                    opacity=0.5,
                    title="Hate Crimes in New York City, by Precinct, 2019",
                    )
fig.show()