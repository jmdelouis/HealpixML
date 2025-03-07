# HealpixML

## the concept

The HealpixML genesis has been built to synthesise data (2D or Healpix) using Cross Scattering Transform. For a detailed method description please refer to https://arxiv.org/abs/2207.12527. This algorithm could be effectively usable for component separation (e.g. denoising).

A demo package for this process can be found at https://github.com/jmdelouis/HEALPIXML_DEMO.

## usage

# Short tutorial

https://github.com/IAOCEA/demo-HealpixML-pangeo-eosc/blob/main/Demo_Synthesis.ipynb

# HEALPIXML_DEMO

The python scripts _demo.py_ included in this package demonstrate how to use the HealpixML library to generate synthetic fields that have patterns with the same statistical properties as a specified image.

# Install HealpixML library

Before installing, make sure you have python installed in your enviroment.
The last version of the HealpixML library can be installed using PyPi:

```
pip install HealpixML
```

Load the HEALPIXML_DEMO package from github.

```
git clone https://github.com/jmdelouis/HEALPIXML_DEMO.git
```

## Recommended installing procedures for mac users

It is recomended to use python=3.9\*.

```
micromamba create -n HEALPIXML
micromamba install -n HEALPIXML ‘python==3.9*’
micromamba activate HEALPIXML
pip install HealpixML
git clone https://github.com/jmdelouis/HEALPIXML_DEMO.git

```

## Recommended installing procedures HPC users

It is recomended to install tensorflow in advance. For [DATARMOR](https://pcdm.ifremer.fr/Equipement) for using GPU ;

```
micromamba create -n HEALPIXML
micromamba install -n HEALPIXML ‘python==3.9*’
micromamba install -n HEALPIXML ‘tensorflow==2.11.0’
micromamba activate HEALPIXML
pip install HealpixML
git clone https://github.com/jmdelouis/HEALPIXML_DEMO.git

```
