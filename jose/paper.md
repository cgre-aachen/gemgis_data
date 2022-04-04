---
title: 'From Maps to Models - Tutorials for structural geological modeling'
tags:
  - Python
  - geology 
  - geographic
  - structural geology
  - GIS
  - spatial data
authors:
  - name: Alexander Jüstel
    orcid: 0000-0003-0980-7479
    affiliation: "1, 2"
  - name: Miguel de la Varga
    affiliation: 3
  - name: Stefan Back
    affiliation: 2
  - name: Florian Wellmann
    orcid: 0000-0003-2552-1876
    affiliation: 4
affiliations:
 - name: Fraunhofer IEG, Fraunhofer Research Institution for Energy Infrastructures and Geothermal Systems, Kockerellstraße 17, 52062 Aachen, Germany
   index: 1
 - name: RWTH Aachen University, Geological Institute, Wüllnerstraße 2, 52062 Aachen, Germnany
   index: 2
 - name: Terranigma Solutions GmbH, Laurentiusstraße 59, 52072 Aachen
   index: 3
 - name: RWTH Aachen University , Computational Geoscience and Reservoir Engineering, Wüllnerstraße 2, 52062 Aachen, Germany
   index: 4


date: 
bibliography: paper.bib
---

# Summary

The presented tutorials enable users of the **GemPy** and **GemGIS** Python libraries and associated packages to create structural geological models from scratch using input data for conceptual models but also more sophisticated models representing possible real world examples. The so-called "Bennison-Maps" and other maps transformed into structural geological models are teaching materials for undergraduate students in the field of Applied Geosciences at RWTH Aachen University, Germany. Their purpose is to enable students to not only think about geological problems in 2D (map view) but also in 3D (current structure of the subsurface) and even 4D (depositional, tectonic and erosinal events resulting in the current structure). Creating these models digitally is not a mean to substitute the necessary analog thinking of geoloscientists but to aid them in verifying their results and to introduce them to the world of data processing, data visualization, and structural geological modeling in Python.


# Statement of Need 

The subsurface below our feet is utilized in many different ways. We extract fresh water, thermal waters and fossil fuels from it. We exploit the subsurface for its coal, minerals and ores in open-pit mines and underground mines. We store fluids and gases as well as nuclear waste in the subsurface. But to do so, a concept of the structure of the subsurface and its properties is needed to drill into the right formation, to dig into right direction and to ensure that no contaminants leak into surrounding rocks. Creating structural geological models not only in 1D boreholes or 2D cross sections but also in 3D models is a first step to gain comprehensive knowledge of the subsurface. Apart from actually drawing models, most efforts to create structural geological models in 3D is restricted to commercial software packages such as GeoModeller, Petrel, Move, GoCad and others. The aim of **GemPy** [@{gempy}] and **GemGIS** [@{gemgis}] and associated open-source packages and software is to provide open-source software tools to create 3D structural geological models from maps, cross sections, borehole information, stratigraphic boundaries at the surface and the subsurface and orientation measurements of the stratigraphic units. The tutorial materials presented here are adopted from a mapping class for undergraduate students majoring in Applied Geosciences at RWTH Aachen University, Germany. The purpose of this class is to enable the geological thinking of the students and to allow them to obtain a concept of the structures in the subsurface through drawing of 2D cross sections. The tutorials presented here are by no means an attempt to replace this critical thinking and the drawing of the maps in an analog way but rather to motivate students to literally dig deeper into the data or to confirm their previous results. Furthermore, the barrier to utilize the Python language and associated packages for processing and visualizing data is lowered. 

