"""Embed a Google map for locating cannabis dispensaries"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from os import getenv

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Cannabis dispensaries near you:
            Call ahead for selection and availability.

            """
        )
    ]
)

layout = dbc.Row([column1, html.Iframe(src = 'https://www.google.com/maps/embed/v1/search?key={}&q=cannabis+dispensaries'.format(getenv('API_key')), 
                     style={'width':'100%', 'height':'500px'})])

#layout = html.Iframe(src = 'https://www.google.com/maps/embed/v1/search?key={}&q=cannabis+dispensaries'.format(getenv('API_key')), 
 #                    style={'width':'100%', 'height':'500px'})