from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import logging
import os
from datetime import datetime

app = Flask(__name__)
multiplier = 2.4  # Inflation multiplier for prediction adjustment 
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the trained model
try:
    model = pickle.load(open("models/house_price_model.pkl", "rb"))
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

# Get available locations from the dataset
def get_available_locations():
    try:
        if os.path.exists("data/Pune_House_Data.csv"):
            df = pd.read_csv("data/Pune_House_Data.csv")
            locations = sorted(df['site_location'].dropna().unique().tolist())
            area_types = sorted(df['area_type'].dropna().unique().tolist())
            return locations, area_types
        return [], []
    except Exception as e:
        logger.error(f"Error loading locations: {e}")
        return [], []

@app.route("/", methods=["GET", "POST"])
def index():
    locations, area_types = get_available_locations()
    prediction = None
    prediction_details = {}
    
    if request.method == "POST":
        try:
            # Get form data
            total_sqft = float(request.form["total_sqft"])
            bath = int(request.form["bath"])
            balcony = int(request.form["balcony"])
            bhk = int(request.form["bhk"])
            area_type = request.form["area_type"]
            site_location = request.form["site_location"]
            
            # Validate inputs
            if total_sqft <= 0:
                return render_template("index.html", error="Total Square Feet must be positive", 
                                      locations=locations, area_types=area_types)
            
            # Create DataFrame with user inputs
            input_data = {
                "total_sqft": [total_sqft],
                "bath": [bath],
                "balcony": [balcony],
                "BHK": [bhk],
                "area_type": [area_type],
                "site_location": [site_location]
            }
            
            prediction_details = {
                "total_sqft": total_sqft,
                "bath": bath,
                "balcony": balcony,
                "bhk": bhk,
                "area_type": area_type,
                "site_location": site_location,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Make prediction
            input_df = pd.DataFrame(input_data)
            raw_prediction = model.predict(input_df)[0]
            # Apply inflation multiplier (1.5) to adjust the prediction
            prediction = round(raw_prediction * multiplier, 2)
            
            # Log successful prediction
            logger.info(f"Prediction made: {prediction} lakhs (adjusted for inflation) for {total_sqft} sqft, {bhk} BHK in {site_location}")

        except ValueError as e:
            error_msg = "Invalid input values. Please check your inputs."
            logger.error(f"Value Error: {e}")
            return render_template("index.html", error=error_msg, locations=locations, area_types=area_types)
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            logger.error(f"Prediction error: {e}")
            return render_template("index.html", error=error_msg, locations=locations, area_types=area_types)

    return render_template("index.html", prediction=prediction, prediction_details=prediction_details, 
                          locations=locations, area_types=area_types)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """API endpoint for predictions"""
    if request.is_json:
        try:
            data = request.get_json()
            
            # Create DataFrame with user inputs
            input_data = {
                "total_sqft": [float(data.get("total_sqft", 0))],
                "bath": [int(data.get("bath", 0))],
                "balcony": [int(data.get("balcony", 0))],
                "BHK": [int(data.get("bhk", 0))],
                "area_type": [data.get("area_type", "")],
                "site_location": [data.get("site_location", "")]
            }
            
            # Adjust for inflation
            input_df = pd.DataFrame(input_data)
            raw_prediction = model.predict(input_df)[0]
            adjusted_prediction = round(raw_prediction * multiplier, 2)
            
            return jsonify({"success": True, "prediction": adjusted_prediction, "unit": "lakhs"})
        
        except Exception as e:
            logger.error(f"API error: {e}")
            return jsonify({"success": False, "error": str(e)}), 400
    
    return jsonify({"success": False, "error": "Request must be JSON"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
