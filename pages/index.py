# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """

            """
        ),
    ],
    md=4,
)



column3 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Are you ready to try medical cannabis?

            Med Cabinet listens to you and your needs. Do you need help sleeping? Pain relief? Do you want to feel calm, or energetic?

            Med Cabinet is created for the first-time MMJ user, who wants to explore the therapeutic possibilities of cannabis.

            """
        ),
        dcc.Link(dbc.Button('Click here to try it out', color='primary'), href='/predictions')
    ],
    md=4,
)

layout = dbc.Row([column1, column2, column3])