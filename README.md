
# About

Our app helps patients find the right medical cannabis strains with a Machine Learning model that takes in user data and strain data to produce recommendations.

# How-to

1. Fork this repository to your GitHub account and then clone it onto your local machine.

2. From your terminal, enter the directory "Plotly-Dash" (or whatever you called your cloned repository).

3. "pipenv install" will automatically install all the dependencies from the Pipfile.

4. "pipenv shell" will start up your virtual environment.

5. Open the repository on your preferred IDE and poke around in the code.

6. If you want full functionality, you will need to obtain a Google Maps API key. 
https://developers.google.com/maps/documentation/embed/get-api-key

6a. Open a Google Cloud Platform account if you do not already have one.

6b. Create a new project (e.g. "Med Cabinet")

6c. Go to the APIs & Services > Credentials page to create an API key.

6d. From the Credentials page, click "edit" on your API key, and select "Restrict Key". 
Choose "Maps Embed API" under "Selected APIs" and save your settings.

6e. To run the app on your local machine, create a .env file in your Plotly-Dash repository.
Save your API key as a string to a variable called API_key.

6f. To run the app on a site like Heroku, you will need to go to that website's settings
for configuration variables and create a new variable called API_key.

7. To run the app on your local machine, make sure you are in your virtual environment and run
the command "python run.py" from your terminal.

# Dash Template

[Instructions](https://lambdaschool.github.io/ds/unit2/dash-template/)

If you want to play around with the formatting, here's the [relevant documentation for Dash bootstrap components](https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout)

# Product Vision Document: 

[Read our PVD here](https://docs.google.com/document/d/1W5DvYxZ7w0BRVx2edskghjsFW5Ri7QgLCNCMGmcm9vA/)

