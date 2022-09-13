from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Segment
from convex import Polygon


class TestR2Point1:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(2.0, 0.0))

    # Двуугольник не имеет диагоналей, соответственно длина равна нулю
    def test_min_d1(self):
        assert self.f.min_d() == approx(0.0)


class TestPolygon1:

    # Аналогично для треугольника (диагоналей нет)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                -4.0, 3.0), R2Point(
                -4.0, -3.0), R2Point(
                4.0, -3.0))

    def test_min_d2(self):
        assert self.f.min_d() == approx(0.0)


class TestPolygon2:

    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                4.0, 0.0), R2Point(
                0.0, 3.0))

    def test_min_d3(self):
        assert self.f.add(R2Point(4.0, 3.0)).min_d() == approx(5.0)

    def test_min_d4(self):
        assert self.f.add(R2Point(5.0, 5.0)).min_d() == approx(5.0)

    def test_min_d5(self):
        assert self.f.add(R2Point(3.5, -1.0)).min_d() == approx(4.0)


class TestPolygon3:

    def setup_method(self):
        self.f = Polygon(
            R2Point(
                -2.0, 3.0), R2Point(
                3.0, 1.0), R2Point(
                2.0, -1.0))

    def test_min_d6(self):
        assert self.f.add(R2Point(-2.0, -2.0)).min_d() == approx(sqrt(32))

    def test_min_d7(self):
        assert self.f.add(R2Point(1.0, 3.0)).min_d() == approx(sqrt(17))
