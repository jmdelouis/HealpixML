# HealpixML

## the concept

The HealpixML genesis has been built to synthesise data (2D or Healpix) using Cross Scattering Transform. For a detailed method description please refer to https://arxiv.org/abs/2207.12527. This algorithm could be effectively usable for component separation (e.g. denoising).

## Authors
J.-M. Delouis, T. Foulquier, L. Mousset, T. Odaka,  P. Campeti, E. Allys,  F. Paul,

# Short tutorial

## Exemple of synthesis

https://github.com/jmdelouis/HealpixML/blob/main/Notebooks/Demo_Synthesis.ipynb

A more complete exemple of what is doable with HealpixML is here https://github.com/pcampeti/CMBSCAT

# Install HealpixML library

Before installing, make sure you have python installed in your enviroment.
The last version of the HealpixML library can be installed using PyPi:

```
pip install HealpixML
```

## Recommended installing procedures for mac users

It is recomended to use python=3.9\*.
It is recomended to install tensorflow in advance.

```
micromamba create -n HEALPIXML
micromamba install -n HEALPIXML ‘python==3.9*’
micromamba install -n HEALPIXML ‘tensorflow’
micromamba activate HEALPIXML
pip install HealpixML

```

## Recommended installing procedures HPC users

It is recomended to install tensorflow in advance. For [DATARMOR](https://pcdm.ifremer.fr/Equipement) for using GPU ;

```
micromamba create -n HEALPIXML
micromamba install -n HEALPIXML ‘python==3.9*’
micromamba install -n HEALPIXML ‘tensorflow==2.11.0’
micromamba activate HEALPIXML
pip install HealpixML

```
