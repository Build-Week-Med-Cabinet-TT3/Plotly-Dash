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
            Our team had four days to create a model that can take a user's input (in this case, medical cannabis preferences) 
            and output the strain(s) that best match, as well as create a website for hosting our creation.
            ### Natural Language Processing:
            Machines cannot analyze raw text on their own, so we performed tokenization which is a task in Natural Language Processing (NLP).
            This method allows us to convert columns that are just text (descriptions of
            effects, ailments, taste) into numeric values that can be used for machine learning.
            """
        ),
        html.Img(src='assets/nearest_neighbor_ex.png', 
                 title="nearest neighbor example, image from wiki", 
                 style={'display':'block',
                        'width':'40%',
                        'margin':'auto'})
    ],
    style={'margin':'20px'},
)
column2 = dbc.Row(
    [
        dcc.Markdown(
            """
            ### Nearest Neighbor:
            Our team decided the best model to use for the task was the "k-nearest neighbors" algorithm. K-nearest neighbors 
            puts all the data 
            you're looking for onto a plane, with the recommendation you are searching for as points (in this case, the names of 
            medicinal cannabis strains). For an example, if you want a hybrid strain known for helping to cure insomnia, 
            with an earthy flavor, there might not be a recommendation that is spot on, so with k-nearest neighbors, our model will 
            find a point that is between the closest spreads of points, and pick the one with the most points
            in that area to output a recommendation.
            In the diagram above, we are trying to classify the green circle.
            Within the inner circle, there are two red triangles and one blue square.
            K-nearest neighbors would classify the green circle as similar to the red 
            triangle. 
            """
        ),
    ],
    style={'margin':'20px'},
)
column3 = dbc.Row(
    [
        dcc.Markdown(
            """
            ### Google API:
            For a stretch goal, our team decided to add a Locate page that would show the dispensaries nearest
            to a user's location. We decided on using Google Maps API for this task. When someone is 
            using our webpage, they can refer to the Locate tab to find the closest dispensary near them.
            """
        ),
    ],
    style={'margin':'20px'},  
)

img = html.Img(src='assets/pipe_left_crop.jpeg', 
               title="18th century pipe, images courtesy of metmuseum.org", 
               style={'width':'99%',
                      'display':'block',
                      'margin':'20px'})

layout = dbc.Row([column1, column2, column3, img])