
from dxfwrite import DXFEngine as dxf

for i in range(12):




    drawing = dxf.drawing('layer%s.dxf' % i)
    
    drawing.add(dxf.polyline(points=[(10,0),(10,60),(50,60),(50,0),(10,0)]))
    
    if(i > 3):
        drawing.add(dxf.circle(radius=(i-3)*2+4, center=(17,30)))
    
    drawing.add(dxf.circle(radius=i*2+4, center=(40,20)))
    
    if(i > 4):
        drawing.add(dxf.circle(radius=(i-4)*2+4, center=(35,60)))
    

    drawing.save()