from starpy.main import Quadrant
import numpy as np

def test_quadrant_subdivison_contains_1():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    assert quadrant.contains(np.array([12, 11])) is False
    
def test_quadrant_subdivision_contains_2():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    assert quadrant.contains(np.array([10, 10])) is True
    
def test_quadrant_subdivision_contains_3():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    assert quadrant.contains(np.array([3, 5])) is True

def test_quadrant_length():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    
    assert quadrant.length == 10

def test_quadrant_subdivision_nw_1():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    subquadrant = quadrant.new_nw_quadrant()
    subquadrant_lower_left_point = subquadrant.lower_left_point
    subquadrant_upper_right_point = subquadrant.upper_right_point
    
    assert (np.array_equal(subquadrant_lower_left_point, np.array([0, 5])) and
            np.array_equal(subquadrant_upper_right_point, np.array([5, 10])))

def test_quadrant_subdivision_ne_1():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    subquadrant = quadrant.new_ne_quadrant()
    subquadrant_lower_left_point = subquadrant.lower_left_point
    subquadrant_upper_right_point = subquadrant.upper_right_point
    
    assert (np.array_equal(subquadrant_lower_left_point, np.array([5, 5])) and
            np.array_equal(subquadrant_upper_right_point, np.array([10, 10])))

def test_quadrant_subdivision_sw_1():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    subquadrant = quadrant.new_sw_quadrant()
    subquadrant_lower_left_point = subquadrant.lower_left_point
    subquadrant_upper_right_point = subquadrant.upper_right_point
    
    assert (np.array_equal(subquadrant_lower_left_point, np.array([0, 0])) and
            np.array_equal(subquadrant_upper_right_point, np.array([5, 5])))

def test_quadrant_subdivision_se_1():
    quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    subquadrant = quadrant.new_se_quadrant()
    subquadrant_lower_left_point = subquadrant.lower_left_point
    subquadrant_upper_right_point = subquadrant.upper_right_point
    
    assert (np.array_equal(subquadrant_lower_left_point, np.array([5, 0])) and
            np.array_equal(subquadrant_upper_right_point, np.array([10, 5])))