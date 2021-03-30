import math
from src.publay_net import add_text
from scipy.spatial import distance as dist
def calculate_distance(images):
   for i, (_, image) in enumerate(images.items()):
      bef_bbox=0
      after_bbox=0
      count=1
      Label='space'
            
      for annotation in image['annotations']:
         bef_bbox=after_bbox
        
         if count!=1:
            after_bbox=dist.euclidean((temp[0], temp[1]), (annotation['bbox'][0],annotation['bbox'][1]))
            temp=annotation['bbox']
            res=[bef_bbox,after_bbox]
            add_text.add(flag,res,Label)
            #print(bef_bbox,after_bbox)
            #print_bbox(bef_bbox,after_bbox)
         else:
            temp=annotation['bbox']
            count+=1
         flag=annotation   
         #print(annotation['bbox'])
      add_text.add(flag,res,Label)    
    #print_bbox(after_bbox,0)
       

