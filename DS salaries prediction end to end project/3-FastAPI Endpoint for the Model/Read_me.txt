## README: Salary Prediction API

This repository contains a FastAPI application for predicting salaries based on certain factors.

### Prerequisites

* Python 3.x
* Docker (optional)

### Installation

1.  Clone the repository
2.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1.  Export your ngrok auth token:

    ```bash
    export NGROK_AUTH_TOKEN="your_ngrok_auth_token"
    ```

2.  Run the application:

    ```bash
    python main.py
    ```
    This will start a local server and print a ngrok public URL, which you can use to access the API

### Usage

To use the API, send a POST request to the endpoint `/diabetes_prediction` with the following JSON payload:

