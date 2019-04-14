# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Quick Start published on Azure.

from mlhub.pkg import get_key_endpoint, send_request, ask_continue, inform_about

inform_about("Azure Anomaly Detector", """\
Welcome to a demo of the pre-built model for Anomaly Detection. This Azure
Service supports the identification of anomalies in time series data.
""")

import os
import json
import statistics
from textwrap import fill

# Constants.

SERVICE   = "Anomaly Detector"
KEY_FILE  = os.getcwd() + "/private.txt"
DATA_FILE = "request.json"

# URLs for anomaly detection with the Anomaly Detector API.

BATCH_URL  = "/anomalydetector/v1.0/timeseries/entire/detect"
LATEST_URL = "/anomalydetector/v1.0/timeseries/last/detect"

# Request subscription key and endpoint from user.

subscription_key, endpoint = get_key_endpoint(KEY_FILE, SERVICE)

ask_continue()

# Read data from a json time series from file.

file_handler = open(DATA_FILE)
data = json.load(file_handler)
series = data['series']
sensitivity = data['sensitivity']

inform_about("Sample Data", """\
The dataset contains {} {} observations recording the number of requests
received for a particular service. It is quite a small dataset used to 
illustrate the concepts. Below we see sample observations from the dataset.
""".format(len(series), data['granularity']), begin="\n")

print(json.dumps(series[0:2], indent=4))

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

ask_continue()

# Detect anomalies in the time series.

inform_about("Detecting Anomalies", """\
The data is being sent to the server and the results are being collected.
A sensitivity of {} was specified in the data to increase the boundary 
beyond which observations are regarded as an outlier. The default 
sensitivity is 99.
""".format(sensitivity), begin="\n")

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

anom = " "
count = 0
for x in range(len(anomalies)):
    if anomalies[x] == True:
        anom += "{} ".format(x)
        count += 1
inform_about("", """\
There were {} anomalies detected at the following data positions: 
""".format(count))
print(fill(anom, initial_indent="     ", subsequent_indent="    "))

inform_about("", """
For a sample of anomalies we show the meta data that is used to determine
the observation is an anomaly.
""")

for i in [21, 22, 23, 30, 31, 32, 44]: inform_about("", """\
{:2}: {:,} expect {:,} range {:,} to {:,} {}{} {}
""".format(i,
           round(values[i]),
           round(expected[i]),
           round(expected[i]-lower[i]),
           round(expected[i]+upper[i]),
           "positive" if positive[i] else "",
           "negative" if negative[i] else "",
           "anomaly" if anomaly[i] else ""), end="")

f = open("request-anom.csv", "w")
f.write("timestamp,value,expected,from,to,anomaly\n")
for i in range(len(anomalies)):
    f.write("{},{},{},{},{},{}\n".format(timestamps[i],
                                         round(values[i]),
                                         round(expected[i]),
                                         round(expected[i]-lower[i]),
                                         round(expected[i]+upper[i]),
                                         "TRUE" if anomaly[i] else "FALSE"))
f.close()
os.system("Rscript request-anom.R > /dev/null 2>&1")
ask_continue(begin="\n")

# Detect if the latest data point in the time series is an anomaly.

inform_about("Latest Data Point", """\
A common task is to determine if the latest data point in a time series is an
anomaly. There are many usecases for apps where a series of data is being 
streamed.  We are interested to know of an anomaly, when it arises. 
As data points arrive we can query the service to check if in the context
of the time series data whether this latest observation is an anomaly.
""", begin="\n")

result = send_request(endpoint, LATEST_URL, subscription_key, data)
print(json.dumps(result, indent=4))

ask_continue(begin="\n")

# Generate a plot to show the time series and the anomalies.

inform_about("Visualising the Anomalies", """\
We now plot the original data overlayed on the expected values which represent
a range of values within which we expect the actual value to be. The expected
range is the shaded area. The actual values are plotted as the blue line, and
the identified anomalies are shown in red.
""", begin="\n")

os.system("atril --preview request-anom.pdf")

print("Press Ctrl-w to close the graphics window.\n")

ask_continue()

# We now repeat this for the rattle download data.

DATA_FILE = "rattle.json"

# Read data from a json time series from file.

inform_about("Rattle Data", """\
We now replicate the same process but with a larger dataset. The rattle
download data records the number of downloads of the rattle package for
R from one of the archive nodes on CRAN. We demonstrate anomaly detection
using this dataset.
""", begin="\n")

ask_continue("Now to review the data. ")

file_handler = open(DATA_FILE)
data = json.load(file_handler)
series = data['series']
sensitivity = data['sensitivity']

inform_about(text="""
The dataset contains {:,} {} observations recording the number of downloads.
Below we share some sample observations.
""".format(len(series), data['granularity']))

print(json.dumps(series[0:2], indent=4), "\n")

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

ask_continue()

# Detect anomalies in the time series.

inform_about("Detecting Anomalies", """\
The data is being sent to the server and the results are being collected.
A sensitivity of {} was specified in the data to increase the boundary 
beyond which observations are regarded as an outlier. The default 
sensitivity is 99.
""".format(sensitivity), begin="\n")

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

anom = ""
count = 0
for x in range(len(anomalies)):
    if anomalies[x] == True:
        anom += "{} ".format(x)
        count += 1
inform_about("", """\
There were {} anomalies detected at the following data positions: 
""".format(count))
print(fill(anom, initial_indent="     ", subsequent_indent="    "))

inform_about("", """
For a sample of anopmalies we show the meta data that is used to determine
the observation as an anomaly.
""")

for i in [630, 685, 925, 964, 1038, 1039, 2276]: inform_about("", """\
{:4}: {:3} expect {:,} range {:,} to {:,} {}{} {}
""".format(i,
           round(values[i]),
           round(expected[i]),
           round(expected[i]-lower[i]),
           round(expected[i]+upper[i]),
           "positive" if positive[i] else "",
           "negative" if negative[i] else "",
           "anomaly" if anomaly[i] else ""), end="")

f = open("rattle-anom.csv", "w")
f.write("timestamp,value,expected,from,to,anomaly\n")
for i in range(len(anomalies)):
    f.write("{},{},{},{},{},{}\n".format(timestamps[i],
                                         round(values[i]),
                                         round(expected[i]),
                                         round(expected[i]-lower[i]),
                                         round(expected[i]+upper[i]),
                                         "TRUE" if anomaly[i] else "FALSE"))
f.close()
os.system("Rscript rattle-anom.R > /dev/null 2>&1")
ask_continue(begin="\n")

# Detect if the latest data point in the time series is an anomaly.

inform_about("Latest Data Point", """\
A common task is to determine if the latest data point in a time series is an
anomaly. There are many usecases for apps where a series of data is being 
streamed.  We are interested to know of an anomaly, when it arises. 
As data points arrive we can query the service to check if in the context
of the time series data whether this latest observation is an anomaly.
""", begin="\n")

result = send_request(endpoint, LATEST_URL, subscription_key, data)
print(json.dumps(result, indent=4))

ask_continue(begin="\n")

# Generate a plot to show the time series and the anomalies.

inform_about("Visualising the Anomalies", """\
We now plot the original data overlayed on the expected values which represent
a range of values within which we expect the actual value to be. The expected
range is the shaded area (though not particularly visible in this plot). The
actual values are plotted as the blue line, and the identified anomalies are
shown in red.
""", begin="\n")

ask_continue()

print("\nPress Ctrl-w to close the graphics window.")

os.system("atril --preview rattle-anom.pdf")
