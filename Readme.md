The themed link to this repo is: https://southforkresearch.github.io/CHaMP_Metrics/

This repo contains open source scritps for calculating CHaMP metrics from ShapeFile and GeoTIF datasets. See the [wiki](https://github.com/SouthForkResearch/CHaMP_Metrics/wiki) for more information.

It is designed to be used by the CHaMPAutomation script but it can just as easily be run standalone:

<https://riverscapes.github.io/CHaMPAutomation/>

### [Tools](docs/index.md)


### Creating new tools

1. Create a `.py` file for your tools in the `tools` folder

### Templates

The templates folder contains the metric schema definitions for inserting the metrics calculated into the CHaMP API

More about how to use these here:

<https://riverscapes.github.io/CHaMPAutomation/metrics/metricschemaxml.html>


### Testing

Test Data is stored on S3. Check the `scripts` directory for scripts to download / upload it.
