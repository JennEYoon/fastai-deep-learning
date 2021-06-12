# my reading notes

Date: Jan 25, 2021  
Author: Jennifer Yoon  

### Notes:  

Main development is residual layer, 1x1 identity add residual weights to later layer, skipped layers.  
Won 2015 ImageNet competition, COCO competition.  

Image segmentation - partitioning pixels for that pixels belonging to an object is tagged as part of that object.  
Creates polygons, "segments" with object identification.  

Takes a while to run 20 layers at the end.  Try 100 layers, but with some twicks.  Maybe float16 changed data type to speed it up.  
Smooth SGD image impressive.  Rough valleys without residual network.  

<img alt="Impact of ResNet on loss landscape" width="600" caption="Impact of ResNet on loss landscape (courtesy of Hao Li et al.)" id="resnet_surface" src="att_00044.png">

### More:  

Try reproducing notebook without pre-populated code.  
Try on other datasets.  
Study loading data from URL, datasets, dataLoader, chp11 munging datasets.  
\
