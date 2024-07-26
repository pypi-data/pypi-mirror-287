[![DOI](https://zenodo.org/badge/199771667.svg)](https://zenodo.org/doi/10.5281/zenodo.10152905)

![PyKOSMOS logo](pykosmos.png)

An easy to use reduction package for one-dimensional longslit spectroscopy. 

## Installation
The easiest way to install is via [pip](https://pypi.org/project/pykosmos/):
````
pip install pykosmos
````


## Goals
This tool *should* be able to handle 90% of basic reduction needs from a longslit-style spectrograph.... there are many other smaller or more subtle goals for this project that will be outlined here.

There needs to be many worked examples available.


## Motivation
We need simple to use, standalone reduction tools that can handle most tasks automatically.

The predecessor was [PyDIS](https://github.com/StellarCartography/pydis), a semi-complete standalone reduction suite in Python that has been used for many instruments and [publications](https://ui.adsabs.harvard.edu/abs/2016zndo.....58753D/abstract) so far! Since then, many [astropy](https://www.astropy.org) components have advanced to better handle the tasks PyDIS attempted, including  [specreduce](https://github.com/astropy/specreduce) that has inherited methods and workflow structure from PyDIS and PyKOSMOS.

My [original blog post](https://jradavenport.github.io/2015/04/01/spectra.html) on the topic from 2015 still largely stands.

## Related Links
* [PyKOSMOS](https://github.com/jradavenport/pykosmos/) on GitHub
* [dtw_identify](https://github.com/jradavenport/dtw_identify/), automatic wavelength calibration using Dynamic Time Warping, developed in PyKOSMOS
* [kosmos-arc](https://github.com/jradavenport/kosmos-arc), a library of calibrated arc lamp templates for KOSMOS at APO
* [KOSMOS](https://www.apo.nmsu.edu/arc35m/Instruments/KOSMOS/) instrument page at APO
* [PyDIS](https://github.com/StellarCartography/pydis), the predecessor.
