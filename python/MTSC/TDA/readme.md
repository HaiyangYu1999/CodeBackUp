## TDA algorithm

##### *Haiyang Yu*

### This directory contains all the files about TDA.

#### You may run these Python and R files in order as below:

+ **`dataSplit.py`**

  From `RawData.txt` to `TrainRawData.csv` and `TestRawData.csv`

+ **`dataNormalization.py`**        

  In order to get `TrainDataNormalized.csv`, `TrainSetClassification.csv`, `TestDataNormalized.csv` and `TestSetClassification.csv`

+ **`dataToPointClouds.py` and `CloudsClassification.py `**       

  In order to get `TrainCloudMatrix.txt`, `TestCloudMatrix.txt`, `TrainCloudClass.txt` and `TestCloudClass.txt`

+ **`PersistenceDiagramAndW-Dist.R`**

  In order to get `WassersteinDistMatrix.csv`

+ **`knn.py`**

  To get the classification prediction and a tuple of (accuracy, sensitivity,specificity) 

#### Running Time Compare

+ You can call the function `timeTestGenerator()` in `dataToPointClouds.py`. In order to get the directory `./TimeTest/`.

+ `TimeWholeLoaded.R` and `TimeSeparatelyLoaded.R` allow you to compare the running time expense. Function `loadWhole()` loads all the clouds in `./TimeTest/` into RAM at the very beginning. Function `loadSeparately()` loads the cloud at every iteration. 

+ You could run `TimeTestIteration.bat` on Windows Command Prompt to test the time expense. Time expense data are recorded in `./RunningTimeCmp/`