#!/usr/bin/env python3
"""
Example usage of the phcalc package.
"""

import numpy as np
from phcalc import calc_pH

def main():
    """Demonstrate basic usage of the calc_pH function."""
    
    print("pH calculation example using phcalc package")
    print("=" * 50)
    
    # realistic coastal seawater pH values around 7.9 (free scale) and 7.8 (total scale)
    
    Vrs = np.array([-0.941602, -0.945, -0.940, -0.942])  # Voltage measurements (V)
    Press = np.array([0, 10, 50, 100])                   # Pressure in decibars
    Temp = np.array([21, 20, 18, 15])                    # Temperature in degrees C
    Salt = np.array([30, 30.5, 31, 31.2])               # Salinity (PSS)
    
    # Sensor calibration parameters (from MBARI mFET calibration)
    k0 = -1.4156395                                      # Reference potential (V)
    k2 = -0.0010626                                      # Temperature coefficient (V/°C)
    Pcoefs = np.array([0.0, 0.0])                       # Pressure coefficients (no pressure correction)
    
    
    print(f"Input data:")
    print(f"  Voltage (V): {Vrs}")
    print(f"  Pressure (dbar): {Press}")
    print(f"  Temperature (°C): {Temp}")
    print(f"  Salinity (PSS): {Salt}")
    print(f"  k0: {k0}")
    print(f"  k2: {k2}")
    print(f"  Pressure coefficients: {Pcoefs}")
    print()
    
    # Calculate pH
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    print("Results:")
    print(f"  pH (free scale): {pHfree}")
    print(f"  pH (total scale): {pHtot}")
    print()
    
    # Display results in a formatted table
    print("Detailed results:")
    print(f"{'Index':<6} {'Press':<8} {'Temp':<8} {'Salt':<8} {'pH_free':<10} {'pH_total':<10}")
    print("-" * 60)
    for i in range(len(Vrs)):
        print(f"{i:<6} {Press[i]:<8.1f} {Temp[i]:<8.1f} {Salt[i]:<8.1f} {pHfree[i]:<10.3f} {pHtot[i]:<10.3f}")

if __name__ == "__main__":
    main()
