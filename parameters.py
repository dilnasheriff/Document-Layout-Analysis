# Define colour code
from PIL import ImageFont
from matplotlib import pyplot as plt
import os
colours = {0: (255, 0, 0), #title
             1: (0, 255, 0),  #text
             2: (0, 0, 255),  #list
             3: (255, 255, 0),#table 
             4: (0, 255, 255)} #figure
font = ImageFont.truetype(os.getcwd() +"/data/images_publaynet/DejaVuSans.ttf", 15)      
   #print()    
   