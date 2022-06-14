import numbers
import param
from param import Parameter,Integer, Parameterized,Number


class Square(Parameterized):
    side1 = Number(doc="side1", default=1.,units="m")
    side2 = Number(doc="side2",default=1.,units="m")
    
    # side1 = Parameter(name="len1", default=1)
    # side2 = Parameter(name="len1", default=1)

p1 = Number(doc="side1", default=1.)

print(p1)
print(p1.doc)
  

sq1 =Square(side1=5, side2=4)

print(sq1)

print(sq1.param.side1.doc)
print(sq1.param.side1.units)

