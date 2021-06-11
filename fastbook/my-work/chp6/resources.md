# Fastai Chp 6 talk, resources  

 * fastai chp 6 notebook, run on Google Colab:  
   - https://github.com/JennEYoon/deep-learning/blob/main/fastai-20/fastbook/06_multicat_JY_full2.ipynb  

### 1. Multiclass Classification  

Multi-label classification refers to the problem of identifying the categories of objects in images that may not contain exactly one type of object. There may be more than one kind of object, or there may be no objects at all in the classes that you are looking for.

For instance, this would have been a great approach for our bear classifier. One problem with the bear classifier that we rolled out in <

In practice, we have not seen many examples of people training multi-label classifiers for this purpose—but we very often see both users and developers complaining about this problem. It appears that this simple solution is not at all widely understood or appreciated! Because in practice it is probably more common to have some images with zero matches or more than one match, we should probably expect in practice that multi-label classifiers are more widely applicable than single-label classifiers.

First, let's see what a multi-label dataset looks like, then we'll explain how to get it ready for our model. You'll see that the architecture of the model does not change from the last chapter; only the loss function does. Let's start with the data.

### 2. Regression, continuous variable  

 * 2.a  Middle of face, not nose.   

It's easy to think of deep learning models as being classified into domains, like computer vision, NLP, and so forth. And indeed, that's how fastai classifies its applications—largely because that's how most people are used to thinking of things.

But really, that's hiding a more interesting and deeper perspective. A model is defined by its independent and dependent variables, along with its loss function. That means that there's really a far wider array of models than just the simple domain-based split. Perhaps we have an independent variable that's an image, and a dependent that's text (e.g., generating a caption from an image); or perhaps we have an independent variable that's text and dependent that's an image (e.g., generating an image from a caption—which is actually possible for deep learning to do!); or perhaps we've got images, texts, and tabular data as independent variables, and we're trying to predict product purchases... the possibilities really are endless.

To be able to move beyond fixed applications, to crafting your own novel solutions to novel problems, it helps to really understand the data block API (and maybe also the mid-tier API, which we'll see later in the book). As an example, let's consider the problem of image regression. This refers to learning from a dataset where the independent variable is an image, and the dependent variable is one or more floats. Often we see people treat image regression as a whole separate application—but as you'll see here, we can treat it as just another CNN on top of the data block API.

We're going to jump straight to a somewhat tricky variant of image regression, because we know you're ready for it! We're going to do a key point model. A key point refers to a specific location represented in an image—in this case, we'll use images of people and we'll be looking for the center of the person's face in each image. That means we'll actually be predicting two values for each image: the row and column of the face center.

### 3. Data Pre-Processing, Pandas, Regular Expression, Fastai  
  * Pandas cheatsheet  
    - https://docs.google.com/viewer?url=https%3A%2F%2Fpandas.pydata.org%2FPandas_Cheat_Sheet.pdf&embedded=true&chrome=false&dov=1  
  * Vanderplas book  
    - https://github.com/jakevdp/PythonDataScienceHandbook  
  * McKinney book  
    - https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/ref=asc_df_1491957662/?tag=hyprod-20&linkCode=df0&hvadid=312140868236&hvpos=&hvnetw=g&hvrand=10272796695638732188&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9007587&hvtargid=pla-396828636441&psc=1  
  * Regular Expression website - also many games  
    - https://docs.python.org/3/library/re.html  
  * Fastai DataBlock, Data Loader, Tutorials  
    - https://docs.fast.ai/  

### 4. Group Project Proposal - Planet 2017 Kaggle Challenge  
 * Show how to download from Kaggle  
   - https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/data  
   - Project Proposal:  https://github.com/JennEYoon/geo-ml/blob/main/rainforest/proposal.md  
   - Notice 2 student projects links, on my proposal page.  
   - Slack new channel - join by browsing for channel, **Amazon Rainforest**  
 * tif, jpg, and convert to rgb  
   ```python  
   from PIL import Image
   im = Image.open(f)
   #im  # Get error message
   print(im.mode)  # Output: CMYK

   if im.mode == 'CMYK': 
       rgb_image = im.convert('RGB')
    
   rgb_image  
   # Add .show() if not running in a Jupyter notebook
   ```
   - sample notebook:  https://github.com/JennEYoon/geo-ml/blob/main/rainforest/nbs-planet/data-sample-test1.ipynb   
 * My geo-ml repo: https://github.com/JennEYoon/geo-ml  
   - Caution: May move folders around and temporarily rename repo to perform cleanup.  
   - Repo size getting close to 1 GB, made the mistake of pushing many image files.  
 * \-\-\-    
 * Contact info: Jennifer Yoon, jenneyoon@gmail.com, datasciY.com  
   Github:  https://github.com/JennEYoon   
   Leesburg, Virginia, USA   
   
