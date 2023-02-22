<p align="center"><img src="https://raw.githubusercontent.com/cgre-aachen/gemgis/main/docs/getting_started/images/Modern1.png" width="600">

> Spatial data and information processing for geomodeling


[![PyPI](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)
![PyPI](https://img.shields.io/pypi/v/gemgis_data)
![Conda](https://img.shields.io/conda/vn/conda-forge/gemgis_data)
![GitHub](https://img.shields.io/github/license/cgre-aachen/gemgis_data)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cgre-aachen/gemgis/main)
![Read the Docs](https://img.shields.io/readthedocs/gemgis)
[![DOI](https://img.shields.io/badge/DOI-https%3A%2F%2Fdoi.org%2F10.5194%2Fegusphere--egu21--4613-blue)](https://doi.org/10.5194/egusphere-egu21-4613)
[![DOI](https://zenodo.org/badge/309125606.svg)](https://zenodo.org/badge/latestdoi/309125606)

<p align="center"><img src="https://raw.githubusercontent.com/cgre-aachen/gemgis/main/docs/getting_started/images/task1.png" width="200"><img src="https://raw.githubusercontent.com/cgre-aachen/gemgis/main/docs/getting_started/images/model1.png" width="300"></p>

## Overview 

This repository provides the notebooks and data to the [example models](https://gemgis.readthedocs.io/en/latest/getting_started/example/index.html) of GemGIS and GemPy. It is set up as course adapted from two Bachelor courses at RWTH Aachen University, Germany ([Geological methods and geological map](https://www.rwth-aachen.de/cms/root/studium/Vor-dem-Studium/Studiengaenge/Liste-Aktuelle-Studiengaenge/Studiengangbeschreibung/~bqxx/Angewandte-Geowissenschaften-B-Sc/?lidx=1) & [Introduction to geological maps](https://www.rwth-aachen.de/cms/root/studium/Vor-dem-Studium/Studiengaenge/Liste-Aktuelle-Studiengaenge/Studiengangbeschreibung/~bllm/Georessourcenmanagement-B-Sc/?lidx=1)). The course contains the following sections:

1. [Introduction to structural geological modeling using GemPy and GemGIS](#introduction-to-structural-geological-modeling-using-gempy-and-gemgis)
    1. [Introdurction to structural geological models](#introduction-to-structural-geological-models)
    2. [Introduction to GemPy and GemGIS](#introduction-to-gempy-and-gemgis)
    3. [Resources for GemPy and GemGIS](#resources-for-gemgis-gempy)
    4. [Installation of GemPy and GemGIS](#installation-of-gempy-and-gemgis)
2. Modeling of the basic structures in GemPy
    1. Modeling planar layers
    2. Modeling folded layers
    3. Modeling faulted layers
    4. Modeling truncated/unconformal layers
3. Modeling of more complex models including additional tasks (main part)
4. Post-processing of structural geological models using GemGIS

For more information about GemGIS and GemPy see the dedicated Github Repositories and Documentation pages:
- [GemGIS Repository](https://github.com/cgre-aachen/gemgis)
- [GemGIS Installation & Docs](https://gemgis.readthedocs.io/en/latest/getting_started/installation.html)
- [GemPy Repository](https://github.com/cgre-aachen/gempy)
- [GemPy Installation & Docs](https://www.gempy.org/installation)

## Purpose of structural geological models in Earth Sciences

Structural geological models describe the spatial distribution of layers in the subsurface. This includes the extent and depth distribution of either lithological layers (e.g. sand or clay, sandstones, carbonates, evaporites, etc.) or stratigraphic units for more regional questions of the structure of the subsurface (e.g. Base Tertiary, transition to basement rocks, etc.). The resulting structures can be used to parametrize the rocks between these constructed bounding surfaces for a wide range of applications. These include but are not limited to hydrogeological applications, geohazards, ressource extraction (e.g. fresh water, thermal waters, hydrocarbons, minerals), storage applications (e.g. thermal waters, gases such as CO2 or hydrogen, nuclear waste). 




## Target Audience

The tutorials provided in this repository aim at enabling students who want to become familiar with structural geological modeling in GemPy to have a smooth start. Further, the tutorials serve as aids for researchers to set up and parametrize their structural geological models properly. Lectures are encouraged to use and adapt the provided tutorials for their own Python and Structural Geological Modeling classes. 

## Dependencies

The GemGIS package mainly depends on [GeoPandas/Pandas](https://geopandas.org/en/stable/index.html), [Rasterio](https://rasterio.readthedocs.io/en/latest/) and [PyVista](https://docs.pyvista.org/). All geometric operations are performed using [Shapely](https://shapely.readthedocs.io/en/stable/manual.html). Numerical operations are performed using [NumPy](https://numpy.org/doc/stable/index.html) while plotting is done with [Matplotlib](https://matplotlib.org/). The structural modeling package [GemPy](https://www.gempy.org) is an optional dependency but is required to build the structural geological models. 

<a name="ref"></a>
## References

* Jüstel, A., Endlein Correira, A., Wellmann, F. and Pischke, M.: GemGIS – GemPy Geographic: Open-Source Spatial Data Processing for Geological Modeling. EGU General Assembly 2021, https://doi.org/10.5194/egusphere-egu21-4613, 2021
* Jüstel, A.: 3D Probabilistic Modeling and Data Analysis of the Aachen-Weisweiler Area: Implications for Deep Geothermal Energy Exploration, unpublished Master Thesis at RWTH Aachen University, 2020
* de la Varga, M., Schaaf, A., and Wellmann, F.: GemPy 1.0: open-source stochastic geological modeling and inversion, Geosci. Model Dev., 12, 1-32, https://doi.org/10.5194/gmd-12-1-2019, 2019
* Powell, D.: Interpretation of Geological Structures Through Maps: An Introductory Practical Manual, Longman, pp. 192, 1992
* Bennison, G.M.: An Introduction to Geological Structures and Maps, Hodder Education Publication, pp. 78, 1990
