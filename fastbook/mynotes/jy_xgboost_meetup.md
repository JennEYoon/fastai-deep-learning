# Meetup Oct 2021, XGBoost  

 * Presented in a paper for the first time in 2016.  
   - https://arxiv.org/pdf/1603.02754.pdf 
   - Tianqi Chen and Carlos Guestrin, XGBoost: A Scalable Tree Boosting System.  

### Overview   

XGBoost is used primarily on tabular data or on structured data kept in databases.  XGBoost provides a paper and open-source library with optimization routines. After the paper and software was unveiled, many top Kaggle competitions for tabular data used XGBoost alone or with natural language processing for text data to win.  X stands for extreme gradient descent.  Library allows easy way to process large dataset and run the job in parallel on multiple CPUs. Processing time decreases almost linearly with additional CPUs.  Boosting is a supervised learning task.  Common uses are regression (predict sales price) and category identification.  Category text names are numericalized in "embeddings".  Example, (low, medium, high) values can be encoded as (0, 1, 2).

Fastbook chp9: Tabular Data Deep Dive.
Tabular data primarily uses an ensemble of decision trees models, Random Forest or XGBoost.  Deep learning models sometimes works a little better.  The advantage of tree-based models is their ease of interpretability. Easier to answer questions like, "which columns (features) in the dataset were the most important?  How are the dependent variable (column, features) related (correlated)?  Which features were most important for select datasets (rows)?

XGBoost optimizer necessary points: 
 * is sparce tree aware 
 * weighted quantile search capable for approximate learning
 * cache access patterns and
 * data compression and sharding algorithms essential  

These improvements help solve very large data models with minimum resources.  Linear like growth in resources for improvements in time. 

### Boosting vs Random Forest  
\(from XGBOOST docs:  https://xgboost.readthedocs.io/en/latest/tutorials/rf.html\)  
"XGBoost is normally used to train gradient-boosted decision trees and other gradient boosted models. Random Forests use the same model representation and inference, as gradient-boosted decision trees, but a different training algorithm. One can use XGBoost to train a standalone random forest or use random forest as a base model for gradient boosting."   

Boosting trees learn sequentially. Earlier trees fit simpler models.  Later trees input resulting errors and fit complex models for finer predictions.  The "Boosting" is used to describe interdependent trees model.  


### XGBoost software library 
Python Dask (parallel) application available.  
Supports multiple languages (Python, R, Scala, Julia)   

### My contact  
Jennifer E. Yoon  github: https://github.com/JennEYoon/  
email:  jenneyoon@gmail.com  
