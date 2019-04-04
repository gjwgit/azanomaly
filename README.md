Azure Anomaly Detection
=======================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the pre-built Anomaly Detection model provided through Azure's
Cognitive Services. This service identifies anomalies in time series
data.

A free Azure subscription allowing up to 20,000 calls per month is
available from https://azure.microsoft.com/free/. Once set up visit
https://ms.portal.azure.com and Create a resource under AI and Machine
Learning called Anomaly Detection. Once created you can access the web
API subscription key and endpoint from the portal. This will be
prompted for in the demo.

Please note that this is *closed source software* which limits your
freedoms and has no guarantee of ongoing availability.

Visit the github repository for more details:
<https://github.com/gjwgit/azanomaly>

The Python code is based on the [Quickstart: Detect anomalies in your
time series data using the Anomaly Detector REST API and
Python](https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/quickstarts/detect-data-anomalies-python)

Usage
-----

- To install mlhub (e.g., on Ubunut 18.04 LTS)

```shell
$ pip3 install mlhub
```

- To install and run the demo:

```shell
$ ml install   azanomaly
$ ml configure azanomaly
$ ml demo      azanomaly
```

Demonstration
-------------

```console
$ ml demo azanomaly
======================
Azure Anomaly Detector
======================

Welcome to a demo of the pre-built model for Anomaly Detection. This Azure
Service supports the identification of anomalies in time series data.

The following file has been found and is assumed to contain an Azure 
subscription key and endpoint for Anomaly Detector. We will load 
the file and use this information.

    /home/gjw/.mlhub/azanomaly/private.txt

Press Enter to continue: 

===========
Sample Data
===========

Here we review the data that we wish to explore for anomalies.

The dataset contains 47 daily observations recording the number of requests
received for a particular service. It is quite a small dataset used to 
illustrate the concepts. Below we see sample observations from the dataset.

[
    {
        "timestamp": "2018-03-01T00:00:00Z",
        "value": 32858923
    },
    {
        "timestamp": "2018-03-02T00:00:00Z",
        "value": 29615278
    }
] 

Press Enter to continue: 

The timestamps ranges from 2018-03-01T00:00:00Z to 2018-04-16T00:00:00Z.
The observations range from 21,244,209 to 38,144,434 with a mean value
30,379,943 and standard deviation 4,651,713.

===================
Detecting Anomalies
===================

The data is being sent to the server and the results are being collected.

Anomalies were detected in the following data positions: 

    3 18 21 22 23 24 25 28 29 30 31 32 35 44 

For a sample of observations we show the meta data that is used to determine
whether the observation is an anomaly.

 0: 32,858,923 expect 32,894,419 range 32,565,475 to 33,223,363  
 1: 29,615,278 expect 29,707,932 range 29,410,853 to 30,005,012  
 2: 22,839,355 expect 22,651,867 range 22,425,348 to 22,878,386  
 3: 25,948,736 expect 24,943,248 range 24,693,816 to 25,192,680 positive anomaly
30: 21,244,209 expect 22,473,094 range 22,248,363 to 22,697,825 negative anomaly
31: 22,576,956 expect 24,813,478 range 24,565,344 to 25,061,613 negative anomaly
32: 31,957,221 expect 34,017,256 range 33,677,083 to 34,357,428 negative anomaly
33: 33,841,228 expect 33,864,058 range 33,525,418 to 34,202,699  
34: 33,554,483 expect 33,577,520 range 33,241,744 to 33,913,295  

Press Enter to continue: 

=================
Latest Data Point
=================

A common task is to determine if the latest data point in a time series is an
anomaly. There are many usecases for apps where a series of data is being 
streamed.  We are interested to know of an anomaly, when it arises. 
As data points arrive we can query the service to check if in the context
of the time series data whether this latest observation is an anomaly.

{
    "expectedValue": 35344244.421857625,
    "isAnomaly": false,
    "isNegativeAnomaly": false,
    "isPositiveAnomaly": false,
    "lowerMargin": 353442.44421857625,
    "period": 7,
    "suggestedWindow": 29,
    "upperMargin": 353442.44421857625
}

Press Enter to continue: 

=========================
Visualising the Anomalies
=========================

We now plot the original data overlayed on the expected values which represent
a range of values within which we expect the actual value to be. The expected
range is the shaded area. The actual values are plotted as the blue line, and
the identified anomalies are shown in red.
```
![alt
text](request-data.png "Actual Values versus Range of Expected Values")

```console
Thank you for exploring the 'azanomaly' package.
```

