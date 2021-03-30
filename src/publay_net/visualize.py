# Function to visulaize the annotation
import parameters
import os
import json
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image
from PIL import ImageFont, ImageDraw

def visualization(images):
    ''' Draws the segmentation, bounding box, and label of each annotation
    '''
 
    fig=plt.figure(figsize=(16, 100))
    for i, (_, image) in enumerate(images.items()):
        with Image.open(image['file_name']) as img:
            ax = plt.subplot(int(len(images) / 2), 2, i + 1)
            with open(os.getcwd()+'/src/publay_net/raw.json', 'r') as fp:
              samples = json.load(fp)
            draw = ImageDraw.Draw(img, 'RGBA')
            colours,font=parameters.colours,parameters.font
            

            for annotation in image['annotations']:
               # Draw bbox
               #an_count+=1
               #category.append(annotation['category_id'])
               #add_value(annotation['id'],annotation['bbox'],bounding_box)
               #print(category)
               draw.rectangle(
                 (annotation['bbox'][0],
                 annotation['bbox'][1],
                 annotation['bbox'][0] + annotation['bbox'][2],
                 annotation['bbox'][1] + annotation['bbox'][3]),
                 outline=colours[annotation['category_id'] - 1]+ (255,),width=2)
            
        
               #to draw box around the category title
               w, h = draw.textsize(text=samples['categories'][annotation['category_id'] - 1]['name'],font=font)
               if annotation['bbox'][3] < h:
                   draw.rectangle(
                      (annotation['bbox'][0] + annotation['bbox'][2],
                      annotation['bbox'][1],
                      annotation['bbox'][0] + annotation['bbox'][2] + w,
                      annotation['bbox'][1] + h),
                      fill=(64, 64, 64, 255)
                      )
                   draw.text(
                      (annotation['bbox'][0] + annotation['bbox'][2],
                      annotation['bbox'][1]),
                      text=samples['categories'][annotation['category_id'] - 1]['name'],
                      fill=(255, 255, 255, 255),
                      font=font
                      )
               else:
                  draw.rectangle(
                    (annotation['bbox'][0],
                    annotation['bbox'][1],
                    annotation['bbox'][0] + w,
                    annotation['bbox'][1] + h),
                    fill=(64, 64, 64, 255)
                    )
                  draw.text(
                   (annotation['bbox'][0],
                   annotation['bbox'][1]),
                  text=samples['categories'][annotation['category_id'] - 1]['name'],
                  fill=(255, 255, 255, 255),
                  font=font
                    )
        
            
            ax.axis('off')
            ax.imshow(np.array(img))
            
    plt.subplots_adjust(hspace=0, wspace=0)
    plt.savefig("demo.png")
    
    image = Image.open('demo.png')
    image.show()


    