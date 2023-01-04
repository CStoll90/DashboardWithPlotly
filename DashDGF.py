import plotly.express as px
import pandas as pd

import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

px.set_mapbox_access_token("pk.eyJ1IjoiY29ycmk1dG8iLCJhIjoiY2xidWwycTU5MW1jYzN2bXZsbWVqNjJ1NiJ9.QeQTdGqMxKbFdMK01S_KbQ")

# df_geo_full = pd.read_csv('deutscheglasfaser_bvmortefull3de.csv', sep='|')
df_geo_fbfull = pd.read_csv('deutscheglasfaser_geodatennfbfullde.csv', sep='|')
df_geo_bvmfull = pd.read_csv('deutscheglasfaser_bvmgeofullde.csv', sep='|')
df_geo_nvmfull = pd.read_csv('deutscheglasfaser_nvmgeofullde.csv', sep='|')

df_merge = pd.concat([df_geo_fbfull, df_geo_nvmfull, df_geo_bvmfull])  # ,df_geo_bvmfull, df_geo_nvmfull
df_merge.reset_index(inplace=True)

markdown_text = '''
# A simple look at DGF marketing locations in Germany

made possible by ASOD, dash and plotly express :)
'''

fig1 = px.scatter_mapbox(df_merge, lat="latitude", lon="longitude", color="projektstatus_alt", size="radius",
                         color_continuous_scale=px.colors.cyclical.IceFire, size_max=40, zoom=10)

fig1.update_layout(width=1200, height=800)
app.layout = html.Div([
        html.Div([dcc.Markdown(children=markdown_text)]),
        dcc.Graph(id='graph', figure=fig1),
])

if __name__ == '__main__':
    # print(df_merge.head())
    app.run_server(debug=True)
