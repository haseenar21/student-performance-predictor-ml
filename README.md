# student-performance-predictor-ml
This is a ML web application that predicts a student's exam score based on academic performance, lifestyle, and environmental factors. It uses multiple regression models, hyperparameter tuning, and a Streamlit interface to deliver real-time predictions in an interactive dashboard.

# Live Demo - https://ml-student-performance-predictor.streamlit.app/

# Live Features
- Predict student exam score in real-time
- Trained on multiple - ML models
- Hyperparameter tuning using GridSearchCV
- Model evaluation using R^2, MAE, RMSE
- Interactive Streamlit UI with categorized inputs
- Visual performance profile of student inputs
- Intelligent performance labeling (Excellent/ Good/ Needs improvement)

# Machine Learning Workflow
1. Data Preprocessing
- Handled missing values using SimpleImputer
- Scaled numerical features using StandardScaler
- Encoded categorical features using OneHotEncoder
2. Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression
- Support Vector Regression (SVR)
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- HistGradientBoosting Regressor
3. Model Selection
- Cross-validation using KFold (k=5)
- Metrics:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
4. Hyperparameter Tuning
- GridSearchCV applied to:
   - Ridge Regression
   - SVR
   - HistGradientBoosting
5. Final Model
- Best performing model: Ridge Regression
- Saved using joblib for deployment

# Web App (Streamlit)

# Tech Stack
- Python 
- Pandas & NumPy
- Scikit-learn 
- Streamlit 
- Joblib 
