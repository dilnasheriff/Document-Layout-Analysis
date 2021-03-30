from src.publay_net import cos
from src.publay_net import space_bb
from src.publay_net import text_ner
from src.publay_net import visualize
from src.publay_net import space_bb
from src.publay_net import c_matrix
from src.publay_net import categorize
from src.pan_card.Google_Image_Scraper_master import roi
from src.pan_card.ROI import pan
from src.pan_card.text import flair
import json
import os
class PANOCR():
    def choice(self,i):
        switcher = {
            1:lambda:roi.init(),
            3:lambda:pan.main1(),
            2:lambda:flair.extract_text() 
            
        }
        func = switcher.get(i, lambda: 'Invalid')
        func()
    def driver1(self):
        value=int(input("Press 1.IMAGE DOWNLOAD 2.EXTRACT TEXT 3.BACKGROUND SUBTRACTION"))
        extract.choice(value)

class Publaynet():
    # Parse the JSON file and read all the images and labels
    def __init__(self,images = {}):
        self.images=images
    def parse_json(self):
        with open('/home/kafil/Desktop/DLA/src/publay_net/raw.json', 'r') as fp:
            samples = json.load(fp)
        # Index images
        
 
        #appending filename with its annotation
        for image in samples['images']:
          self.images[image['id']] = {'file_name': os.getcwd() +"/data/images_publaynet/"+ image['file_name'], 'annotations': []}
          
        for ann in samples['annotations']:
          self.images[ann['image_id']]['annotations'].append(ann)
        #print(self.images)

    def choice(self,i):
        switcher = {
            1:lambda:text_ner.extract_text(self.images,1),
            2:lambda:text_ner.extract_text(self.images,2),
            3: lambda: visualize.visualization(self.images),
            4: lambda: cos.Cosine_angle(self.images),
            5: lambda: space_bb.calculate_distance(self.images),
            6: lambda: c_matrix.confusion_mat(self.images),
            7: lambda: categorize.divide(self.images)
            
        }
        func = switcher.get(i, lambda: 'Invalid')
        func()


    def driver(self):
        extractor.parse_json()
        value=int(input("1.TEXT 2.NER 3.VISULAIZE DATASET 4.COSINE 5.REGION-SPACE 6.CONFUSION MATRIX  7.CATEGORIZE...."))
        extractor.choice(value)
        
    

if __name__ == "__main__":
    case=1
    while(case):
        case=int(input("Press 1 for PAN CARD, 2 for Publaynet,0 for exit...."))
        if(case==1):
            extract=PANOCR()
            extract.driver1()
   
        elif(case==2):
            extractor=Publaynet()
            #extractor.parse_json()   
            extractor.driver()
        else:
            break
