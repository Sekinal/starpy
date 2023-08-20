from __future__ import annotations
import numpy as np

class Quadrant:
    """A quadrant datatype. It subdivides the space into smaller regions.
    This quadrant is defined by a lower left point located at (x_1, y_1) and an upper
    right point located at (x_2, y_2).
    """
    def __init__(self,
                 lower_left_point: np.ndarray,
                 upper_left_point: np.ndarray) -> None:
        
        self.lower_left_point = lower_left_point
        self.upper_right_point = upper_left_point
        self.length = self.upper_right_point[0] - self.lower_left_point[0]
    
    def contains(self, point: np.ndarray) -> bool:
        """A method that checks if the given point located at (x, y) is contained within
        the quadrant region.

        Args:
            point (np.ndarray): A formatted numpy array in the form of (x, y).

        Returns:
            bool: Returns either True if the given point is within the quadrant or False
            if it's not
        """
        if (point[0] >= self.lower_left_point[0] and
            point[0] <= self.upper_right_point[0]):
            if (point[1] >= self.lower_left_point[1] and
                point[1] <= self.upper_right_point[1]):
                return True
        else:
            return False
    
    def new_nw_quadrant(self) -> Quadrant:
        """A method that creates a new NW subquadrant in the specified quadrant.

        Returns:
            Quadrant: A new quadrant in a subregion of the main quadrant.
        """
        
        new_y_1 = self.lower_left_point[1] + self.length/2
        new_x_2 = self.upper_right_point[0] - self.length/2
        new_lower_left_point = np.array([self.lower_left_point[0], new_y_1])
        new_upper_right_point = np.array([new_x_2, self.upper_right_point[1]])
        
        return Quadrant(new_lower_left_point, new_upper_right_point)
    
    def new_ne_quadrant(self) -> Quadrant:
        """A method that creates a new NE subquadrant in the specified quadrant.

        Returns:
            Quadrant: A new quadrant in a subregion of the main quadrant.
        """
        
        new_x_1 = self.lower_left_point[0] + self.length/2
        new_y_1 = self.lower_left_point[1] + self.length/2
        new_lower_left_point = np.array([new_x_1, new_y_1])
        
        
        return Quadrant(new_lower_left_point, self.upper_right_point)
    
    def new_sw_quadrant(self):
        """A method that creates a new SW subquadrant in the specified quadrant.

        Returns:
            Quadrant: A new quadrant in a subregion of the main quadrant.
        """
        new_x_2 = self.upper_right_point[0] - self.length/2
        new_y_2 = self.upper_right_point[1] - self.length/2
        new_upper_right_point = np.array([new_x_2, new_y_2])
        
        return Quadrant(self.lower_left_point, new_upper_right_point)
    
    def new_se_quadrant(self):
        """A method that creates a new SE subquadrant in the specified quadrant.

        Returns:
            Quadrant: A new quadrant in a subregion of the main quadrant.
        """
        new_x_1 = self.lower_left_point[0] + self.length/2
        new_y_2 = self.upper_right_point[1] - self.length/2
        new_lower_left_quadrant = np.array([new_x_1, self.lower_left_point[1]])
        new_upper_right_quadrant = np.array([self.upper_right_point[0], new_y_2])
        
        return Quadrant(new_lower_left_quadrant, new_upper_right_quadrant)

class Body:
    """A body datatype. This represents an individual or a system of bodies in the
    physical simulation, containing all of its relevant physical data.
    """
    def __init__(self, mass: float, position: np.ndarray) -> None:
        self.mass = mass
        self.spatial_data = np.array([position, # Position
                                     [0, 0], # Velocity
                                     [0, 0]]) # Acceleration
    
    def is_in_quadrant(self, quadrant: Quadrant) -> bool:
        """A method that checks if the given body is contained within the specified
        quadrant.

        Args:
            quadrant (Quadrant): A quadrant object.

        Returns:
            bool: Returns either True or False depending on whether or not the body is
            contained within the given quadrant.
        """                
        is_contained = quadrant.contains(self.spatial_data[0])
        return is_contained

    def add(self, second_body: Body) -> Body:
        """A method that calculates the center of mass given another body, and creates
        a new body on the given data.

        Args:
            second_body (Body): A physical body.

        Returns:
            Body: A new body composed of the input body and the actual body.
        """
        
        m_1, x_1, y_1 = self.mass, self.spatial_data[0][0], self.spatial_data[0][1]
        m_2, x_2, y_2 = (second_body.mass,
                         second_body.spatial_data[0][0],
                         second_body.spatial_data[0][1])
        
        m_cm = m_1 + m_2
        x_cm = (x_1*m_1 + x_2*m_2)/m_cm
        y_cm = (y_1*m_1 + y_2*m_2)/m_cm
        position_cm = np.array([x_cm, y_cm])
        
        return Body(m_cm, position_cm)

    def calculate_spatial_data(self, second_body) -> None:
        """A function that calculates the current acceleration due to gravitational
        interaction with another body.

        Args:
            second_body (Body): Another body in gravitational interaction with the
            current body.
        """
        G = 6.67430e-11 # Gravitational constant
        
        position_vector = np.array(self.spatial_data[0] - second_body.spatial_data[0])
        position_vector_norm = np.linalg.norm(position_vector)
        unit_position_vector = position_vector/position_vector_norm
        
        gravitational_force_scalar = (G*second_body.mass)/(position_vector_norm**2)
        
        self.spatial_data[2] = -gravitational_force_scalar*unit_position_vector
        
        delta_t = 25000
        self.spatial_data[1] = self.spatial_data[1] + delta_t*self.spatial_data[2]
        self.spatial_data[0] = self.spatial_data[0] + delta_t*self.spatial_data[1]
        
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
            # If there is at least one body, we have to divide the tree and insert
            # the body
            self.divide()
            self.nw.insert(self.body)
            self.ne.insert(self.body)
            self.sw.insert(self.body)
            self.se.insert(self.body)
            
        self.body = body.add(self.body)
        
        return (self.nw.insert(body) or self.ne.insert(body) or
                self.sw.insert(body) or self.se.insert(body))

    def update_force(self, body):
        if not self.divided:
            # Check if the node is an external node
            pass