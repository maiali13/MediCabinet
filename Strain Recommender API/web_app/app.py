from flask import Flask, jsonify, request
import requests

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        x = 400 + 20
        return f"Home Page {x}"

    @app.route("/test")
    def test():
        return f"420"

    @app.route('/predict', methods=['GET'])
    def strain_recommend():
        user_input = request.args.get("user_input")
        # Import data
        resp = requests.get('https://med-cabinet-7.herokuapp.com/api/weed/data')
        data = resp.json()
        # Create and clean df
        df = pd.DataFrame(data)
        df = df.drop(['id'],axis=1)
        df = df[:2351]
        df = df[df["Description"] != ""]
        df = df[df["Description"] != "None"]
        df = df[df["Strain"] != "B-Witched"]
        df = df[df["Strain"] != "Blue-Train"]
        df = df[df["Strain"] != "Grape-Krush"]
        df = pd.DataFrame.reset_index(df, drop = True)
        # Instantiate vectorizer object
        tfidf = TfidfVectorizer(stop_words='english', max_features=1500, max_df=.98, min_df=.02)
        # Create a vocabulary and get word counts per document
        # Similiar to fit_predict, fit dtm to Descriptions column
        dtm = tfidf.fit_transform(df['Description'])
        # Send to the df
        # Get feature names to use as dataframe column headers
        dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
        dtm = dtm.drop(dtm.iloc[:, 0:8], axis=1)
        # Fit on DTM on NN model
        nn = NearestNeighbors(n_neighbors=5, algorithm='kd_tree')
        nn.fit(dtm)
        # Get DTM for the user_input description
        new = tfidf.transform([user_input])
        new = pd.DataFrame(new.todense(), columns=tfidf.get_feature_names())
        new = new.drop(new.iloc[:, 0:8], axis=1)
        # Getting the top 5 results
        top_five = nn.kneighbors(new)[1][0]

        result = []
        for n in top_five:
            result.append(df['Strain'][n])

        return jsonify([result])

    @app.errorhandler(404)
    def page_not_found(error):
        return 'The page you were looking for does not exist', 404

    return app
