# Car-Price-Project

MACHINE LEARNING PROJECT (Car Price Prediction, Regression Analysis)
•	Metrics tracked with DVC (Data Version Control)
•	Data Analysis
•	Automated Pipelines
•	Machine Learning

Summary
Data was loaded and analyzed i.e., checked for null values, after which, major data analysis such as lookout for outliers, plots and extraction of tables was carried out, plots saved to folder as well, we then proceed to folder selection, encoding and training. The above-mentioned steps were followed and model(xgboost) was created and saved. For inference, we load the model and evaluate on a part of the dataset. Metrics are compared after several retraining of models based on changed hyperparameters.
-	Experiment Tracking with DVC
The whole machine learning process was automated with DVC. An automated pipeline is created, experiments are run easily and metrics are tracked are monitored with DVC’s UI (DVC Studio). This makes the task easier and more efficient as just one command-line command is used for tasks i.e., ‘dvc repro’ reproduces/reruns the whole experiment and saves files to disk.

