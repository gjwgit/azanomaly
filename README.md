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

- To install mlhub (Ubuntu 18.04 LTS)

  ```shell
  $ pip3 install mlhub
  ```

- To install and configure the demo:

  ```shell
  $ ml install   azanomaly
  $ ml configure azanomaly
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

An Azure resource is required to access this service (and to run this command).
See the README for details of a free subscription. If you have a subscription
then please paste the key and the endpoint here.

Please paste your Anomaly Detector subscription key: ********************************
Please paste your endpoint: https://westus2.api.cognitive.microsoft.com

I've saved that information into the file:

    /home/kayon/.mlhub/azanomaly/private.txt

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
A sensitivity of 95 was specified in the data to increase the boundary 
beyond which observations are regarded as an outlier. The default 
sensitivity is 99.

Anomalies were detected in the following data positions: 

    21 22 23 28 29 30 31 32 44 

For a sample of anomalies we show the meta data that is used to determine
the observation is an anomaly.

21: 38,144,434 expect 33,381,055 range 31,712,002 to 35,050,108 positive anomaly
22: 34,662,949 expect 30,169,004 range 28,660,554 to 31,677,454 positive anomaly
23: 24,623,684 expect 23,087,374 range 21,933,005 to 24,241,743 positive anomaly
30: 21,244,209 expect 22,473,094 range 21,349,439 to 23,596,749 negative anomaly
31: 22,576,956 expect 24,813,478 range 23,572,804 to 26,054,152 negative anomaly
32: 31,957,221 expect 34,017,256 range 32,316,393 to 35,718,119 negative anomaly
44: 22,504,059 expect 23,773,788 range 22,585,099 to 24,962,477 negative anomaly

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
    "lowerMargin": 1767212.2210928812,
    "period": 7,
    "suggestedWindow": 29,
    "upperMargin": 1767212.2210928812
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
text](request-anom.png "Actual Values versus Range of Expected Values")

```console
===========
Rattle Data
===========

The rattle download data is now used for anomaly detection.

We again begin with a review of the data.

The dataset contains 2286 daily observations recording the number of downloads
of the rattle package for R from a CRAN node. This is quite a larger dataset
and demonstrates a more relaistic scneario. Below we share some sample
observations from the dataset.

[
    {
        "timestamp": "2013-01-01",
        "value": 8
    },
    {
        "timestamp": "2013-01-02",
        "value": 21
    }
] 

Press Enter to continue: 

The timestamps ranges from 2013-01-01 to 2019-04-05.
The observations range from 0 to 1,456 with a mean value
356 and standard deviation 250.

===================
Detecting Anomalies
===================

The data is being sent to the server and the results are being collected.
A sensitivity of 95 was specified in the data to increase the boundary 
beyond which observations are regarded as an outlier. The default 
sensitivity is 99.

Anomalies were detected in the following data positions: 

    630 685 925 964 979 981 1020 1028 1033 1034 1038 1039 1043 1048 1120 1121 1128 1144 1248 1258 1288 1300 1311 1318 1320 1321 1327 1340 1347 1402 1427 1428 1429 1472 1479 1483 1512 1520 1528 1552 1575 1593 1594 1597 1602 1603 1610 1633 1640 1656 1657 1659 1660 1668 1699 1704 1705 1708 1709 1710 1713 1720 1727 1740 1741 1747 1749 1750 1752 1755 1761 1762 1766 1768 1769 1780 1784 1791 1802 1803 1808 1809 1830 1848 1865 1866 1877 1878 1879 1880 1882 1901 1924 1925 1926 1939 1951 1957 1964 1972 1989 2013 2014 2034 2040 2068 2118 2119 2121 2140 2143 2149 2160 2163 2164 2165 2201 2208 2218 2248 2249 2253 2260 2274 2276 2280 

For a sample of anopmalies we show the meta data that is used to determine
the observation as an anomaly.

 630:  21 expect 249 range 199 to 299 negative anomaly
 685:   0 expect 225 range 180 to 270 negative anomaly
 925: 527 expect 326 range 261 to 391 positive anomaly
 964:   0 expect 225 range 180 to 270 negative anomaly
1038: 694 expect 380 range 304 to 456 positive anomaly
1039: 565 expect 359 range 287 to 431 positive anomaly
2276: 885 expect 619 range 495 to 742 positive anomaly

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
    "expectedValue": 645.2996719661152,
    "isAnomaly": false,
    "isNegativeAnomaly": false,
    "isPositiveAnomaly": false,
    "lowerMargin": 129.05993439322302,
    "period": 7,
    "suggestedWindow": 29,
    "upperMargin": 129.05993439322302
}

Press Enter to continue: 

=========================
Visualising the Anomalies
=========================

We now plot the original data overlayed on the expected values which represent
a range of values within which we expect the actual value to be. The expected
range is the shaded area (though not particularly visible in this plot). The
actual values are plotted as the blue line, and the identified anomalies are
shown in red.
```
![alt
text](rattle-anom.png "Actual Values versus Range of Expected Values")


```console
Thank you for exploring the 'azanomaly' package.
```

