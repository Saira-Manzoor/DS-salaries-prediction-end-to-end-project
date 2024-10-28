import gradio as gr
import joblib

# ## Deployment at Hugging Face with a Simple UI using Gradio

# Load the trained model
model = joblib.load('model_salaries.joblib')

def predict_salary(work_year, experience_level, employment_type, company_size, work_models):
    """Predicts the salary based on the input features."""
    # Assuming you have a dictionary mapping string values to numerical values
    # for each feature (like in your EDA)
    experience_level_mapping = {'Entry-level': 1, 'Mid-level': 2, 'Senior-level': 3, 'Executive-level': 4}
    employment_type_mapping = {'Part-time': 1, 'Freelance': 2, 'Full-time': 3, 'Contract': 4}
    company_size_mapping = {'Large': 1, 'Medium': 2, 'Small': 3}
    work_models_mapping = {'Remote': 1, 'On-site': 2, 'Hybrid': 3}

    input_data = [
        work_year,
        experience_level_mapping[experience_level],
        employment_type_mapping[employment_type],
        company_size_mapping[company_size],
        work_models_mapping[work_models],
    ]

    prediction = model.predict([input_data])[0]
    return f"Predicted Salary: ${prediction:.2f}"

iface = gr.Interface(
    fn=predict_salary,
    inputs=[
        gr.Dropdown(choices=[2020, 2021, 2022, 2023], label="Work Year"),  # Dropdown for work year
        gr.Dropdown(choices=['Entry-level', 'Mid-level', 'Senior-level', 'Executive-level'], label="Experience Level"),
        gr.Dropdown(choices=['Part-time', 'Freelance', 'Full-time', 'Contract'], label="Employment Type"),
        gr.Dropdown(choices=['Large', 'Medium', 'Small'], label="Company Size"),
        gr.Dropdown(choices=['Remote', 'On-site', 'Hybrid'], label="Work Models"),
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Data Science Salary Prediction",
    description="Predict the salary based on work year, experience level, employment type, company size, and work models."
)
iface.launch(share=True)