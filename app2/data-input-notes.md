# Combine information on data input to one place.  

1) Local Ubuntu directory  


2) Google Coloab - external directory (mounted Google Drive)  
   * Install libraries  
   * Save kaggle.json to ~/.kaggle/  Home is user root?  No access to system root  //root or /bin/  
   * Easy way to upload full data folder?  Using clicks?  
   * Easy way to connect Google Drive (mounted) data folder?  Using pathlib?  
   * Kaggle API, how to specify path other than default?  
   * Can I upload downloaded kaggle data folder directly to Google Colab instance?  
   * Already saved kaggle.json to Google Drive root and "Colab Notebooks" path.
   * bulldozers data folder also saved to "Colab Notebooks" path



3) Amazon AWS - external, saved config directory
  * Install libaries  
  * Save ~/.kaggle folder to home, .kaggle private folder, kaggle.json file write key to it. Home is user root, not system root.  
  * Save untar_data() to server, ~/.fastai/data  path.  Home is usr root.  
