## End to End Machine Learning Project
1. We have created a conda environment on python 3.8 version 

2. Mapping in the github repository

3. Creating .gitignore file in github and pulling it in vscode
#### WE have created .gitignore file so as some of the file that need not to be committed in the gitgub, will get removed

4. Creating setup.py 
#### setup.py is responsible for creating ML application as a package, It helps make a Python project installable and reusable. We can even deploye this package in python pypi and from there anybody can install this package and use it

5. Creating src folder and in that creating __init__.py file so that this src folder can be treated as package, that can be exported or imported to some other file location 
#### The src folder is commonly created in Python projects to keep the actual application code organized and separated from other files.

6. In src folder we will create another folder named components and in this folder we will create file such as __init__.py, data_ingestion.py, data_transformatoin.py and model_trainer.py. 
So this components that you have seen till now data ingestion data transformation model trainer.The mainly this is specifically for the training purpose
