from starpy.main import Quadrant, Body, BHTree

def test_insert_mass():
    quadrant = Quadrant(0, 0, 10, 10)
    bhquadrant = BHTree(quadrant)
    planet_1 = Body(100, 2, 2)

    bhquadrant.insert(planet_1)
    
    assert bhquadrant.body.mass == 100
    
def test_insert_mass_2():
    quadrant = Quadrant(0, 0, 10, 10)
    bhquadrant = BHTree(quadrant)
    planet_1 = Body(100, 2, 2) # Mass in the SW quadrant
    planet_2 = Body(100, 8, 2) # Mass in the SE quadrant

    bhquadrant.insert(planet_1)
    bhquadrant.insert(planet_2)
    
    assert bhquadrant.body.mass == 200
    
def test_individual_node_mass():
    quadrant = Quadrant(0, 0, 10, 10)
    bhquadrant = BHTree(quadrant)
    planet_1 = Body(100, 2, 2) # Mass in the SW quadrant
    planet_2 = Body(100, 8, 2) # Mass in the SE quadrant

    bhquadrant.insert(planet_1)
    bhquadrant.insert(planet_2)
    
    sw_quadrant = bhquadrant.sw
    se_quadrant = bhquadrant.se
    
    assert sw_quadrant.body.mass == 100 and se_quadrant.body.mass == 100