# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import dash_daq as daq
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import spacy
import pickle
import pandas as pd
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
                                {'label': 'Relaxed', 'value': 'Relaxed'},
                                {'label': 'Euphoric', 'value': 'Euphoric'}, 
                                {'label': 'Uplifted', 'value': 'Uplifted'}, 
                                {'label': 'Sleepy', 'value': 'Sleepy'}, 
                                {'label': 'Creative', 'value': 'Creative'},
                                {'label': 'Energetic', 'value': 'Energetic'}, 
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
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button('Submit', id='Submit', color='primary', n_clicks=0),
                    ]
                ),
                html.Div(id='output', className='lead')
            ]
        )
    ]
)

layout = row

df = pd.read_csv('https://raw.githubusercontent.com/kushyapp/cannabis-dataset/master/Dataset/Strains/strains-kushy_api.2017-11-14.csv', index_col='id')
df = df[['status', 'name', 'type', 
         'breeder','effects','ailment',
         'flavor','thc','thca','cbd','cbda']]
df = df[df['effects'].notna()]
df = df[df['ailment'].notna()]

knn = pickle.load(open('model.pkl', 'rb'))

tfidf = pickle.load(open('tfidf.pkl', 'rb'))

@app.callback(
    Output('output', 'children'),
    [Input('Submit', 'n_clicks')],
    [
        State("ctype", "value"),
        State("effects", "value"),
        State("ailment", "value"),
        State("flavor", "value"),
    ],
)

def recommender(n_clicks, input1, input2, input3, input4):
    if n_clicks:
        x = pd.DataFrame(columns=df.columns)
        text = []
        for i in [input1, input2, input3, input4]:
            if i is None:
                pass
            elif type(i) == str:
                text.append(i)
            else:
                text = text + list(i)
        if text == []:
            return "You need to put something in"
        input_features = tfidf.transform(text)
        for i in knn.kneighbors(input_features, n_neighbors=5, return_distance=False)[0]:
            x = x.append(df.iloc[[i]])
        x = x[['name', 'type', 'effects', 'ailment', 'flavor']]
        x = x.rename(columns={'name': 'Name', 'type': 'Type', 'effects': 'Effects',
                              'ailment': 'Ailment', 'flavor': 'Flavor'})
        
        y = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in x.columns],
            data=x.to_dict('records'),
            style_cell={
                'textAlign': 'left',
                'backgroundColor': 'rgba(50,50,50,0)',
                'color': 'primary',
                'whiteSpace': 'normal',
                'height': '30px',
                'lineHeight': '15px',
                'maxWidth': 400,
            }
        )
        return y

if __name__ == '__main__':
    app.run_server(debug=True)