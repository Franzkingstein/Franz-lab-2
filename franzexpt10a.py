class Rectangle:
    def __init__ (self,length,breadth):

     self.length = length
     self.bredth = breadth
    def __add__(self,other):
       combined_length = self.length+other.length
       combined_length = self.breadth+other.breadth
       return Rectange(combined_length,combined_breadth)
    
    def __str__(self):
       return f"Length is {self.length}  and breadth is {self.breadth}" 
    
    def __eq__(self,other):
       return self.length == other.length and self.bredth == other.bredth 
    def __lt__(self,other):
       return self.length*self.bredth > other.breadth*other.length 
    
    def __gt__(self,other):
       return self.length*self.bredth < other.breadth*other.length
    
    def __le__(self,other):
       return self.length*self.bredth <= other.breadth*other.length
    
    def __ge__(self,other):
       return self.length*self.bredth >= other.breadth*other.length
r1 = Rectangle     