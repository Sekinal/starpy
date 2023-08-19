from starpy.main import Quadrant

def test_quadrant_subdivison_contains_1():
    quadrant = Quadrant(0, 0, 10, 10)
    assert quadrant.contains(12, 11) is False
    
def test_quadrant_subdivision_contains_2():
    quadrant = Quadrant(0, 0, 10, 10)
    assert quadrant.contains(10, 10) is True
    
def test_quadrant_subdivision_contains_3():
    quadrant = Quadrant(0, 0, 10, 10)
    assert quadrant.contains(3, 5) is True

def test_quadrant_length():
    quadrant = Quadrant(0, 0, 10, 10)
    
    assert quadrant.length == 10

def test_quadrant_subdivision_ne_1():
    quadrant = Quadrant(0, 0, 10, 10)
    subquadrant = quadrant.new_ne_quadrant()
    subquadrant_coordinates = (subquadrant.x_1, subquadrant.y_1,
                               subquadrant.x_2, subquadrant.y_2)
    
    assert subquadrant_coordinates == (5, 5, 10, 10)

def test_quadrant_subdivision_nw_1():
    quadrant = Quadrant(0, 0, 10, 10)
    subquadrant = quadrant.new_nw_quadrant()
    subquadrant_coordinates = (subquadrant.x_1, subquadrant.y_1,
                               subquadrant.x_2, subquadrant.y_2)
    
    assert subquadrant_coordinates == (0, 5, 5, 10)
    
def test_quadrant_subdivision_se_1():
    quadrant = Quadrant(0, 0, 10, 10)
    subquadrant = quadrant.new_se_quadrant()
    subquadrant_coordinates = (subquadrant.x_1, subquadrant.y_1,
                               subquadrant.x_2, subquadrant.y_2)
    
    assert subquadrant_coordinates == (5, 0, 10, 5)

def test_quadrant_subdivision_sw_1():
    quadrant = Quadrant(0, 0, 10, 10)
    subquadrant = quadrant.new_sw_quadrant()
    subquadrant_coordinates = (subquadrant.x_1, subquadrant.y_1,
                               subquadrant.x_2, subquadrant.y_2)
    
    assert subquadrant_coordinates == (0, 0, 5, 5)