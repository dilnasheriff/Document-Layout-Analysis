from setuptools import setup

setup(
   name='DLA',
   version='1.0',
   description='improved feature extraction techniques',
   author='Batch 6 CSE G2',
   author_email='dilnasheriff78@gmail.com',
   packages=['DLA'],  #same as name
   install_requires=['flair','tesseract','selenium','cv2'], #external packages as dependencies
   
)
