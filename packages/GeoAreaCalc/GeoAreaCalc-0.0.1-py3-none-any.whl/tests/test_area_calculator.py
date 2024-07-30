import pytest
from GeoAreaCalc.area_calculator import calculate_area
from GeoAreaCalc.shapes import Circle, Triangle


def test_area_calculate_circle():
    circle = Circle(radius=5)
    assert pytest.approx(calculate_area(circle), 0.0001) == 78.5398


def test_area_calculate_triangle():
    triangle = Triangle(side1=3, side2=4, side3=5)
    assert pytest.approx(calculate_area(triangle), 0.0001) == 6
