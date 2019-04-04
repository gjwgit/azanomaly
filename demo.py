# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Quick Start published on Azure.

from utils import get_key_endpoint, send_request, ask_continue, inform_about

inform_about("Azure Anomaly Detector", """\
Welcome to a demo of the pre-built model for Anomaly Detection. This Azure
Service supports the identification of anomalies in time series data.
""")

import os
import json
import statistics

# Constants.

SERVICE   = "Anomaly Detector"
KEY_FILE  = os.getcwd() + "/private.txt"
DATA_FILE = "request-data.json"

# URLs for anomaly detection with the Anomaly Detector API.

BATCH_URL  = "/anomalydetector/v1.0/timeseries/entire/detect"
LATEST_URL = "/anomalydetector/v1.0/timeseries/last/detect"

# Request subscription key and endpoint from user.

subscription_key, endpoint = get_key_endpoint(KEY_FILE, SERVICE)

ask_continue()

# Read data from a json time series from file.

inform_about("Sample Data", """\
Here we review the data that we wish to explore for anomalies.""",
             begin="\n")

file_handler = open(DATA_FILE)
data = json.load(file_handler)
series = data['series']

inform_about(text="""
The dataset contains {} {} observations recording the number of requests
received for a particular service. It is quite a small dataset used to 
illustrate the concepts. Below we see sample observations from the dataset.
""".format(len(series), data['granularity']))

print(json.dumps(series[0:2], indent=4), "\n")

ask_continue()

timestamps = [ x['timestamp'] for x in series ]
values     = [ x['value'] for x in series ]

inform_about("", """
The timestamps ranges from {} to {}.
The observations range from {:,} to {:,} with a mean value
{:,} and standard deviation {:,}.
""".format(min(timestamps), max(timestamps),
           min(values), max(values),
           round(statistics.mean(values)),
           round(statistics.pstdev(values))))

# Detect anomalies in the time series.

inform_about("Detecting Anomalies", """\
The data is being sent to the server and the results are being collected.
""")

# Send the request

result = send_request(endpoint, BATCH_URL, subscription_key, data)

expected = result['expectedValues']
anomaly  = result['isAnomaly']
negative = result['isNegativeAnomaly']
positive = result['isPositiveAnomaly']
lower    = result['lowerMargins']
upper    = result['upperMargins']

# Find and display the positions of anomalies in the data set
anomalies = result["isAnomaly"]
inform_about("", """\
Anomalies were detected in the following data positions: 
""", end="\n    ")

for x in range(len(anomalies)):
    if anomalies[x] == True:
        print(x, end=" ")

inform_about("", """\n
For a sample of observations we show the meta data that is used to determine
whether the observation is an anomaly.
""")

for i in [0, 1, 2, 3, 30, 31, 32, 33, 34]: inform_about("", """\
{:2}: {:,} expect {:,} range {:,} to {:,} {}{} {}
""".format(i,
           round(values[i]),
           round(expected[i]),
           round(expected[i]-lower[i]),
           round(expected[i]+upper[i]),
           "positive" if positive[i] else "",
           "negative" if negative[i] else "",
           "anomaly" if anomaly[i] else ""), end="")

ask_continue(begin="\n")

# Detect if the latest data point in the time series is an anomaly.

inform_about("Latest Data Point", """\
A common task is to determine if the latest data point in a time series is an
anomaly. There are many usecases for apps where a series of data is being 
streamed at we are interested to know an anomaly arises, when it arises. 
As data points arrive we can query the service to check if in the context
of the time series data whether this latest observation is an anomaly.
""", begin="\n")

result = send_request(endpoint, LATEST_URL, subscription_key, data)
print(json.dumps(result, indent=4))

# Generate a plot to show the time series and the anomalies.

