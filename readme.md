# Project Title

## Overview
This project is designed to Machine Learning Response API Detection. It uses Python 3.13 and several essential packages such as `requests`, `ipython`, `pandas`, and `scikit-learn`.

## Prerequisites
- Python 3.13.0
- `pip` (Python package installer)

## Depedencies
- `scikit-learn`
- `joblib`

These dependencies are managed by `pipenv` and are specified in the `Pipfile`.

## Installation

### Step 1: Install `pipenv`
`pipenv` is a tool that aims to bring the best of all packaging worlds (bundled, development, and deployment) to the Python world. It automatically creates and manages a virtual environment for your projects and adds/removes packages from your `Pipfile` as you install/uninstall packages.

To install `pipenv`, run the following command:
```
pip install pipenv
```

### Step 2: Set Up the Project Environment
Navigate to the project directory and install the dependencies specified in the `Pipfile`:
```
cd path/to/your/project
pipenv install
```
This will create a virtual environment and install all the packages listed in the `Pipfile`.

### Step 3: Activate the Virtual Environment
To activate the virtual environment created by `pipenv`, run:
```
pipenv shell
```

### Step 4: Run the Python Script For Generate file .pkl model
To start the learning model using SVM, run:
```
pipenv run start-learning-model-svm
```

To start the learning model using Naive Bayes, run:
```
pipenv run start-learning-model-naive-bayes
```

## Loading the Trained Model
The main script (`main.py`) loads the trained model and vectorizer. By default, it loads the Naive Bayes model. If you want to use a different model, change the file name accordingly.

```python
# Load the trained model
# change the file name to model_*.pkl if you want to use the Naive Bayes model
try:
    model = joblib.load('model_*.pkl')
except FileNotFoundError:
    print("Error: The model file was not found. Please train the model first.")
    exit(1)

# Load the vectorizer
try:
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    print("Error: The vectorizer file was not found. Please train the model first.")
    exit(1)
```

### Step 5 : Run the Python Script For Test Prediction
Once the virtual environment is activated, you can run the main Python script using the following command:
```
pipenv run start
```