import pytest
from ornament_calculator import ornament_estimator

def test_budget():
    assert ornament_estimator("yes", 3, 1.2) != ornament_estimator("no", 3, 1.2)
    assert ornament_estimator("yes", 5, 2) < ornament_estimator("no", 5, 2)

def test_height():
    assert ornament_estimator("yes", 3, 1.2) < ornament_estimator("yes", 4, 1.2)
    assert ornament_estimator("yes", 5, 2) < ornament_estimator("yes", 6, 2)

def test_radius():
    assert ornament_estimator("yes", 3, 1.2) < ornament_estimator("yes", 3, 2)
    assert ornament_estimator("yes", 5, 2) < ornament_estimator("yes", 5, 3.5)

def test_formula():
    assert ornament_estimator("yes", 3, 1.2) == 97
    assert ornament_estimator("no", 5, 2) == 406