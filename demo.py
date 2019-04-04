# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import requests
import json
import os

from utils import get_key_endpoint

# Constants

SERVICE   = "Anomaly Detector"
KEY_FILE  = os.getcwd() + "/private.txt"
DATA_FILE = "request-data.json"

# URLs for anomaly detection with the Anomaly Detector API.

BATCH_URL  = "/anomalydetector/v1.0/timeseries/entire/detect"
LATEST_URL = "/anomalydetector/v1.0/timeseries/last/detect"

# Request subscription key and endpoint from user.

subscription_key, endpoint = get_key_endpoint(KEY_FILE, SERVICE)

# Send a request.

def send_request(endpoint, url, subscription_key, request_data):
    """Send anomaly detection request to the Anomaly Detector API. 

    If the request is successful, the JSON response is returned.
    """
    
    headers = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': subscription_key}
    
    response = requests.post(endpoint+url,
                             data=json.dumps(request_data),
                             headers=headers)
    
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print(response.status_code)
        raise Exception(response.text)

# Detect anomalies in the time series.
    
def detect_batch(request_data):
    print("Detecting anomalies as a batch")
    # Send the request, and print the JSON result
    result = send_request(endpoint, BATCH_URL, subscription_key, request_data)
    print(json.dumps(result, indent=4))

    # Find and display the positions of anomalies in the data set
    anomalies = result["isAnomaly"]
    print("Anomalies detected in the following data positions:")

    for x in range(len(anomalies)):
        if anomalies[x] == True:
            print (x)

# Detect if the latest data point in the time series is an anomaly.

def detect_latest(request_data):
    print("Determining if latest data point is an anomaly")
    # send the request, and print the JSON result
    result = send_request(endpoint, LATEST_URL, subscription_key, request_data)
    print(json.dumps(result, indent=4))


# Read data from a json time series from file.

file_handler = open(DATA_FILE)
json_data = json.load(file_handler)

# Send the requests.

detect_batch(json_data)
detect_latest(json_data)

# Generate a plot to show the time series and the anomalies.

