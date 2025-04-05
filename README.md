# Pune House Price Predictor

A machine learning web application that predicts house prices in Pune based on various features like location, size, and amenities.

## Features

- Predicts property prices in Pune using a trained machine learning model
- User-friendly web interface for input and visualization
- Support for different area types and locations across Pune
- RESTful API for integrating predictions into other applications
- Mobile-responsive design

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Deployment**: Gunicorn

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/pune-house-price-predictor.git
   cd pune-house-price-predictor
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python main.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`

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

## API Usage

The application includes a RESTful API endpoint for programmatic predictions:

```
POST /api/predict
Content-Type: application/json

{
  "total_sqft": 1500,
  "bath": 2,
  "balcony": 1,
  "bhk": 3,
  "area_type": "Super built-up  Area",
  "site_location": "Wakad"
}
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
