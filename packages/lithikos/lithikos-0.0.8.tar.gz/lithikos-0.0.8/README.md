# Stone Tool Symmetry Analyser

Lithikos is an open-source morphometry which calculates volumetric data for the artefact model and a radially symmetrical reference.

This application was initally written for the analysis of bilateral and bifacial symmetry of 3D models of paleolithic stone tools.
Various options are available for artefact alighment. Once aligned and oriented, the model is divided into a number of slices along the legth of the model in order to analyze the morphology of each model before fitting the largest possible known-symmetrical reference (Endo-Sym) within the topological boundary of each artefact model.
The measurements from the generated reference mesh can then be used, in conjunction with the original mesh, to determine coefficients of asymmetry etc.


## Motivation

There have been a number of 2D approaches to the analysis of bilateral symmetry in Acheulean handaxes: a radial qualification approach (Marathe, 1980), a radial quantification approach (Wynn & Tierson, 1990), the Continuous Symmetry Measure (Saragusti et al., 1998), a mental folding method (McNabb et al., 2004), the Index of Symmetry measure (Lycett et al., 2008) and the Index of Deviation of Symmetry by Feizi et al. (2018, 2020). The most popular analysis of bilateral symmetry has been the Flip Test and its Asymmetry Index (Couzens, 2013; Hardaker & Dunn, 2005; Keen et al. 2006; Lee, 2016; Putt et al., 2014; Shipton, 2018; Underhill, 2007; White & Foulds, 2018). To simultaneously quantify both bilateral and bifacial handaxe symmetry, Li et al. (2016, 2018) introduced a novel correlative approach based on analyzing the volumes of opposing halves of bifurcated 3D models of handaxes, but without any reference to a known symmetrical min. As an alternative to the unreferenced volumetric approach by Li et al., this application and the resulting *Coefficents of Symmetry* offer a 3-dimensional analysis of symmetry referencing a known symmetrical min.

## Installation and Setup

To install the applicastion,

```
pip install lithikos
```

## Quickstart Code Example
```
lithikos my_handaxe.obj
```
## Usage Reference

Roe (1964, 1968) measured a small set of planar metrics and analyzed a large body of Acheulean bifaces gathered from 38 sites in Southern Britain to document the variability in size, shape, and refinement of whole assemblages or groups of assemblages. He employed five ratios based on seven linear (planar) measurements (in millimeters) and the weight (in ounces) of an artefact. The planar measurements included length (tip to butt in plan view), breadth (maximum from side to side in plan view), and thickness (maximum in profile view).

## Recommended citation

## Other Related Tools
