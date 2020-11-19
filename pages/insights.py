# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Unit 3 
            


   

            


            """
        ),
    
    ]
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Unit 4

            ### Hunter
            fdgdfgdfgdffggdfdfg
            fdgdfgfdddddd
            dfgdfgdgfdgfd
            ### Leo
            fdgfdgdfgdfgdf
            dfgdfgdfgdfffffff
            dfgdfgdfgdfgdfgdfgd


            


            """
        ),
    
    ]
)
column3 = dbc.Row(
    [
        dcc.Markdown(
            """
        

            


            """
        ),
    html.Img(src='/assets/pipe_right.jpeg', title="18th century pipe, images courtesy of metmuseum.org", style={'width':'100%'})    

    ]
)



layout = dbc.Row([column1, column2, column3])