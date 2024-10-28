**Data Science Salaries Prediction Project**
This repository presents a Machine Learning pipeline for predicting salaries in data science roles based on various features. The project is structured into essential components that span the entire workflow from data preprocessing to deployment.

**Data Cleaning:** The pipeline begins by loading and preprocessing the dataset. This includes handling missing values, encoding categorical variables like job titles and education, and normalizing numerical features to prepare the data for analysis.

**Model Building:** After cleaning the data, the project constructs a regression model for salary prediction. The dataset is split into training and testing sets, allowing for effective performance evaluation. The model's accuracy is assessed using metrics such as Mean Absolute Error (MAE) and R-squared.

Model Saving and Loading: The trained model is saved using joblib, enabling easy loading for future predictions without retraining.

**FastAPI Endpoint:** A FastAPI application exposes an API endpoint for users to receive salary predictions based on input features.

**Deployment with UI:** A user-friendly interface built with Gradio or Streamlit allows real-time interaction. The application is deployed on Hugging Face Spaces, making it accessible to a wider audience.

This project demonstrates a complete data science application workflow, emphasizing effective machine learning solutions for real-world scenarios.
