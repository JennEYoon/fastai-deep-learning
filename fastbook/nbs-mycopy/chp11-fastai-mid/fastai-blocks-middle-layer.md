# Chp 11, Fastai Middel Layer, DataBlock, DataLoaders  

Summarize my notes on chp 11 and reading source code for fastai DataBlock, DataLoaders  

Chp 11 still totally confusing.  
Each data set needs custom code to get it into DataBlocks API.  
Samples can be copied, but each case is unique.  

Planet, images are from train folder.  get_files, selects random draw of image files.  
y-labels, lookup from CSV table, matching chosen image file's name col, read off labels, then split on space.  
transforms, y-flip is OK for categorizing, but not for location based prediction. 
resize 256 to 224 to match pretrained model?  





