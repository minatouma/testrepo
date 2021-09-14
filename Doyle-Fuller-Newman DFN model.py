#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:41:39 2021

@author: Mina
"""

#Tutorial 1 - How to run a model
#Run first PyBaMM model in just a few simple lines.
#To run through this jupyter notebook simply shift-enter to run the cells
# install PyBaMM if it is not installed
import pybamm

model = pybamm.lithium_ion.DFN() # Doyle-Fuller-Newman (DFN) model

sim = pybamm.Simulation(model)

sim.solve([0, 3600])

sim.plot()

pybamm.print_citations()

pybamm.print_citations(output_format="bibtex")