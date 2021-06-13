# Colab - working with, fastai 2020 class


#I found out how to add conda in colabs (2019 v): kurianbenoy
!wget -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
!chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
!bash ./Anaconda3-5.1.0-Linux-x86_64.sh -b -f -p /usr/local
!conda install -y --prefix /usr/local -c pytorch
!conda install -c fastai fastai

#If you want just fast.ai, you could use this (2019 v): Ajay Arasanipalai
!curl https://course-v3.fast.ai/setup/colab | bash

"""
Jonathan Aghachi
Nov 3, '18
Here is a simple ‘for loop’ for helping make image folders more automatically.

All you need to do is create a “data/urls” folder where your’re running your notebook 
and upload all the link files into the urls folder.

Folder names will be named whatever you name the url txt files.

Note: This isn't to take away from highlighting the fact that you can run things 
out of order in notebooks, I just got a bit lazy in changing lots of code blocks, 
so this 'for loop' was born.

EDIT: variable path to images is now "pathI" instead of "path" just fyi.
"""

folderNames = []

pathU = 'data/urls/'
 
files = os.listdir(pathU)
for name in files:
    folderNames.append(os.path.splitext(name)[0])

pathI = Path('data/images')

for title in folderNames:
    dest = pathI/title
    filename = title + '.txt'
    dest.mkdir(parents=True, exist_ok=True)
    download_images('data/urls/' + filename, dest, max_pics=200,max_workers=0)

### ------------------------------------------------------------------ ###

# How to change path for reading image files into fastai model, DataBlocks, DataLoaders  

# untar_data download to a different location: 
# Pass in "dest" parameter to "untar_data". 
# So in your case untar_data(URLs.PETS, dest=".") same location as notebook.  

from fastai.vision.all import *
path = untar_data(URLs.PETS)
path = untar_data(URLs.PETS, dest="G:/course-v3-master");

# To see what is in our dataset we can use the ls method:

Path.BASE_PATH = path
path.ls()
# output, 
# [Path('annotations'),Path('images')]
# We can see that this dataset provides us with images and annotations directories.

(path/"images").ls()
# output, 
# (#7393) [Path('images/pomeranian_79.jpg'),Path('images/scottish_terrier_133.jpg'),Path('images/american_pit_bull_terrier_124.jpg'),Path('images/german_shorthaired_96.jpg'),Path('images/Sphynx_14.jpg'),Path('images/scottish_terrier_52.jpg'),Path('images/beagle_74.jpg'),Path('images/boxer_122.jpg'),Path('images/saint_bernard_47.jpg'),Path('images/scottish_terrier_193.jpg')...]

""" 
L is a fastai collection, Python list type with added methods.  
Most functions and methods in fastai that return a collection use a class called L. L can be thought of as an enhanced version of the ordinary Python list type, with added conveniences for common operations.
"""

fname = (path/"images").ls()[0]
# Show first item in collection, name of file, not load image into memory. 

# Use regular expression to rename image files?  
re.findall(r'(.+)_\d+.jpg$', fname.name)
# ['pomeranian']

# DataBlock and DataLoaders next:  
pets = DataBlock(blocks = (ImageBlock, CategoryBlock),
                 get_items=get_image_files, 
                 splitter=RandomSplitter(seed=42),
                 get_y=using_attr(RegexLabeller(r'(.+)_\d+.jpg$'), 'name'),
                 item_tfms=Resize(460),
                 batch_tfms=aug_transforms(size=224, min_scale=0.75))
dls = pets.dataloaders(path/"images")


# Check data block, images were loaded correctly, "show_batch() method."
dls.show_batch(nrows=1, ncols=3)

# To debug [data block], we encourage you to use the summary method. pets1.summary(path/"images")
pets1 = DataBlock(blocks = (ImageBlock, CategoryBlock),
                 get_items=get_image_files, 
                 splitter=RandomSplitter(seed=42),
                 get_y=using_attr(RegexLabeller(r'(.+)_\d+.jpg$'), 'name'))
pets1.summary(path/"images")  # Summary here
# output, 
# shows build steps.  

# Once you got to here, train a simple CNN model to establish a baseline.  
# resnet34 seems to be baked into fastai, don't need to download a pretrained model.  
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(2)

# Viewing Activations and Labels
# Let's take a look at the activations of our model. To actually get a batch of 
# real data from our DataLoaders, we can use the one_batch method:

x,y = dls.one_batch()
# As you see, this returns the dependent and independent variables, as a mini-batch. 
# Let's see what is actually contained in our dependent variable [y]:

y
"""
TensorCategory([ 0,  5, 23, 36,  5, 20, 29, 34, 33, 32, 31, 24, 12, 36,  8, 26, 30,  2, 12, 17,  7, 23, 12, 29, 21,  4, 35, 33,  0, 20, 26, 30,  3,  6, 36,  2, 17, 32, 11,  6,  3, 30,  5, 26, 26, 29,  7, 36,
        31, 26, 26,  8, 13, 30, 11, 12, 36, 31, 34, 20, 15,  8,  8, 23], device='cuda:5')
Our batch size is 64, so we have 64 rows in this tensor. Each row is a single integer between 0 and 36, representing our 37 possible pet breeds. 
"""  