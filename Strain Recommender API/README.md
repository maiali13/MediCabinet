# Strain Recommender API 

## Usage

Submit a GET request to https://cannapi.herokuapp.com/predict with text describing the type of high the user is seeking. 

for example: 
    https://cannapi.herokuapp.com/predict?user_input=%22appetite%20blueberry%20taste%20sweetness%20treat%20soul%20mind%22

This will return the top 5 strains matching the user's desired  effects from their medical cannabis. 

## Installation

This app can be run locally via ```FLASK_APP=web_app flask run``` after setting up a local environment and installing the required dependencies. 



