from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

app = Flask(__name__)

# Load the LSTM model
def load_model():
    try:
        model = keras.models.load_model('my_lstm_model.h5')
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Initialize model
model = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_text = request.form.get('energy_data', '')
        
        # Validate input
        if not input_text.strip():
            return jsonify({'error': 'Please enter energy consumption data'})
        
        # Parse input data (comma-separated values)
        try:
            input_values = [float(x.strip()) for x in input_text.split(',')]
        except ValueError:
            return jsonify({'error': 'Please enter valid numbers separated by commas'})
        
        # Validate that we have exactly 100 values
        if len(input_values) != 100:
            return jsonify({'error': f'Please enter exactly 100 values. You entered {len(input_values)} values.'})
        
        # Check if model is loaded
        if model is None:
            return jsonify({'error': 'Model not loaded properly'})
        
        # Convert to numpy array and reshape for LSTM
        input_array = np.array(input_values).reshape(1, 100, 1)
        
        # Make prediction
        prediction = model.predict(input_array, verbose=0)
        predicted_value = float(prediction[0][0])
        
        # Return result
        return jsonify({
            'success': True,
            'prediction': predicted_value,
            'input_values': input_values,
            'message': f'Predicted next energy consumption: {predicted_value:.4f}'
        })
        
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'})

@app.route('/reset', methods=['POST'])
def reset():
    return jsonify({'success': True, 'message': 'Form reset successfully'})

if __name__ == '__main__':
    # For Railway deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
