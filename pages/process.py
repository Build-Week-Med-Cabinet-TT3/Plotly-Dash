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
            # Process
            Our team was given roughly a week to complete a model that would take a type of strain (input) and 
            give out a recommendation someone asking (output), and deploy it to Heroku.
            ### NLP:
            During the data exploration process, we put the data into a matrix (a table with columns and rows).
            Machines cannot analyze raw text on their own. We performed tokenization which is a task in Natural Language Processing (NLP).
            Without getting into too much details, this method allows us to convert columns that are just text (descriptions of
            effects, ailments, taste) into numeric values that can be used for machine learning.
            """
        ),
        html.Img(src='assets/nearest_neighbor_ex.png', title="nearest neighbor example, image from wiki", style={'width':'40%'})
    ],
)
column2 = dbc.Row(
    [
        dcc.Markdown(
            """
            ### Nearest Neighbor:
            Our team decided the best model to use for the task was the nearest neighbor. Nearest neighbor can easily 
            take data input and output the desired number of suggestions. Nearest neighbor pretty much sets all the data 
            you're looking for onto a plane with the recommendation you are searching for as points (in this case the name of 
            medicinal marijuanas). For an example, if you want a hybrid strain with the effect of happiness, to cure insomnia, 
            and has an earthy flavor. There might not be a recommendation that is spot on, so with nearest neighbor, our model will 
            find a point that is between the closest spreads of points, and pick the one with the most points
            in that area to decide on the recommendation to use.
            In the picture provided above, we are trying to classify the green circle.
            Within the inner circle, there are two red triangles and one blue square.
            Nearest neighbor would classify the green circle as the same as the red 
            triangle. 
            """
        ),
        #html.Img(src='assets/pipe_left_crop.jpeg', title="18th century pipe, images courtesy of metmuseum.org", style={'width':'100%'})
    ],
)
column3 = dbc.Row(
    [
        dcc.Markdown(
            """
            ### Google API:
            To go a bit further, our team decided to add a locations page that would show the nearest dispensaries near 
            someone's location that is using our application. We decided on using Google Maps Api for this task. When someone is 
            using our webpage, they can refer to the next tab to find the closest dispensary near them.
            """
        ),
        html.Img(src='assets/pipe_left_crop.jpeg', title="18th century pipe, images courtesy of metmuseum.org", style={'width':'100%'})
    ],
)
layout = dbc.Row([column1, column2, column3])