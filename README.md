# phcalc

A Python package for calculating pH values from ISFET sensor data in ocean biogeochemical applications, specifically designed for BGC-Argo data processing.

## Overview

This package provides functions for calculating pH values on both free and total scales from voltage measurements of ISFET (Ion-Sensitive Field-Effect Transistor) sensors in seawater. The calculations follow the methodology described in the BGC-Argo pH processing documentation.

PJB found this in MATLAB code at
https://github.com/SOCCOM-BGCArgo/ARGO_PROCESSING/blob/master/MFILES/FLOATS/phcalc.m on 14-June-2019
THIS FUNCTION WAS COPIED AND VERIFIED FROM THE ARGO PH PROCESSING DOCUMENT ON 1/15/19
Processing BGC-Argo pH data at the DAC level (https://doi.org/10.13155/57195)

## Installation

Install the package using uv:

```bash
uv add phcalc
```

Or from source:

```bash
git clone https://github.com/yourusername/phcalc.git
cd phcalc
uv pip install -e .
```

## Usage

```python
import numpy as np
from phcalc import calc_pH

# Example data (realistic BGC-Argo sensor values)
Vrs = np.array([-0.941602, -0.945, -0.940])  # Voltage between reference electrode and ISFET source
Press = np.array([0, 10, 50])                # Pressure in decibars
Temp = np.array([21, 20, 18])                # Temperature in degrees C
Salt = np.array([30, 30.5, 31])             # Salinity (PSS)
k0 = -1.4156395                              # Sensor reference potential
k2 = -0.0010626                              # Linear temperature coefficient
Pcoefs = np.array([0.0, 0.0])               # Pressure coefficients (no pressure correction)

# Calculate pH
pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)

print(f"pH free scale: {pHfree}")
print(f"pH total scale: {pHtot}")
```

## Function Reference

### `calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)`

Calculate pH values from ISFET sensor data.

**Parameters:**
- `Vrs` (numpy array): Voltage between reference electrode and ISFET source
- `Press` (numpy array): Pressures in decibars
- `Temp` (numpy array): Temperature in degrees C
- `Salt` (numpy array): Salinity (usually CTD salinity on the PSS)
- `k0` (float): Sensor reference potential (intercept at Temp = 0°C)
- `k2` (float): Linear temperature coefficient (slope)
- `Pcoefs` (numpy array): Sensor dependent pressure coefficients

**Returns:**
- `pHfree` (numpy array): pH on the free scale
- `pHtot` (numpy array): pH on the total scale

## Scientific Background

The calculations are based on:
- Dickson, A. G., Sabine, C. L., & Christian, J. R. (2007). Guide to best practices for ocean CO2 measurements.
- BGC-Argo pH processing documentation (https://doi.org/10.13155/57195)
- Original MATLAB implementation from SOCCOM-BGCArgo/ARGO_PROCESSING

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.