# Resources
The following resources are provided before going through the tutorials. It is recommended to use an Anaconda Python distribution (https://www.anaconda.com/) and Jupyter Notebooks (https://jupyter.org/) to work with the tutorials. Both **GemPy** and **GemGIS** have been developed in recent years at the Department for Computational Geosciences and Reservoir Engineering at RWTH Aachen University, Germany (https://www.cgre.rwth-aachen.de/). Both libraries are stored on Github and have well-documented resources:

- Tutorial Repository - https://github.com/cgre-aachen/gemgis_data

- GemPy Repository - https://github.com/cgre-aachen/gemgis
- GemPy Documentation - https://www.gempy.org
- GemPy Installation - https://www.gempy.org/installation

- GemGIS Repository - https://github.com/cgre-aachen/gemgis
- GemGIS Documentation - https://gemgis.readthedocs.io/ 
- GemGIS Installation - https://gemgis.readthedocs.io/en/latest/getting_started/installation.html


# Learning Objectives

Upon completion of the tutorials, the users will have learnt to:
- Create the necessary raw data for **GemGIS** and **GemPy** using the open-source software QGIS
- Explore and manipulate the raw data using the Pandas [@{pandas}] and GeoPandas libraries [@{geopandas}]
- Process the raw data using **GemGIS** to create input data for **GemPy**
- Create the 3D structural model using **GemPy**
- Visaulize the results using Matplotlib [@{matplotlib}] and PyVista [@{pyvista}]
- Perform post-processing tasks 

# Contents

The tutorials are organized in a modular fashion and consist of three units:
- Basic structural geological modeling with GemPy (4 notebooks)
- Using **GemGIS** and **GemPy** for construction structural geological models based on teaching material (x notebooks)
- Using post-processing to get more information out of your models (x notebooks) 

## Basic Structural Geological Modeling with GemPy
**GemPy** is capabale of modeling planar layers, folded layers, faulted layers, truncated layers and combinations of the aforementioned structures. The required input data for building a structural model in **GemPy** consists of locations for stratigraphic boundaries encountered on the surface (outcrops, mines) or in the subsurface (boreholes, seismic data) and orientation measurements representing the dip and the azimuth of the respective stratigraphic unit. The input is loaded and will be assigned different Series representing conformal surfaces which will be modeled using one scalar field. Surfaces within different Series will be calculated using different scalar fields. Each fault will be attributed to its own Series and hence modeled with a separat scalar field along which the faulting of the stratigraphic units occurs. The interpolation is performed meshless but a marching cube algorithm is used to create PyVista meshes from the voxel models for further visualization and post-processing.\\

The first four notebooks illustrate how to create the different structures that **GemPy** is capable of modeling (Fig. \ref{fig1}): 
- Planar layers
- Folded layers
- Faulted layers
- Truncated layers

![Basic models representing planar layers, folded layers, faulted layers and truncated layers. \label{fig1}](./images/fig1.png)

## Model Building using teaching materials

In the section for the basic structural geological, models were presented where only one structural feature was present. In this part of the tutorial, the models will include combinations of structural elements and therefore more complex models. In addition, a topography, similar to the topography of the Earth, will be added to the models based on contour lines provided with the geological maps. 

The biggest change to the previous models is that the input data will not be provided as CSV-file but rather as Shape-Files created by the user in a GIS environment such as QGIS. These data sets will be loaded using the geopandas library and processed using **GemGIS** to generate the necessary input DataFrames for **GemPy**. 

## Post-Processing of Models

Now that the user has become familiar with the data creation using QGIS, the data loading using geopandas, the data processing using **GemGIS** and the structural geological modeling using **GemPy**, methods are presented how to further visualize the results of the modeling and how to extract certain information from the model. These methods include but are by far not limited to:

- Creating depth maps and contour lines for single stratigraphic boundaries
- Exporting depth maps as ZMAP files for visualization in QGIS
- Creating virtual boreholes and extract depths of intersected stratigraphic boundaries
- 


# Acknowledgements

All authors would like to thank the Software Underground (https://softwareunderground.org/) for providing a platform to interact with users and to organize hackathons (Transform 2020/2021) to further develop the open-source package. 
We also acknowledge contributions from, and thank all our users for reporting bugs, raising issues and suggesting improvements to the API of **GemGIS**. 

# References
