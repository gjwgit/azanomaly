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

- To install mlhub 

```shell
$ pip3 install mlhub
```

- To install and run the pre-built model:

```shell
$ ml install   azanomaly
$ ml configure azanomaly
$ ml demo      azanomaly

Demonstration
-------------

```console
$ ml demo azanomaly
=======================
Azure Anomaly Detection
=======================
```

