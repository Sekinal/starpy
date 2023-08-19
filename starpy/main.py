class Quadrant:
    """A quadrant datatype. It subdivides the space into smaller regions.
    This quadrant is defined by a lower left point located at (x_1, y_1) and an upper
    right point located at (x_2, y_2).
    """
    def __init__(self, x_1, y_1, x_2, y_2) -> None:
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.length = self.x_2 - self.x_1
    
    def contains(self, x, y):
        """A method that checks if the given point located at (x, y) is contained within
        the quadrant region.

        Args:
            x (float): x coordinate of the given point
            y (float): y coordinate of the given point

        Returns:
            bool: Returns either True if the given point is within the quadrant or False
            if it's not
        """
        if x >= self.x_1 and x <= self.x_2:
            if y >= self.y_1 and y <= self.y_2:
                return True
        else:
            return False
    
    def new_ne_quadrant(self):
        """A method that creates a new NE subquadrant in the specified quadrant.

        Returns:
            quadrant: A new quadrant datatype in a subregion of the main quadrant.
        """
        side_length = self.length
        new_x_1 = self.x_1 + side_length/2
        new_y_1 = self.y_1 + side_length/2
        
        return Quadrant(new_x_1, new_y_1, self.x_2, self.y_2)
    
    def new_nw_quadrant(self):
        """A method that creates a new NW subquadrant in the specified quadrant.

        Returns:
            quadrant: A new quadrant datatype in a subregion of the main quadrant.
        """
        new_y_1 = self.y_1 + self.length/2
        new_x_2 = self.x_2 - self.length/2
        
        return Quadrant(self.x_1, new_y_1, new_x_2, self.y_2)
    
    def new_sw_quadrant(self):
        """A method that creates a new SW subquadrant in the specified quadrant.

        Returns:
            quadrant: A new quadrant datatype in a subregion of the main quadrant.
        """
        new_x_2 = self.x_2 - self.length/2
        new_y_2 = self.y_2 - self.length/2
        
        return Quadrant(self.x_1, self.y_1, new_x_2, new_y_2)
    
    def new_se_quadrant(self):
        """A method that creates a new SE subquadrant in the specified quadrant.

        Returns:
            quadrant: A new quadrant datatype in a subregion of the main quadrant.
        """
        new_x_1 = self.x_1 + self.length/2
        new_y_2 = self.y_2 - self.length/2
        
        return Quadrant(new_x_1, self.y_1, self.x_2, new_y_2)

class Body:
    """A particle datatype. This represents an individual or a system of bodies in the
    physical simulation, containing all of its relevant physical data.
    """
    def __init__(self, mass, x, y) -> None:
        self.mass = mass
        self.x = x
        self.y = y
    
    def is_in_quadrant(self, quadrant):
        """A method that checks if the given body is contained within the specified
        quadrant.

        Args:
            quadrant (class quadrant): A quadrant datatype.

        Returns:
            bool: Returns either True or False depending on whether or not the body is
            contained within the given quadrant.
        """                
        is_contained = quadrant.contains(self.x, self.y)
        return is_contained

    def add(self, first_body, second_body):
        """A method that calculates the center of mass given two bodies, anc creates
        a new body on the given data

        Args:
            first_body (class Body): A physical body.
            second_body (class Body): A physical body.

        Returns:
            class Body: Another body.
        """
        
        m_1, x_1, y_1 = first_body.mass, first_body.x, first_body.y
        m_2, x_2, y_2 = second_body.mass, second_body.x, second_body.y
        
        m_cm = m_1 + m_2
        x_cm = (x_1*m_1 + x_2*m_2)/m_cm
        y_cm = (y_1*m_1 + y_2*m_2)/m_cm
        
        return Body(m_cm, x_cm, y_cm)

class BHTree:
    """A class implementing the Barnes-Hut quadtree.
    """
    def __init__(self, quadrant) -> None:

        self.quadrant = quadrant
        self.divided = False
        self.body = None
        
    def divide(self):
        """Creates a BHtree representing each quadrant
        """
        self.nw = BHTree(self.quadrant.new_nw_quadrant())
        self.ne = BHTree(self.quadrant.new_ne_quadrant())
        self.sw = BHTree(self.quadrant.new_sw_quadrant())
        self.se = BHTree(self.quadrant.new_se_quadrant())
        
        self.divided = True
    
    def insert(self, body):
        """A method that tries to insert a body in the actual quadrant.

        Args:
            body (class Body): A body to be simulated.

        Returns:
            _type_: _description_
        """
        
        if not body.is_in_quadrant(self.quadrant):
            # If the body doesn't lie within the quadrant, return False and exit
            return False
        elif self.body is None:
            self.body = body
            return True
        elif not self.divided:
            self.divide()
        
        return (self.nw.insert(body) or self.nw.insert(body) or
                self.sw.insert(body) or self.se.insert(body))