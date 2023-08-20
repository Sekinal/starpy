from starpy.main import Quadrant, Body
import numpy as np

def test_is_in_quadrant():
    test_quadrant = Quadrant(np.array([0, 0]), np.array([10, 10]))
    test_body = Body(100, np.array([2, 2]))
    
    assert test_body.is_in_quadrant(test_quadrant) is True
    
def test_add():
    test_body_1 = Body(100, np.array([2, 2]))
    test_body_2 = Body(100, np.array([4, 4]))
    
    test_composite_body = test_body_1.add(test_body_2)
    
    test_mass = test_composite_body.mass
    test_position = test_composite_body.spatial_data[0]
        
    assert (np.array_equal(test_mass, 200) and
            np.array_equal(test_position, np.array([3, 3])))