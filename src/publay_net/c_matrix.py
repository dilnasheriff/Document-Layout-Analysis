import pandas as pd
from matplotlib import pyplot as pl
import random
# confusion matrix in sklearn
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sn

def confusion_mat(images):
  category=[]
  for i, (_, image) in enumerate(images.items()):
        for annotation in image['annotations']:
            category.append(annotation['category_id'])
  n=random.sample(category,len(category))
  
  classes=['text','title','list','table','figure']
  
  
  
  df_cm = pd.DataFrame(confusion_matrix(category,n), range(5), range(5))
  print(df_cm)
  sn.set(font_scale=1.4) # for label size
  sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size

  pl.show() 