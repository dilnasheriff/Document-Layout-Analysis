from PIL import Image
import os.path, sys
def divide(images):
    img_count=0
    for i, (_, image) in enumerate(images.items()):
      with Image.open(image['file_name']) as img:
        an_count=0
        img_count+=1
        for annotation in image['annotations']:
             an_count+=1
             crop_img = img.crop((annotation['bbox'][0],   #crop the image
             annotation['bbox'][1],
             annotation['bbox'][0] + annotation['bbox'][2],
             annotation['bbox'][1] + annotation['bbox'][3]))
             
             if(annotation['category_id']==1):
               image_path=os.getcwd()+'/src/publay_net/category/text'
               if not os.path.exists(image_path):
                 os.makedirs(image_path)
               crop_img.save(image_path+'/cropped'+str(img_count)+str(an_count)+'.jpg')

             elif(annotation['category_id']==2):
               image_path=os.getcwd()+'/src/publay_net/category/title'
               if not os.path.exists(image_path):
                 os.makedirs(image_path)
               crop_img.save(image_path+'/cropped'+str(img_count)+str(an_count)+'.jpg')
             elif(annotation['category_id']==3):
               image_path=os.getcwd()+'/src/publay_net/category/list'
               if not os.path.exists(image_path):
                 os.makedirs(image_path)
               crop_img.save(image_path+'/cropped'+str(img_count)+str(an_count)+'.jpg')

             elif(annotation['category_id']==4):
               image_path=os.getcwd()+'/src/publay_net/category/table'
               if not os.path.exists(image_path):
                 os.makedirs(image_path)
               crop_img.save(image_path+'/cropped'+str(img_count)+str(an_count)+'.jpg')

             else:
               image_path=os.getcwd()+'/src/publay_net/category/figure'
               if not os.path.exists(image_path):
                 os.makedirs(image_path)
               crop_img.save(image_path+'/cropped'+str(img_count)+str(an_count)+'.jpg')

