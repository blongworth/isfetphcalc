"""
Basic tests for the isfet-phcalc package.
"""

import numpy as np
import pytest
from isfet_phcalc import calc_pH

def test_calc_pH_basic():
    """Test basic functionality of calc_pH function."""
    # Test data with realistic BGC-Argo sensor values
    Vrs = np.array([-0.941602])
    Press = np.array([0.0])
    Temp = np.array([21.0])
    Salt = np.array([30.0])
    k0 = -1.4156395
    k2 = -0.0010626
    Pcoefs = np.array([0.0, 0.0])
    
    # Calculate pH
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    # Basic checks
    assert isinstance(pHfree, np.ndarray)
    assert isinstance(pHtot, np.ndarray)
    assert len(pHfree) == len(Vrs)
    assert len(pHtot) == len(Vrs)
    assert np.all(np.isfinite(pHfree))
    assert np.all(np.isfinite(pHtot))
    
    # pH values should be finite numbers (exact range depends on calibration)
    assert isinstance(pHfree[0], (int, float, np.floating))
    assert isinstance(pHtot[0], (int, float, np.floating))

    # test for correct values
    np.testing.assert_allclose(pHfree[0], 7.9271, rtol=1e-4, atol=1e-4)
    np.testing.assert_allclose(pHtot[0], 7.8382, rtol=1e-4, atol=1e-4)

def test_calc_pH_arrays():
    """Test calc_pH with array inputs."""
    # Test with multiple realistic data points
    Vrs = np.array([-0.941602, -0.945, -0.940])
    Press = np.array([0, 10, 50])
    Temp = np.array([21, 20, 18])
    Salt = np.array([30, 30.5, 31])
    k0 = -1.4156395
    k2 = -0.0010626
    Pcoefs = np.array([0.0, 0.0])
    
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    assert len(pHfree) == 3
    assert len(pHtot) == 3
    assert np.all(np.isfinite(pHfree))
    assert np.all(np.isfinite(pHtot))

def test_calc_pH_relationship():
    """Test that pH_free and pH_total have expected relationship."""
    Vrs = np.array([-0.941602])
    Press = np.array([0.0])
    Temp = np.array([21.0])
    Salt = np.array([30.0])
    k0 = -1.4156395
    k2 = -0.0010626
    Pcoefs = np.array([0.0, 0.0])
    
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    # pH_total should be lower than pH_free due to sulfate contribution
    assert pHtot[0] < pHfree[0]

def test_calc_pH_expected_values():
    """Test that calc_pH produces expected pH values for known inputs."""
    # Test with specific BGC-Argo sensor calibration values
    Vrs = np.array([-0.941602])
    Press = np.array([0.0])
    Temp = np.array([21.0])
    Salt = np.array([30.0])
    k0 = -1.4156395
    k2 = -0.0010626
    Pcoefs = np.array([0.0, 0.0])
    
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    # Test expected values (within reasonable tolerance for floating point)
    np.testing.assert_allclose(pHfree[0], 7.9271, rtol=1e-4, atol=1e-4)
    np.testing.assert_allclose(pHtot[0], 7.8382, rtol=1e-4, atol=1e-4)

def test_calc_pH_no_negative_values():
    """Test that calc_pH doesn't produce negative pH values with realistic inputs."""
    # Test with various realistic sensor values
    Vrs = np.array([-0.941602, -0.945, -0.940, -0.935])
    Press = np.array([0, 10, 50, 100])
    Temp = np.array([21, 20, 18, 15])
    Salt = np.array([30, 30.5, 31, 31.2])
    k0 = -1.4156395
    k2 = -0.0010626
    Pcoefs = np.array([0.0, 0.0])
    
    pHfree, pHtot = calc_pH(Vrs, Press, Temp, Salt, k0, k2, Pcoefs)
    
    # All pH values should be positive (realistic seawater pH is typically 7.5-8.5)
    assert np.all(pHfree > 0), f"Found negative pH_free values: {pHfree[pHfree <= 0]}"
    assert np.all(pHtot > 0), f"Found negative pH_total values: {pHtot[pHtot <= 0]}"
    
    # pH values should be in reasonable range for seawater
    assert np.all(pHfree > 7.0), f"pH_free values too low: {pHfree[pHfree <= 7.0]}"
    assert np.all(pHfree < 9.0), f"pH_free values too high: {pHfree[pHfree >= 9.0]}"
    assert np.all(pHtot > 7.0), f"pH_total values too low: {pHtot[pHtot <= 7.0]}"
    assert np.all(pHtot < 9.0), f"pH_total values too high: {pHtot[pHtot >= 9.0]}"
