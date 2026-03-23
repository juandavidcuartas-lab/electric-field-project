# Electric Field Reconstruction from Experimental Data

This project reconstructs the electric field from experimentally measured electric potential using numerical methods.

## Method

The electric field is computed from the potential using:

E = -∇V

A finite difference approximation is used to estimate the gradient.

## Features

- Reads experimental data from CSV
- Computes numerical gradient using NumPy
- Visualizes:
  - Equipotential lines
  - Electric field vectors

## Result

![Electric Field](results/campo_electrico.png)

## How to Run

```bash
pip install numpy matplotlib pandas
python src/main.py
