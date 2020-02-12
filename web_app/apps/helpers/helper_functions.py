import numpy as np
import pandas as pd
import dash_html_components as html
import random

df = pd.read_csv(r"D:\Events\VIL Codefest\CustomDash\web_app\appdata\sample_plotting.csv")
tweets_df = pd.read_csv(r"D:\Events\VIL Codefest\CustomDash\web_app\appdata\Tweets.csv")
tweets = list(tweets_df['text'])


def get_location(customer):
    return df.iloc[customer]['Location']


def get_gender(customer):
    return df.iloc[customer]['Gender']


def get_age(customer):
    return df.iloc[customer]['Age']


def get_extended_values(value):
    operation = np.random.randint(0, 2)
    extended_values = []
    if operation:
        for i in range(6):
            i = np.random.randint(0, 100)
            extended_values.append(i + value)
    else:
        for i in range(6):
            i = np.random.randint(0, 100)
            extended_values.append(value - i)
    return extended_values


def get_segment(customer):
    return df.iloc[customer]['Customer Segment']


def get_churn(customer):
    return str(df.iloc[customer]['Churn']) + "%"


def get_tweets():
    a = random.choice(tweets)
    b = random.choice(tweets)
    c = random.choice(tweets)
    d = random.choice(tweets)
    e = random.choice(tweets)
    return html.Div([
        html.P(a, className='tweet'),
        html.P(b, className='tweet'),
        html.P(c, className='tweet'),
        html.P(d, className='tweet'),
        html.P(e, className='tweet'),
    ])