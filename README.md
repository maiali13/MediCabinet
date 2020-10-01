# MediCabinet
## A Medical Marijuana Strain Recommender

This ia a small back-end Flask API model providing marijuana strain recommendations for the MediCabinet project, based on desired effects and ailments to be treated. K-Nearest-Neighbor model takes a pandas series holding user input regarding their cannabis strain preferences, and outputs a raw JSON array containing the most similar strains in the database.

# Strain Recommender API 

## Usage

Submit a GET request to https://cannapi.herokuapp.com/predict with text describing the type of high the user is seeking. 

for example: 
    https://cannapi.herokuapp.com/predict?user_input=%22appetite%20blueberry%20taste%20sweetness%20treat%20soul%20mind%22

This will return the top 5 strains matching the user's desired  effects from their medical cannabis. 

## Installation

This app can be run locally via ```FLASK_APP=web_app flask run``` after setting up a local environment and installing the required dependencies. 



