from starpy.main import Quadrant, Body

def test_is_in_quadrant():
    test_quadrant = Quadrant(0, 0, 10, 10)
    test_body = Body(100, 2, 2)
    
    assert test_body.is_in_quadrant(test_quadrant) is True
    
def test_add():
    test_body_1 = Body(100, 2, 2)
    test_body_2 = Body(100, 4, 4)
    
    test_composite_body = test_body_1.add(test_body_2)
    
    assert test_composite_body.mass == 200