"""
Created on Tue Oct 01
For Mango Solutions Python test
For any questions please contact Claire Blejean: claire.blejean@gmail.com

The data analysed in this exercise is presented in the format of a dashboard. It relies on the installation of the dash package.
The dashboard is here in a development format and hosted locally. It can be seen by visiting http://127.0.0.1:8050/.
If operating windows, please enable 'Internet Information Services' from 'Turn Windows features on or off', to access localhost.
In the context of a client project such a dashboard could be deployed on a server for wide-spread access.

"""

#%%

#Please ensure the dash package is installed
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np

#%%
#Link the directory where the free throw csv is stored
df = pd.read_csv('C:/Users/hel-claireb/Documents/Mango/free_throws.csv')


#%%
    
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        
app.layout = html.Div(children=[
        html.H1(children='NBA Free Throws',
            style={
                    'marginLeft': '20%',
                    'marginRight': '10%',
                    'marginTop': '20px',
                    'marginBottom':'40px'
                    }),

    html.Div(children='Select the type of games:',
            style={
                    'marginLeft': '10%',
                    'marginRight': '5%',
                    }),

#Dropdown menu enables the user to select between regular, playoffs or all games             
    dcc.Dropdown(
            id='Game types',
            options=[
                    {'label': 'Regular season', 'value': 'regular'},
                    {'label':'Playoffs', 'value':'playoffs'},
                    {'label':'All', 'value':'All'}
                    ],
            value='All',
            style={
                'max-width': '600px',
                   'marginLeft': '5%',
                   'marginRight': '5%'
                   },
                ),

    dcc.Graph(
        id='Free throws',
        style={
                'max-width': '800px',
                'marginBottom':'40px'
               },
        ),
            
    html.H4(children='Players league table',
            style={
                    'marginLeft': '20%',
                    'marginRight':'10%'
                    }),
    
    html.Div(children='Select the season(s):',
                style={
                    'marginLeft': '10%',
                    'marginRight':'5%'
                    }),

#Dropdown menu enables the user to chose one or several season for a player league table     
    dcc.Dropdown(id='seasons_select', 
                 options=[{'label': i, 'value': i} for i in df['season'].unique()],
                 multi=True, 
                 value=[df['season'].unique()[-1]],
                 style={
                        'max-width': '600px',
                        'marginLeft':'5%',
                        'marginRight':'5%',
                        'marginBottom':'20px'
                        }
                 ),
    
    dash_table.DataTable(
            id='player league table',
            sort_action='native',
            fixed_rows={'headers': True},
            style_table={
                    'maxWidth' : '700px',
                    'maxHeight': '400px',
                    'margin-left': '5%',
                    'margin-right':'5%',
                    },
            style_header={
                        'backgroundColor': 'lightslategrey',
                        'color' : 'white',
                        'font_size': '14px'
                        },
            style_cell_conditional=[
                        {
                        'if': {'column_id': 'Player'},
                        'textAlign': 'left'
                        }
                        ],
            style_cell={
                        'padding': '5px',
                        'font_size': '14px',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0,
                        },
            style_as_list_view=True,
            )

])
    
#The graph and table are dependent on the selection of the dropdown menus
@app.callback(
    [Output('Free throws', 'figure'),
    Output('player league table', 'data'),
    Output('player league table', 'columns')],
    [Input('Game types', 'value'),
     Input('seasons_select', 'value')])

def update_figure(games, seasons):
#filters the dataframe based on the dropdown selection
    if games == 'All':
        filtered_df = df
    else:
        filtered_df = df[df.playoffs == games]

#This data set displays the total number of successful shots per season in a bar format
#It also shows the percentage of success on hover          
    trace1 = {
        'name':'Successful shot',
        'type':'bar',
        'x': filtered_df['season'].unique(),
        'y': pd.crosstab(filtered_df.season, filtered_df.shot_made)[1],
        'showlegend':False,
        'hoverinfo':'text',
        'text': [str(i) + '% Successful' for i in round(filtered_df.groupby('season')['shot_made'].mean()*100, 2)],
        'marker':{
                'cmin': 5,
                'cmax': 25,
                'color': np.arange(len(filtered_df['season'].unique()))+10,
                'color_continuous_scale':'Magma'
                }
        }

#This data set displays the total number of unsuccessful shots per season in a bar format
#It also shows the total number of free throws made on hover   
    trace2 = {
        'name':'Unsuccessful shot',
        'type':'bar',
        'x': filtered_df['season'].unique(),
        'y': pd.crosstab(filtered_df.season, filtered_df.shot_made)[0],
        'showlegend':False,
        'hoverinfo':'text',
        'text': [str(i) + ' Shots total' for i in filtered_df.groupby('season').size()],
        'marker':{
                'cmin': 5,
                'cmax': 25,
                'color': np.arange(len(filtered_df['season'].unique()))+10,
                'color_continuous_scale':'Magma',
                'opacity' : 0.5
                }
        }

#This data set shows the average number of free throws per game per season in a linked scatter plot format
#The exact value is displayed on hover
    trace3 = {
        'name':'Average number of Free Throws per game',
        'type' : 'scatter',
        'x': filtered_df['season'].unique(),
        'y': filtered_df['season'].value_counts()/filtered_df.groupby('season')['game_id'].nunique(),
        'marker':{
                'size':12,
                'color':'lightslategrey'
                },
        'yaxis':'y2',
        'hoverinfo':'text',
        'text': round(filtered_df['season'].value_counts()/filtered_df.groupby('season')['game_id'].nunique(), 2)             
        }
    
    g_data = go.Data([trace1, trace2, trace3])

#Given the amount of information displayed on hover, a minimalist layout was chosen, with most functions disabled.

#For clarity the scatter plot is offset with the variable ymax    
    ymax = max(filtered_df.groupby('season')['shot_made'].count())*1.3

    layout ={
        'xaxis': {
                'ticks':'',
                'showgrid':False,
                'showline':True,
                'zeroline':False,
                'autorange':True,
                },
        'yaxis' : {
                'ticks':'',
                'showgrid':False,
                'showticklabels':False,
                'showline':False,
                'zeroline':False,
                'range':[0, ymax],
                },
        'yaxis2': {
                'side': 'right', 
                'overlaying': 'y',
                'ticks':'',
                'showgrid':False,
                'showticklabels':False,
                'showline':False,
                'zeroline':False,
                'autorange':True,
                'rangemode':'tozero'
                },
        'barmode':'stack',
        'legend': {
                'orientation': 'h',
                'font':{'size':14},
                'x':0,
                'y':5
                }
            }
    

#A table presenting the total number of shots made, the total number of successful shots and the success rate,
# per player, per season (with multiple season being possible)

    tb = filtered_df.loc[filtered_df['season'].isin(seasons)].groupby('player')['shot_made'].agg(['count', 'sum', 'mean']).reset_index()
    tb.columns = ['Player', 'Total shots', 'Successful shots', 'Success rate']
    tb = tb.sort_values('Successful shots', ascending = False) #table initially sorted by successful shots
    tb['Success rate']=(tb['Success rate']*100).map('{:,.2f}%'.format)    
    data=tb.to_dict('records')
    columns=[{"name": i, "id": i} for i in tb.columns]
    
    figure={
            'data' : g_data,
            'layout' : layout,
            }
    
    return figure, data, columns


if __name__ == '__main__':
    app.run_server(port=8050)
