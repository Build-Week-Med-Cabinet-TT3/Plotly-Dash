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

            Our team was givin roughly a week to complete a model that would take a type of strain and 
            give out a recommended type giving specific features.

            ### Monday

            The teams scheduling started off kind of rough because of how our track team was designed at 
            first. The team only had two members in Unit 3 and none at all in Unit 4. At first when the team
            was assembled, we had to finish up assignments that was supposed to be completed on the previous 
            Friday. After finally getting Github and Trello going along, our team finally was able to start 
            giving out roles and tasks. With the dataset from "placeholder", our Unit 4 members started
            data wrangling and deciding what model to use. While Unit 3 spent their time working on the API.
            
            Going off of the TODO checklist: 
            
                * Our team found a dataset and preformed EDA on it. 
                
                * Filled up the "stories" section on Trello. 
                
                * Deploy what we had working today onto Heroku.

                * Decided to use Plotly Dash for our API.

            Our team was able to complete all the task giving from the module checklist, and was procceding
            smoothly.



            
            
            
            
            ### Tuesday

            Who would of thought after all these months of starting a stand up or lecture at 9 A.M Lambda
            time, the calender said to hold it at 8 A.M?? That actually threw our build team off a bit. 
            However, that did not stop the adaptability and prowess of our team to move things forward.
            Today our team decided on our model and deploy it onto the correlating files. Because our Unit
            4 people had the most experience, Unit 3 handed that task to them. The Unit 3 people decided 
            to pick the brains of how Unit 4 did their process, and Unit 3 continued to work on the API.

            The TODO checklist for Tuesday is still a WIP: 

                * Move data so the app can use it

                * Deploy the data via Heroku 

                * Have a working model

        



            """
        ),

    ],
)

layout = dbc.Row([column1])