import data
import lab4
import unittest
import math

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input = [[1,2], []]
        result = lab4.first_element(input)
        expected = [1]
        self.assertEqual(expected, result)
    # Part 2
    def test_x_coordinates_1(self):
        point = data.Point(1,2)
        point2 = data.Point(3,4)
        list = [point,point2]
        result = lab4.x_coordinates(list)
        expected = [1,3]
    def test_x_coordinates_2(self):
        point = data.Point(1, 2)
        point2 = 0
        list = [point, point2]
        result = lab4.x_coordinates(list)
        expected = [1]

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        point = data.Point(1,2)
        point2 = data.Point(3,4)
        point3 = data.Point(-5,6)
        list = [point,point2,point3]
        result = lab4.are_in_positive_quadrant(list)
        expected = [point,point2]
    def test_are_in_positive_quadrant_2(self):
        point = data.Point(1,-2)
        point2 = data.Point(3,4)
        point3 = data.Point(-5,-6)
        point4 = 0
        list = [point,point2,point3,point4]
        result = lab4.are_in_positive_quadrant(list)
        expected = [point2]
    # Part 4
    def test_distance_1(self):
        point = data.Point(1,2)
        point2 = data.Point(3,4)
        result = lab4.distance(point,point2)
        expected = math.sqrt(8)
    def test_distance_2(self):
        point = data.Point(2,3)
        point2 = data.Point(3,4)
        result = lab4.distance(point,point2)
        expected = math.sqrt(2)
    # Part 5
    def test_manhattan_distance_1(self):
        point = data.Point(1,2)
        point2 = data.Point(3,4)
        result = lab4.manhattan_distance(point,point2)
        expected = 4
    def test_manhattan_distance_2(self):
        point = data.Point(1,11)
        point2 = data.Point(3,0)
        result = lab4.manhattan_distance(point,point2)
        expected = 13
    # Part 6
    def test_all_distance_1(self):
        origin = data.Point(0,0)
        point = data.Point(1, -2)
        point2 = data.Point(3, 4)
        point3 = data.Point(-5, -6)
        point4 = data.Point(0,9)
        list = [point, point2, point3, point4]
        result = lab4.are_in_positive_quadrant(list)
        expected = [lab4.distance(origin, point), lab4.distance(origin, point2), lab4.distance(origin, point3), lab4.distance(origin, point4)]
    def test_all_distance_2(self):
        origin = data.Point(0,0)
        point = data.Point(1, 10)
        point2 = data.Point(0, 4)
        point3 = data.Point(-5, -6)
        point4 = data.Point(0,9)
        list = [point, point2, point3, point4]
        result = lab4.are_in_positive_quadrant(list)
        expected = [lab4.distance(origin, point), lab4.distance(origin, point2), lab4.distance(origin, point3), lab4.distance(origin, point4)]




if __name__ == '__main__':
    unittest.main()
