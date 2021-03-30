import pytesseract
from PIL import Image
from src.publay_net import add_text
#import flair 
#from flair.data import Sentence 
#from flair.models import SequenceTagger
#Import segtok library to split the paragraph into sentences
#from segtok.segmenter import split_single

import os
def extract_text(images,option):
       #to extract text
       for i, (_, image) in enumerate(images.items()):
           with Image.open(image['file_name']) as img:
               for annotation in image['annotations']:
                     crop_img = img.crop((annotation['bbox'][0],   #crop the image
                     annotation['bbox'][1],
                     annotation['bbox'][0] + annotation['bbox'][2],
                     annotation['bbox'][1] + annotation['bbox'][3]))
                     #extract only if category is text,title or list
                     if(annotation['category_id']==1 or annotation['category_id']==2 or annotation['category_id']==3):
                         e_text = pytesseract.image_to_string(crop_img)
                         add_text.add(annotation,e_text,'text')
                         #print(text)
                         
                         if(option==2):
                             
                             s = Sentence(text)
                             tagger_NER= SequenceTagger.load('ner') 

                             # run NER over sentence 
                             tagger_NER.predict(s) 
 
                             print('The following NER tags are found:\n') 
                             ner=[]
                             # iterate and print 
                             for entity in s.get_spans('ner'):
                                 ner.append(entity)
                             print(ner)
                             add_text.add(annotation,ner,'NER')
