import pytesseract
import cv2
import os
#import flair 
#from flair.data import Sentence 
#from flair.models import SequenceTagger 
#rcParams['figure.figsize'] = 8, 16

from PIL import Image, ImageEnhance, ImageFilter
#im = Image.open(os.getcwd()+'/src/pan_card/text/pan.jpeg')
def extract_text():
   text = pytesseract.image_to_string(Image.open(os.getcwd()+'/src/pan_card/text/pan.jpeg'))
   print(text)

