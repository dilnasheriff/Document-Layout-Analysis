import math
from src.publay_net import add_text
def Hypotenuse(X,Y):
      deltaY = ((X)-(0))**2
      deltaX = ((Y)-(0))**2
      hyp = (deltaX+deltaY)**(1/2)
      return (round(hyp,2))
def Adjacent(X):
      deltaY = ((X)-(0))**2
      deltaX = ((0)-(0))**2
      adj = (deltaX+deltaY)**(1/2)
      return (round(adj,2))
 
def Cosine_angle(images):
        for i, (_, image) in enumerate(images.items()):
            
            for annotation in image['annotations']:
                div1=Adjacent(annotation['bbox'][0])
                div2=Hypotenuse(annotation['bbox'][0],annotation['bbox'][1])
                angle=int(round(math.degrees(math.acos(div1/div2))))
                Label='cosAngle'
                add_text.add(annotation,angle,Label)