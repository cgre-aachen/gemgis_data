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
Source: Powell, D. (1995): Interpretation geologischer Strukturen durch Karten - Eine praktische Anleitung mit Aufgaben und Lösungen, page 15, figure 10 A, Springer Verlag Berlin, Heidelberg, New York, ISBN: 978-3-540-58607-4.

## Overview 

This repository provides the notebooks and data to the [example models](https://gemgis.readthedocs.io/en/latest/getting_started/example/index.html) of GemGIS and GemPy. It is set up as course adapted from two Bachelor courses at RWTH Aachen University, Germany ([Geological methods and geological map](https://www.rwth-aachen.de/cms/root/studium/Vor-dem-Studium/Studiengaenge/Liste-Aktuelle-Studiengaenge/Studiengangbeschreibung/~bqxx/Angewandte-Geowissenschaften-B-Sc/?lidx=1) & [Introduction to geological maps](https://www.rwth-aachen.de/cms/root/studium/Vor-dem-Studium/Studiengaenge/Liste-Aktuelle-Studiengaenge/Studiengangbeschreibung/~bllm/Georessourcenmanagement-B-Sc/?lidx=1)). The easiest way to access the data is to [download the repository including all data from Github](https://github.com/cgre-aachen/gemgis_data/archive/refs/heads/main.zip). The course contains the following sections:

0. [Introduction to the course](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/00_introduction_to_structural_modeling.ipynb)
1. [Introduction to structural geological modeling using GemPy and GemGIS](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/00_introduction_to_structural_modeling.ipynb)
    1. Introduction to structural geological models
    2. Introduction to GemPy and GemGIS
    3. Purpose of structural geological models in Earth Sciences
    4. Introduction to GemPy and GemGIS
    5. Resources for GemPy and GemGIS
    6. Installation of GemPy and GemGIS
2. [Modeling of the basic structures in GemPy](https://github.com/cgre-aachen/gemgis_data/tree/main/notebooks/01_basic_modeling)
    1. [Modeling planar layers](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/01_basic_modeling/model1_Horizontal_Layers.ipynb)
    2. [Modeling folded layers](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/01_basic_modeling/model2_Folded_Layers.ipynb)
    3. [Modeling faulted layers](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/01_basic_modeling/model3_Faulted_Layers.ipynb)
    4. [Modeling truncated/unconformal layers](https://nbviewer.org/github/cgre-aachen/gemgis_data/blob/main/notebooks/01_basic_modeling/model4_Truncated_Layers.ipynb)
3. Modeling of more complex models including additional tasks (main part)
    1. [Planar dipping layers](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/02_planar_dipping_layers)
    2. [Folded layers](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/03_folded_layers)
    3. [Faulted layers](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/04_faulted_layers)
    4. [Unconformal layers](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/05_unconformal_layers)
    5. [Combination of models](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/06_combined_models)
    6. [Special Case Models](https://github.com/cgre-aachen/gemgis_data/blob/main/notebooks/07_special_models)
4. Post-processing of structural geological models using GemGIS

For more information about GemGIS and GemPy see the dedicated Github Repositories and Documentation pages:
1. GemPy
    1. [Github Repository](https://github.com/cgre-aachen/gempy)
    2. [GemPy Documentation](https://www.gempy.org/)
    3. [GemPy Installation](https://www.gempy.org/installation)
    4. [GemPy Publication](https://gmd.copernicus.org/articles/12/1/2019/)
    5. [Tutorial: Geological Modeling with GemPy @Transform 2020](https://www.youtube.com/watch?v=n0btC5Zilyc&t=1s)
    6. [Tutorial: Geological Modeling with GemPy @Transform 2021](https://www.youtube.com/watch?v=1oS6xTJkRwo)
    7. [Tutorial: Geological Modeling with GemPy ](https://www.youtube.com/watch?v=7P6WrBOaHSM)
    
2. GemGIS
    1. [Github Repository](https://github.com/cgre-aachen/gemgis)
    2. [GemGIS Documentation](https://gemgis.readthedocs.io/)
    3. [GemGIS Installation](https://gemgis.readthedocs.io/en/latest/getting_started/installation.html)
    4. [GemGIS Publication](https://joss.theoj.org/papers/10.21105/joss.03709)

## Purpose of structural geological models in Earth Sciences

Structural geological models describe the spatial distribution of layers in the subsurface. This includes the extent and depth distribution of either lithological layers (e.g. sand or clay, sandstones, carbonates, evaporites, etc.) or stratigraphic units for more regional questions of the structure of the subsurface (e.g. Base Tertiary, transition to basement rocks, etc.). The resulting structures can be used to parametrize the rocks between these constructed bounding surfaces for a wide range of applications. These include but are not limited to hydrogeological applications, geohazards, ressource extraction (e.g. fresh water, thermal waters, hydrocarbons, minerals), storage applications (e.g. thermal waters, gases such as CO2 or hydrogen, nuclear waste). 




## Target Audience

The tutorials provided in this repository aim at enabling students who want to become familiar with structural geological modeling in GemPy to have a smooth start. Further, the tutorials serve as aids for researchers to set up and parametrize their structural geological models properly. Lecturers are encouraged to use and adapt the provided tutorials for their own Python and Structural Geological Modeling classes. 

## Dependencies

The GemGIS package mainly depends on [GeoPandas/Pandas](https://geopandas.org/en/stable/index.html), [Rasterio](https://rasterio.readthedocs.io/en/latest/) and [PyVista](https://docs.pyvista.org/). All geometric operations are performed using [Shapely](https://shapely.readthedocs.io/en/stable/manual.html). Numerical operations are performed using [NumPy](https://numpy.org/doc/stable/index.html) while plotting is done with [Matplotlib](https://matplotlib.org/). The structural modeling package [GemPy](https://www.gempy.org) is an optional dependency but is required to build the structural geological models. 

The following dependency versions are recommended for using GemGIS (as of 2023-05-06):
- Python >=3.9
- GeoPandas >= 0.13 (lastest version update on 2023-06-05) 
- Rasterio >= 1.3.6 (lastest version update on 2023-06-05) 
- PyVista >= 0.39 (lastest version update on 2023-06-05) 
- GemPy >= 2.2.12 (lastest version update on 2022-07-22) 

<a name="ref"></a>
## References

* Jüstel, A., Endlein Correira, A., Wellmann, F. and Pischke, M.: GemGIS – GemPy Geographic: Open-Source Spatial Data Processing for Geological Modeling. EGU General Assembly 2021, https://doi.org/10.5194/egusphere-egu21-4613, 2021
* Jüstel, A., Endlein Correira, A., Pischke, M. and Wellmann, F.: GemGIS - Spatial Data Processing for Geomodeling. Journal of Open Source Software, 7(73), 3709, https://doi.org/10.21105/joss.03709, 2022
* Jüstel, A.: 3D Probabilistic Modeling and Data Analysis of the Aachen-Weisweiler Area: Implications for Deep Geothermal Energy Exploration, unpublished Master Thesis at RWTH Aachen University, 2020
* de la Varga, M., Schaaf, A., and Wellmann, F.: GemPy 1.0: open-source stochastic geological modeling and inversion, Geosci. Model Dev., 12, 1-32, https://doi.org/10.5194/gmd-12-1-2019, 2019
* Powell, D.: Interpretation geologischer Strukturen durch Karten - Eine praktische Anleitung mit Aufgaben und Lösungen, Springer Verlag Berlin, Heidelberg, New York, ISBN: 978-3-540-58607-4, 1995
* Bennison, G.M.: An Introduction to Geological Structures and Maps, Hodder Education Publication, pp. 78, ISBN: 978-1-4615-9632-5, 1988
