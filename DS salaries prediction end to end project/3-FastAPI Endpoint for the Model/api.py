# -*- coding: utf-8 -*-
"""api.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MP1JmKX31t5cNT3-2TmF4GJh1u0KGAhs
"""

!pip install fastapi uvicorn

# Fast Api Using Unicorn and njrok
import joblib
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
import pandas as pd
import numpy as np
import traceback
import json
!pip install fastapi uvicorn pyngrok

# Fast Api Using Unicorn

diabetes_model = joblib.load('model_salaries.joblib')
#     return prediction

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelInput(BaseModel):
    work_year: int
    experience_level: object
    employment_type: object
    company_size: object
    work_models: object

@app.post("/diabetes_prediction")
async def diabetes_prediction(input_parameters: ModelInput):
    try:
        logger.info("Received input parameters:")
        logger.info(input_parameters)

        # Process input parameters
        input_data = {
            "work_year": input_parameters.work_year,
            "experience_level": input_parameters.experience_level,
            "employment_type": input_parameters.employment_type,
            "company_size": input_parameters.company_size,
            "work_models": input_parameters.work_models
        }

        logger.info("Input data:")
        logger.info(input_data)

        # Create DataFrame
        df = pd.DataFrame([input_data])

        logger.info("DataFrame:")
        logger.info(df.head())

        # Make prediction
        prediction = diabetes_model.predict(df)

        logger.info("Prediction:")
        logger.info(prediction)

        print("Prediction:", prediction)

        # Ensure prediction is a JSON serializable object
        prediction_dict = {"prediction": float(prediction)}

        # Return prediction as JSON
        return JSONResponse(content=json.dumps(prediction_dict), media_type="application/json")

    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error(traceback.format_exc())
        return JSONResponse(content={"error": "Internal server error"}, status_code=500, media_type="application/json")

!pip install pyngrok
from pyngrok import ngrok

# Terminate open tunnels if exist
ngrok.kill()

# Setting the authtoken (optional)
# Get your authtoken from https://dashboard.ngrok.com/auth
NGROK_AUTH_TOKEN = "2o4maFh71LTWbJbkK7Z8aWu4Tqi_3MKKVMsYr73EGysyN5hjc"  # Replace with your authtoken
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Open a HTTP tunnel on port 8000 for http://localhost:8000
public_url = ngrok.connect(8000)
print(" * ngrok tunnel \"{}\" -> \"http://localhost:8000\"".format(public_url))