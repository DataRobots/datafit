# Libraries
import os
import json
import io
import re
import pandas as pd
import numpy as np

from flask import Flask, request, redirect, url_for, jsonify,render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Uploads'

model = None
graph = None


# def load_model():
#     global model
#     global graph
#     model = LinearRegression()
#     graph = K.get_session().graph


# load_model()

@app.route("/",methods=['GET', 'POST'])
def index():

    data = {"success": False}

    if request.method == 'POST':
        if request.files.get('file'):
                # read the file
            file = request.files['file']
            
                # read the filename , create a path to the uploads folder
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

                # read column names from the uploaded file
            uploaded_file = pd.read_csv(filepath, encoding="ISO-8859-1")
            column_names = list(uploaded_file.columns.values)
            
                # write column names to data dictionary, indicate that the request was a success
            data["column_names"] = column_names
            data["success"] = True

        return jsonify(data)

        """Return the homepage."""
    return render_template("index1.html")

# route to read columns from the uploaded file

# @app.route('/column_names', methods=['GET', 'POST'])
# def upload_file():

#     data = {"success": False}
#     if request.method == 'POST':
#         if request.files.get('file'):
#                 # read the file
#             file = request.files['file']

#                 # read the filename , create a path to the uploads folder
#             filename = file.filename
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)

#                 # read column names from the uploaded file
#             uploaded_file = pd.read_csv(filepath, encoding="ISO-8859-1")
#             column_names = list(uploaded_file.columns.values)
            
#                 # write column names to data dictionary, indicate that the request was a success
#             data["column_names"] = column_names
#             data["success"] = True

#         return jsonify(data)

    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <p>type=submit value=Upload>
    # </form><input type=file name=file>
    #      <input 
    # '''
# @app.route('/api/train', methods=['POST'])
# def train():
#     # get parameters from request
#     parameters = request.get_json()

#     # read iris data set
#     iris = datasets.load_iris()
#     X, y = iris.data, iris.target

#     # fit model
#     clf = svm.SVC(C=float(parameters['C']),
#                   probability=True,
#                   random_state=1)
#     clf.fit(X, y)

#     # persist model
#     joblib.dump(clf, 'model.pkl')

#     return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


if __name__ == "__main__":
    app.run(debug=True)
