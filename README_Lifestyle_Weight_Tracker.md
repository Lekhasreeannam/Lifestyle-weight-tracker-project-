# ⚖️ Lifestyle Weight Tracker – Weight Prediction

A machine learning regression project that predicts a person's **current weight (kg)** using selected daily lifestyle and nutrition-related features. The project includes data cleaning, exploratory analysis, feature selection, model training, evaluation, model saving, and deployment with **Streamlit**.

## 📌 Project Overview

The goal of this project is to predict weight using daily routine and lifestyle information.

The dataset contains:

- **55,000 rows**
- **18 columns**

The final Streamlit application predicts weight from five inputs:

- Stress Level
- Calories Consumed
- Protein (g)
- Carbs (g)
- Fat (g)

## 📊 Dataset

**Dataset:** `lifestyle weight tracker.csv`

The original dataset contains features such as:

- Age
- Gender
- Height
- Initial Weight
- Stress Level
- Sleep Hours
- Caffeine Intake
- Calories Consumed
- Protein
- Carbohydrates
- Fat
- Steps
- Workout Type
- Workout Intensity
- Temperature
- Weight Change
- Current Weight

The prediction target is a numeric weight value, so this project is treated as a **regression problem**.

## 🧹 Data Cleaning

The project identifies missing values in:

- `Calories_Consumed`
- `Workout_Type`

The documented preprocessing includes:

- Replacing missing `Calories_Consumed` values with the median
- Replacing missing `Workout_Type` values with the mode
- Detecting outliers in `Calories_Consumed`, `Protein_g`, `Carbs_g`, and `Fat_g`
- Treating outliers using the IQR method
- Using box plots to inspect the data after outlier treatment

## 🔍 Feature Selection

Correlation analysis is used to identify features that are strongly related to the target.

The final deployed model uses:

```text
Stress_Level
Calories_Consumed
Protein_g
Carbs_g
Fat_g
```

## ⚙️ Data Transformation

The selected numerical features are standardized using:

```python
StandardScaler()
```

The fitted scaler is saved and reused by the Streamlit application so new user inputs receive the same transformation used during model development.

## 🧠 Machine Learning Model

The project uses:

**Linear Regression**

Linear Regression was selected because the target variable is numeric.

The data is divided into:

- **80% training data**
- **20% testing data**

## 📈 Model Performance

### Holdout Evaluation

| Metric | Training | Testing |
|---|---:|---:|
| MAE | 0.0320 | 0.0317 |
| MSE | 0.00161 | 0.00158 |
| RMSE | 0.0401 | 0.0398 |
| R² Score | 0.8542 | 0.8592 |

### Cross-Validation

The documented mean cross-validation score is approximately:

```text
0.8552
```

The similar training, testing, and cross-validation scores indicate stable performance in the documented experiment.

## 🔄 Project Workflow

```text
Lifestyle Weight Dataset
        ↓
Understand the Dataset
        ↓
Handle Missing Values
        ↓
Detect & Treat Outliers
        ↓
Exploratory Data Analysis
        ↓
Correlation-Based Feature Selection
        ↓
StandardScaler
        ↓
80/20 Train-Test Split
        ↓
Linear Regression
        ↓
Model Evaluation
        ↓
Cross-Validation
        ↓
Save Model, Scaler & Features
        ↓
Streamlit Web Application
        ↓
Predicted Weight (kg)
```

## 💻 Streamlit Application

The project includes an interactive **Streamlit** application.

The application loads:

```text
model.pkl
scaler.pkl
features.pkl
```

The user enters lifestyle and nutrition information, the application scales the input using the saved scaler, and the trained model returns the predicted weight in kilograms.

Example output:

```text
Predicted Weight: 68.45 kg
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

## 📁 Project Structure

```text
Lifestyle-Weight-Tracker/
│
├── app.py
├── lifestyle_weight_tracker_code.ipynb
├── lifestyle_weight_tracker.csv
├── model.pkl
├── scaler.pkl
├── features.pkl
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Lifestyle-Weight-Tracker
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

### 3. Check the required deployment files

Make sure these files are in the same folder:

```text
app.py
model.pkl
scaler.pkl
features.pkl
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔮 Prediction Pipeline

```text
Stress Level
Calories
Protein
Carbs
Fat
     ↓
Pandas DataFrame
     ↓
Saved StandardScaler
     ↓
Linear Regression Model
     ↓
Predicted Weight (kg)
```

## ✨ Key Features

- Lifestyle-based weight prediction
- Data cleaning and missing-value treatment
- IQR-based outlier treatment
- Exploratory data analysis
- Correlation-based feature selection
- Feature standardization
- Linear Regression model
- Holdout and cross-validation evaluation
- Saved model pipeline
- Interactive Streamlit deployment

## ⚠️ Disclaimer

This project is intended for **educational and machine learning demonstration purposes only**. The predicted weight should not be interpreted as medical or nutritional advice. For health-related guidance, consult an appropriate qualified professional.

## 👩‍💻 Author

**Lekha Sree Annam**

B.Tech — Computer Science and Engineering  
Artificial Intelligence & Machine Learning

**Skills:** Python | Machine Learning | Data Science | Pandas | Scikit-learn | Linear Regression | Streamlit

---

⭐ If you find this project useful, consider giving the repository a star.
