# New_theoretical_nuclear_project

## Table of contents:
1. [Description](#description)
2. [Algorithm used](#algo-used)
3. [Referencies](#ref)
4. [Library used](#lib-used)
5. [Run](#how-to-run)

## Description
This Python project deals with the Polonium-210 problem.
Polonium-210 is a result of a series of decaying process involving Bismuth-209 isotope.
During the process, Bi-209 decays to Bi-210 and, by beta decay to Po-210.

Main physical-chemical characteristics of Po-210 are:
1. soluble in acid;
2. low melting temperature (254 °C);
3. volatile at low temperatures (55 °C);
4. half-life 138 days;
6. acts as a neutron source with Beryllium;
7. eliminates stati charges in machinery;
8. acts as a lightweight heat source to thermoelectric cells.

Polonium is an alpha emitter. As alpha emitter, it poses no external hazard but it does pose a hazard 
if ingested, inhaled or if enters the body. 

## Algorithm used
In this project a system of three-ordinary differential equations is solved by matrix exponential approach. The main idea is creating a square matrix containing the decay constants of the three nuclides and diagonalize that matrix in order to compute eigenvalues and expand the exponential through them. This algorithm has been already implemented in the Scipy library (scipy.linalg.expm) and uses the Padé approximation. Only a matrix product is necessary and a loop to iterate the process until a collapsed-time (365 days) is reached.
In this code classes are created in order to collect constants that are used during the main code.
In the file main.py the matrix exponentiation is computed.
Everything is passed to another Python file that shows the three curves obtained. The images.png are then saved and collected here.

## Referencies
By doing this project, many papers, websites have been used. They are quote here:
1. [Introductory Nuclear Physics - Kenneth Krane](https://www.fulviofrisone.com/attachments/article/446/Krane%20-%20Introductory%20Nuclear%20Physics.pdf);
2. [Polonium-210 (paper) - Washington State Department of Health](https://doh.wa.gov/sites/default/files/legacy/Documents/Pubs//320-091_po210_fs.pdf);
3. [Implementation, validation and comparison of different algorithms to solve the Bateman equations for very large systems - Vranckx Maren](https://publications.sckcen.be/portal/files/1169036/Masterproef_Maren_Vranckx.pdf);
4. [Matrix exponential - Wikipedia](https://en.wikipedia.org/wiki/Matrix_exponential).

## Library used
Here a collection of Python libraries used to do the code:
1. Numpy;
2. Scipy.linalg.expm (Padé approximation);
3. Matplotlib.pyplot;
4. Tabulate.

## Run
```shell
python main.py
```
