# THYROID-DETECTION-CLASSIFICATION

[![wakatime](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/860a5125-f8c9-410b-adfb-5de83f6d2c5e.svg)](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/860a5125-f8c9-410b-adfb-5de83f6d2c5e)&nbsp;
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://thyroid-detection-pred-sundi.herokuapp.com/)&nbsp;
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/Shashank-Sundi/THYROID-DETECTION-CLASSIFICATION)&nbsp;
![Lines of code](https://img.shields.io/tokei/lines/github/Shashank-Sundi/THYROID-DETECTION-CLASSIFICATION?style=flat)

Machine Learning Project to indentify (classify) whether a patient suffers from Thyroid Disease or not.

<img src="static\images\thyroid-gland.jpg" alt="affair" />
<hr>

## Deployment

The model has been deployed using REST API using flask, on Heroku :  https://thyroid-detection-pred-sundi.herokuapp.com/


## Original Dataset and Python Notebook

Original Dataset : https://github.com/Shashank-Sundi/THYROID-DETECTION-CLASSIFICATION/blob/main/hypothyroid.csv

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/thyroid-prediction.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting if a patient suffers from Thyroid Disease**| `LOGISTIC REG,KNN,SVC,NAIVE BAYES,RANDOM FOREST,XGBOOST` | `Sklearn , Seaborn ,Pandas ,Numpy ,Scipy ,Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1|Extracted dataset from statsmodels package  |
|2| Validated data types of the features and analysed the statistical properties of the features
|3|Performed EDA on data - checked the distribution of data using NPP, KDE plots ; checked for outliers via boxplots
|4| Standardizing the data and Oversampling the minority class , using SMOTE
|5|  Metric used to evaluate models - We use Accuracy and Precision
|6| Trained and tested various models on the data and chose the model which gave highest accuracy score 
|7| Stacking model with xgboost classifier and random forest gave highest precision ( 78.906 % ) for the test set
|8|Hyperparameter tuning of stacking model
|9| Exported the stacking model via pickle


### (B) **Building the Application**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built REST API using Flask framework ; created routes for home page and pred
|2| Built html pages for data input and results prediction
|3| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|4| Deployed the model on Heroku via Git Bash terminal

<hr>

## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\homethyroid.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

### **The Prediction Page**

<img src="static\images\resultthyroid.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

<hr>
  
## Contact

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>