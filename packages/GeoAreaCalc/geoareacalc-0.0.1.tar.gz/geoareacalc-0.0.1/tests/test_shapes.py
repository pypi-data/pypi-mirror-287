import pytest
from GeoAreaCalc.shapes import Circle, Triangle


def test_circle_area():
    circle = Circle(radius=5)
    assert circle.area() == pytest.approx(78.5398, 2)


def test_triangle_area():
    triangle = Triangle(side1=3, side2=4, side3=5)
    assert triangle.area() == pytest.approx(6.0, 2)
    assert triangle.is_right_triangle() is True

    non_right_triangle = Triangle(side1=3, side2=3, side3=5)
    assert non_right_triangle.is_right_triangle() is False
