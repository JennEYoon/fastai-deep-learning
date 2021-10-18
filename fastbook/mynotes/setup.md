# To Setup, on my laptop, CPU conda env, fastai20.  

Ubuntu - conda env "fastai20" created.   
Need to load book content, fastbook.  But init.py requires Cuda GPU.  
Load version without, look at forum.   

Docker Image - only for GPU, install Nvidea Cuda docker image first - not recommended for class CPU users.  
CPU users - install miniconda or anaconda.  

fastai20 env setup on Ubuntu done.  
To install book:  
>conda activate fastai20  
>conda install fastbook 
>?  Did yesterday, seems to install into library. Check env path.  

DataBlock class study  

dataLoader thin class study  

--- 

# Setup notes for fastai app1, notebook2.  

Need to use GPU for training.  Just using environment.yml does not work.  Packages assume GPU.  
Try using alternative GPU service to Google.  
After it is trained and app is developed, can serve up on CPU, MyBinder.org app.  
Can't load on my laptop CPU as is.  

Docker image available -- may be better.  

Need software "fastai" and content from book "fastbook"  
C Windows - removed all conda environments except base, python = 3.6
Nov 30, 2020. 

pip freeze > requirements.txt  allows you to save every library loaded with versions.  
Use to create a complete environment.  
May still need to load full fastbook each time.  
Fastbook setup file many have more information.  

***On Colab, run fastbook while in CPU engine, then export requirement***  
Copy to my CPU laptop.  
