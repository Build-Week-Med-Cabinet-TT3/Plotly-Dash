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
row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown('### Strain Type'),
                        dcc.Dropdown(
                            id='ctype',
                            style={
                                "color":"black",
                            },
                            options = [
                                {'label': 'Indica', 'value': 'Indica'},
                                {'label': 'Hybrid', 'value': 'Hybrid'},
                                {'label': 'Sativa', 'value': 'Sativa'},
                            ],
                            className='mb-5',
                            placeholder="The type of strain you want"
                        ),

                        dcc.Markdown('### Ailments'),
                        dcc.Dropdown(
                            id='ailment',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Stress', 'value': 'Stress'}, 
                                {'label': 'Depression', 'value': 'Depression'}, 
                                {'label': 'Pain', 'value': 'Pain'},
                                {'label': 'Insomnia', 'value': 'Insomnia'}, 
                                {'label': 'Lack Of Appetite', 'value': 'Lack Of Appetite'}, 
                                {'label': 'Nausea', 'value': 'Nausea'},
                                {'label': 'Inflammation', 'value': 'Inflammation'}, 
                                {'label': 'Muscle Spasms', 'value': 'Muscle Spasms'}, 
                                {'label': 'Seizures', 'value': 'Seizures'},
                            ], 
                            className='mb-5',
                            multi=True, 
                            placeholder="What you want to treat"
                        )
                    ]
                ),

                dbc.Col(
                    [
                        dcc.Markdown("### Desired Effects"),
                        dcc.Dropdown(
                            id='effects',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Happy', 'value': 'Happy'}, 
                                {'label': 'Dry Mouth', 'value': 'Dry Mouth'}, 
                                {'label': 'Relaxed', 'value': 'Relaxed'},
                                {'label': 'Euphoric', 'value': 'Euphoric'}, 
                                {'label': 'Uplifted', 'value': 'Uplifted'}, 
                                {'label': 'Paranoid', 'value': 'Paranoid'},
                                {'label': 'Sleepy', 'value': 'Sleepy'}, 
                                {'label': 'Anxious', 'value': 'Anxious'}, 
                                {'label': 'Creative', 'value': 'Creative'},
                                {'label': 'Energetic', 'value': 'Energetic'}, 
                                {'label': 'Hungry', 'value': 'Hungry'}, 
                                {'label': 'Focused', 'value': 'Focused'},
                                {'label': 'Tingly', 'value': 'Tingly'}, 
                                {'label': 'Talkative', 'value': 'Talkative'}, 
                                {'label': 'Horny', 'value': 'Horny'}, 
                            ],
                            className='mb-5',
                            multi=True,
                            placeholder="What effects you want"
                        ),

                        dcc.Markdown("### Flavor"),
                        dcc.Dropdown(
                            id='flavor',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Earthy', 'value': 'Earthy'}, 
                                {'label': 'Sweet', 'value': 'Sweet'}, 
                                {'label': 'Citrus', 'value': 'Citrus'},
                                {'label': 'Berry', 'value': 'Berry'}, 
                                {'label': 'Pine', 'value': 'Pine'}, 
                                {'label': 'Lemon', 'value': 'Lemon'},
                                {'label': 'Skunk', 'value': 'Skunk'}, 
                                {'label': 'Grape', 'value': 'Grape'}, 
                                {'label': 'Blueberry', 'value': 'Blueberry'},
                                {'label': 'Lime', 'value': 'Lime'}, 
                                {'label': 'Orange', 'value': 'Orange'}, 
                                {'label': 'Pepper', 'value': 'Pepper'},
                                {'label': 'Ammonia', 'value': 'Ammonia'}, 
                                {'label': 'Mango', 'value': 'Mango'}, 
                                {'label': 'Pineapple', 'value': 'Pineapple'},
                                {'label': 'Strawberry', 'value': 'Strawberry'}, 
                                {'label': 'Lavender', 'value': 'Lavender'},
                                {'label': 'Honey', 'value': 'Honey'}, 
                                {'label': 'Coffee', 'value': 'Coffee'}, 
                                {'label': 'Rose', 'value': 'Rose'},
                                {'label': 'Vanilla', 'value': 'Vanilla'}, 
                                {'label': 'Mint', 'value': 'Mint'}, 
                                {'label': 'Apple', 'value': 'Apple'}, 
                            ],  
                            className='mb-5',
                            multi=True,
                            placeholder="What you want it to taste like"
                        )
                    ]
                )
            ]
        )
    ]
)

layout = row