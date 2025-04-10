# House Price Prediction - Pune

A machine learning web application that predicts house prices in Pune based on property features.

## Features

- Accurate price prediction based on property size, bedrooms, bathrooms, and location
- Modern responsive user interface
- API endpoint for programmatic access

## Deployment Guide

### Option 1: Deploy to Render (Recommended)

1. Sign up for a free [Render account](https://render.com)
2. Connect your GitHub/GitLab account or manually deploy the code
3. Create a new Web Service
4. Select "Build and deploy from a Git repository"
5. Configure your deployment:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`
6. Click "Create Web Service"

### Option 2: Deploy to PythonAnywhere

1. Sign up for a free [PythonAnywhere account](https://www.pythonanywhere.com/)
2. Upload your code using their file uploader or via GitHub
3. Create a new web app, selecting Flask and Python 3.10
4. Set up your virtual environment and install requirements
5. Configure WSGI file to point to your Flask app

### Option 3: Deploy to Heroku

1. Sign up for a [Heroku account](https://heroku.com)
2. Install the Heroku CLI: `brew install heroku/brew/heroku`
3. Login to Heroku: `heroku login`
4. Create a new app: `heroku create your-app-name`
5. Deploy your code: `git push heroku main`

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

Visit `http://localhost:5000` in your browser.

## API Usage

Send a POST request to `/api/predict` with JSON data:

```json
{
  "total_sqft": 1200,
  "bath": 2,
  "balcony": 1,
  "bhk": 2,
  "area_type": "Built-up Area",
  "site_location": "Wakad"
}
```

## Technologies Used

- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML/CSS/JavaScript

## Project Structure

```
├── data/
│   └── Pune_House_Data.csv    # Dataset with Pune property information
├── models/
│   └── house_price_model.pkl  # Trained machine learning model
├── notebooks/
│   └── model_training.ipynb   # Jupyter notebook for model development
├── static/
│   └── css/
│       └── style.css          # CSS styling for the web application
├── templates/
│   └── index.html             # Frontend HTML template
├── main.py                    # Flask application entry point
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Future Improvements

- Add more visualization options for prediction results
- Implement user accounts to save prediction history
- Add comparative market analysis feature
- Expand to other cities in India

## License

MIT

## Author

Created by Tanish - April 2025
