# Fire Weather Index (FWI) Prediction App

This is a simple web application that predicts the Fire Weather Index (FWI) based on user-provided values. The application is built using Python and Flask framework.

## Prerequisites

To run this application, you need to have the following installed on your system:

- Python (version 3.6 or higher)
- Flask (version 2.0.1 or higher)

## Installation

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

   ```bash
   cd <project-directory>
   ```

3. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Once the dependencies are installed, run the Flask application by executing the following command:

   ```bash
   python app.py
   ```

2. Open a web browser and visit `http://localhost:5000` to access the application.

3. On the web page, enter the required values in the provided input fields. These values are used to predict the Fire Weather Index (FWI).

4. Click the "Predict" button to submit the values and view the predicted FWI value.

## Project Structure

The project repository contains the following files and folders:

- `app.py`: The main Python file that implements the Flask application.
- `templates/`: A folder containing the HTML templates used by the application for rendering the web page.
- `model/`: A folder containing the trained machine learning model for FWI prediction.
- `dataset/`: A folder containing the dataset used to train the machine learning model.
- `notebooks/`: A folder containing Jupyter notebooks used for data preprocessing, model training, and evaluation.

## Customization

You can customize this application to suit your needs. Here are a few possible modifications you can make:

- **Model**: If you have a different pre-trained model for FWI prediction, replace the contents of the `model/` folder with your own model files. Ensure that the model is compatible with the provided dataset.
- **Dataset**: If you have a different dataset or want to use a subset of the provided dataset, replace the contents of the `dataset/` folder with your own dataset files. Ensure that the dataset format matches the expected input format of the model.
- **UI**: If you want to modify the user interface, you can edit the HTML templates located in the `templates/` folder. You can modify the form fields, styling, or add additional functionality as per your requirements.

Feel free to explore the code and make changes as needed to fit your specific use case.

## Acknowledgments

This application is built using Flask, a micro web framework for Python. The model used for FWI prediction is trained on a specific dataset. The dataset and model development process may vary based on your specific requirements.
