"""
Name: Jack Wu
Email: Jack.Wu55@myhunter.cuny.edu
Title: Hate Crimes in NYC
URL: https://jackwu63.github.io/cs-39542/
Resources: https://crime-data-explorer.fr.cloud.gov/pages/explorer/crime/hate-crime 
           https://www1.nyc.gov/site/nypd/stats/reports-analysis/hate-crimes.page
"""

import pandas as pd
import json
import plotly.express as px 
import plotly.io as pio 
pio.renderers.default = 'browser' #opens the map in default browser

precinctMap = json.load(open("Police Precincts.geojson", 'r')) #loads the Police Precinc.geojson depicting the areas for each police precinct
df1 = pd.read_csv('HC-2019.csv') #reads Hate Crimes Arrests of 2019
df2 = pd.read_csv('HC-2020.csv') #reads Hate Crimes Arrests of 2020
df3 = pd.read_csv('HC-2021.csv') #reads Hate Crimes Arrests of Quarter 1,2, and 3 of 2021
precinct_id_map = {} 
for feature in precinctMap['features']: #for loop to map the ID of precincts to precincts
    feature['id'] = feature['properties']['precinct']
    precinct_id_map[feature['properties']['precinct']] = feature['id']

fig = px.choropleth_mapbox(df1, locations='Precinct', #plotly.express to create the choropleth map
                    geojson=precinctMap, #Using the police precinct geojson
                    color='Occurrences', #The colors depict the intensity of Occurrences
                    hover_name='Area', #Hovering over the precincts display the general area
                    mapbox_style="open-street-map", #The style of the map
                    center={'lat': 40.7128, 'lon': -74.0060}, #The starting point coordinates
                    zoom=9.5, 
                    opacity=0.5,
                    title="Hate Crimes in New York City, by Precinct and Year"
                    )

button1 = dict(method = "restyle", #Creates a 2019 button for the Hate Crimes Arrests of 2019
               args = [{'z': [df1["Occurrences"]]}], 
               label = "2019")

button2 = dict(method = "restyle", #Creates a 2020 button for the Hate Crimes Arrests of 2020
               args = [{'z': [df2["Occurrences"]]}],
               label = "2020")

button3 = dict(method = "restyle", #Creates a 2021 button for the Hate Crimes Arrests of 2021
               args = [{'z': [df3["Occurrences"]]}],
               label = "2021")

fig.update_layout(width=1900, #Layout for the button as well as the choropleth map
                  coloraxis_colorbar_thickness=23,
                  updatemenus=[dict(y=0.9,
                                    x=0.1,
                                    xanchor='right',
                                    yanchor='top',
                                    active=0,
                                    buttons=[button1,button2,button3]
                                )])
fig.show() #displays the map
