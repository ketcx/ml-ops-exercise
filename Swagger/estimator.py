import subprocess as sb
import sys

sb.call([sys.executable, "-m", "pip", "install", "nltk"])

import argparse
import os
import pandas as pd
import numpy as np
import string
import nltk # Natural Language tool kit
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import json
from sklearn.pipeline import Pipeline

nltk.download('stopwords')

INDEX_TO_LABEL = {
    0: 'Positive tweet',
    1: 'Negative tweet'
}

def data_clean(tweet):
    tweet_without_punctuation = [char for char in tweet if char not in string.punctuation]
    tweet_join = ''.join(tweet_without_punctuation)
    tweet_clean = [word for word in tweet_join.split() if word.lower() not in stopwords.words('english')]
    return tweet_clean

if __name__ =='__main__':
    # Create a parser object to collect the environment variables that are in the
    # default AWS Scikit-learn Docker container.
    parser = argparse.ArgumentParser()

    parser.add_argument('--output-data-dir', type=str, default=os.environ.get('SM_OUTPUT_DATA_DIR'))
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    args = parser.parse_args()

    # Load data from the location specified by args.train (In this case, an S3 bucket).
    data = pd.read_csv(os.path.join(args.train,'train.csv'), index_col=0, engine="python")

    # Vectorizer twets
    vectorizer = CountVectorizer(analyzer=data_clean)
    tweets_countvectorizer = vectorizer.fit_transform(data['tweet'])

    # Seperate input variables and labels.
    train_X = pd.DataFrame(tweets_countvectorizer.toarray())
    train_Y = data[['label']]

    #Train the logistic regression model using the fit method
    model = MultinomialNB().fit(train_X, train_Y.values.ravel())

    #Save the model to the location specified by args.model_dir
    joblib.dump(vectorizer, os.path.join(args.model_dir, "model_vectorizer.joblib"))
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))

def data_clean(tweet):
    tweet_without_punctuation = [char for char in tweet if char not in string.punctuation]
    tweet_join = ''.join(tweet_without_punctuation)
    tweet_clean = [word for word in tweet_join.split() if word.lower() not in stopwords.words('english')]
    return tweet_clean


"""
model_fn
    model_dir: (sting) specifies location of saved model

This function is used by AWS Sagemaker to load the model for deployment. 
It does this by simply loading the model that was saved at the end of the 
__main__ training block above and returning it to be used by the predict_fn
function below.
"""
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model

"""
input_fn
    request_body: the body of the request sent to the model. The type can vary.
    request_content_type: (string) specifies the format/variable type of the request
"""
def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':

        input_json = request_body
        input_json = json.dumps(input_json['input'])
        input_df = pd.read_json(input_json, orient='list')

        vectorizer = joblib.load(os.path.join(model_dir, "model_vectorizer.joblib"))
        tweets_countvectorizer = vectorizer.fit_transform(data['tweet'])

        return tweets_countvectorizer
    else:
        raise ValueError("Thie model only supports text/csv input")

"""
predict_fn
    input_data: (numpy array) returned array from input_fn above 
    model (sklearn model) returned model loaded from model_fn above
"""
def predict_fn(input_data, model):
    return model.predict(input_data)

"""
output_fn
    prediction: the returned value from predict_fn above
    content_type: (string) the content type the endpoint expects to be returned
"""
def output_fn(prediction, content_type):
    result = {'output': []}
    list_out = []
    label = [INDEX_TO_LABEL[t] for t in prediction]
    list_out.append({'label': label})

    result['output'] = list_out
    result = json.dumps(result)

    return result