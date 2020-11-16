# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Example to make sure commit worked

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        daq.Knob(
        id='my-daq-knob',
        min=0,
        max=12,
        value=7
        )  
    ]
)

layout = dbc.Row([column1, column2])