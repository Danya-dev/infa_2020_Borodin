import math

class Vector():
    def __init___(self,x , y, z):
        print('vector is created; add x, y, z:')
        self.x = x
        self.y = y
        self.z = z
        
        
    def summ(self, VectorN):
        return Vector(self.x + VectorN.x, self.y + VectorN.y, self.z + VectorN.z)
    
    
    def summe(self, VectorN):
        self.x += VectorN.x
        self.y += VectorN.y
        self.z += VectorN.z
        
        
    def multiply(self, alpha):
        return Vector(self.x * alpha, self.y * alpha, self.z * alpha)
    
    
    def multiplyme(self, alpha):
        self.x *= alpha
        self.y *= alpha
        self.z *= alpha
    def scomult(self, VectorN):
        return self.x * VectorN.x + self.y * VectorN.y + self.z * VectorN.z
    
    
    def vecrot(self,VectorN):
        return Vector(self.y * VectorN.z - self.z * VectorN.y, self.x * VectorN.z- self.z * VectorN.x,
                      self.x * VectorN.y + self.y * VectorN.x)
    
    def vecrotme(self, VectorN):
        self.x = self.y * VectorN.z - self.z * VectorN.y
        self.y = self.x * VectorN.z- self.z * VectorN.x
        self.z = self.x * VectorN.y + self.y * VectorN.x
        
    
    
    
        
