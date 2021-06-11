# My notes, chp10 fastai - NLP Deep Dive 

#### Feb 18, 2021 start:  

  * Chp 10 tokenization - to char tokenization on my own using Numpy, then look at PyTorch char tokenization, Udemy class.  
  * Video lesson 8 - finish watching  

  * Lookup Word2Vec.  How is stem identified?  How much is manually fixed?  

  * Breaking up matix into A, B, C blocks by column numbers, look for real world use, how large are the blocks? Do sentence wrapping fit inside most blocks?  

  * Review matrix multiplication in Numpy, breaking up large arrays into column blocks, yet still keeping track of adjacent bordering columns, when calculation, then putting it back into shape.  

  * Image also stack into long rows, then puts back into shape.  But does not break up word wrapping, one long row per image. Sentences are not all the same length, need to keep track of which cell was next at the edges of block.  

  * Sequence Models - Image use cases, lookup movie sequential scenes matching, cropped image putting back together, high res & low res image, in order to produce high res images from low res inputs.  Fill-in missing concreteness in image.  Medical applications, DL image sharper than original image, damaged during cutting.  
