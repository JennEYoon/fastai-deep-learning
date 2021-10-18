# Chapter 4 presentation outline  


### Show folder path in Google Drive, sample MNIST data, 3, 7  

threes = (path/'train'/'3').ls().sorted()
Threes

Im3 show image
Black background, hot-3.  

array(im3)[4:10, 4:10]  shows numpy array  
dtype = uint8, talk about this tye, all postiive numbers, 0 to 255, 8 bit unsigned.  

Switch to tensors (PyTorch)  
im3_t = tensor(im3)  
df.pd.DataFrame(im3_t[4:15, 4:22])
Set style - switch black and white, make background white. Matplotlib style command

Comment about how a computer "sees" the written number "3."  
Innuits don't have a fixed direction, sees a same object in multiple directions without turning it around.  

Stack all images of 3's together  

Stack all images of 7's together.  

Python list comprehension.  

Divide by 255 to make the distance metric (later) go from 0 to 1, probability scale.  
stacked_threes = torch.stack(three_tensors).float()/255  

Take the mean of all stacked images, show  

Get fuzzy looking "mean" of 3'd and 7's.  
mean3 = stacked_threes.mean(0)

Comparing test image with "summation" image of 3's or 7's.  

"Distance" metic, how to compute.  
Absolute value distance, RMSE distance  (same as for OLS)  

def is_3(x):  returns true or false, based on cut-off number (shorter distance than 7's).  

def is_y(x):  same 

Gradient is a slope, rise over run  

Toy example with X**2 function  

Derivative, rate of change, backward pass, feedback to tell model how much to adjust weights.  

yt.backward()  
PyTorch calculates the value of the derivate function for us. 


f(x**2)  solve  
Answer 2x  (math)  
Answer with value, at x = 3 point:  6. 
PyTorch gives us numerical answers at a supplied point.  

