"""Brief descriptions and social media links for the team"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

column1 = dbc.Col(html.Div(
    [
        dcc.Markdown(
            """
            # Meet the team
            **Hunter Ashby** went into data science right after high school, and loves theorizing about things with data.  [![email Hunter](/assets/email_icon_3.png)](mailto:hunter.ashby19@gmail.com) [![Hunter's GitHub](/assets/github_icon.png)](https://github.com/HunterAshby)

            &nbsp;  

            **Elizabeth Edwards-Appell** is a full-time data science student at Lambda School with policy experience and an enthusiasm for effective philanthropy. Her blog is [here](https://eedwardsa.github.io/).  [![email Elizabeth](/assets/email_icon_3.png)](mailto:ecomstockedwards@gmail.com) [![Elizabeth's GitHub](/assets/github_icon.png)](https://github.com/EEdwardsA) [![Elizabeth's LinkedIn](/assets/linkedin_icon.png)](https://www.linkedin.com/in/elizabeth-edwards-appell-62398b15/)

            """
        ),
    ]
)
)

column2 = dbc.Col((html.Img(src='assets/TeamCollage.png', style={'width':'100%',
                                                                 'position':'relative',
                                                                 'top':'20%',
                                                                 'bottom':'50%'
                                                                  })))

column3 = dbc.Col(html.Div(
    [
        dcc.Markdown(
            """       
            &nbsp;     
            &nbsp;                    

            **Leo Nealon** is a data science student at Lambda School excited to break into the quantitative finance industry. His blog is [here](https://leonealon.medium.com/).  [![email Leo](/assets/email_icon_3.png)](mailto:nealonleo9@gmail.com) [![Leo's GitHub](/assets/github_icon.png)](https://github.com/nealonleo9) 
            
            &nbsp;  

            **Rassamy "Jack" Soumphonphakdy** is a full-time data science student at Lambda School with dreams of relocating to Virginia.  [![email Jack](/assets/email_icon_3.png)](mailto:jacksoumphonphakdy@gmail.com) [![Jack's GitHub](/assets/github_icon.png)](https://github.com/rassamyjs) 


            """
        ),
    ],
))

layout = html.Div(
    [
        dbc.Row(
            [
                column1, 
                column2, 
                column3
            ]
        ),
    ]
)