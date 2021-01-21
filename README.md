# Hypersim PyTorch Dataloader 

![Alt text](img.png?raw=true "Image")
![Alt text](label.png?raw=true "Label")


Light weight dataloader to fully setup the MLHypersim dataset for semantic segmentation.  

The dataset relevant for semantic segmentation can be downloaded with the ```script/download.py```  

This file downloads each file stored in the ```script/urls.py``` list.


| Dataset         | Parameters    | Values                                 |
|-----------------|---------------|----------------------------------------|
| **ML-Hypersim** | Images Train: | 74619 (total)                          |
|                 | Images Val:   |                                        |
|                 | Annotations:  | NYU-40                                 |
|                 | Optical Flow: | False                                  |
|                 | Depth:        | True                                   |
|                 | Resolution:   | 1024×768                               |
|                 | Total Size:   | 247GB                                  |


## Downloading the dataset
```
python script/download --destination=/your/large/ssd
```

After downloading the needed images and labels are extracted and the zip file is deleted to save memory.  


## Testing the dataset
To run test the actual dataset the following packages are needed:
[ ```imageio```, ```PIL```, ```torchvision```, ```torch``` ]

Simply set the correct root dir, standard data augmentation options. 
Currently the validation dataset is created by setting the last N-frames for each scene as the validation dataset given that now standardized train/val/test split is available. 


Test the dataloader by inserting the correct path in def test() function and call the ```ml_hypersim.py``` script
```
python cfg/ml_hypersim.py 
```

The mask and image are stored in the repository. 

