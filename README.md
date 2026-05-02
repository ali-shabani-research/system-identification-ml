# Data-Driven System Identification using Machine Learning

## Overview
This project explores how machine learning can be used to identify and model dynamical systems from data. The goal is to approximate the underlying system dynamics using a data-driven approach.

## Problem Formulation
We consider a discrete-time dynamical system:

x_{t+1} = a x_t + noise

where the system parameter is unknown and must be learned from observed data.

## Methodology
- Simulated a linear dynamical system
- Generated sequential time-series data
- Applied linear regression to estimate system dynamics

## Results
The learned model successfully approximates the true system parameter, demonstrating how machine learning methods can recover underlying system behavior from data.

## Motivation
Understanding dynamical systems from data is a fundamental problem in control theory and machine learning. This project demonstrates a simple example of system identification, with potential extensions to nonlinear systems and probabilistic modeling.

## Future Work
- Nonlinear system identification
- Neural networks for dynamic systems
- Connection to probabilistic modeling and optimal transport
