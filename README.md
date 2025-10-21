# Energy Consumption Prediction Web App

A Flask web application that predicts future energy consumption using a trained LSTM neural network model.

## Features

- **Input Validation**: Ensures exactly 100 energy consumption values are entered
- **LSTM Prediction**: Uses pre-trained model to predict next energy consumption value
- **Modern UI**: Clean, responsive design with gradient backgrounds
- **Data Visualization**: Interactive chart showing input data and prediction
- **Reset Functionality**: Easy form reset button
- **Railway Ready**: Configured for deployment on Railway platform

## Requirements

- Python 3.8+
- Flask 2.3.3
- TensorFlow 2.13.0
- NumPy 1.24.3
- Keras 2.13.1
- Gunicorn 21.2.0

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the web app**:
   Open your browser and go to `http://localhost:5000`

## Usage

1. Enter exactly 100 energy consumption values separated by commas
2. Click "Predict" to get the next energy consumption prediction
3. View the prediction result and data visualization
4. Use "Reset" to clear the form

### Example Input Format:
```
1.2, 1.5, 1.3, 1.4, 1.6, 1.7, 1.5, 1.8, 1.9, 1.7, 1.6, 1.4, 1.3, 1.5, 1.7, 1.8, 1.9, 1.6, 1.4, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.5, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.5, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.5, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.5, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3, 1.4, 1.6, 1.8, 1.9, 1.7, 1.5, 1.3, 1.2, 1.4, 1.6, 1.8, 1.7, 1.5, 1.3
```

## Railway Deployment

This application is configured for deployment on Railway:

1. **Connect your GitHub repository** to Railway
2. **Upload your model file** (`my_lstm_model.h5`) to the repository
3. **Deploy automatically** - Railway will detect the Python app and install dependencies
4. **Access your deployed app** via the provided Railway URL

### Railway Configuration Files:
- `Procfile`: Specifies the web process command
- `railway.json`: Railway-specific deployment configuration
- `requirements.txt`: Python dependencies

## File Structure

```
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── my_lstm_model.h5      # Pre-trained LSTM model
├── requirements.txt      # Python dependencies
├── Procfile             # Railway process file
├── railway.json         # Railway configuration
└── README.md           # This file
```

## API Endpoints

- `GET /`: Main web interface
- `POST /predict`: Submit energy data for prediction
- `POST /reset`: Reset form (AJAX endpoint)

## Model Requirements

The application expects a Keras/TensorFlow LSTM model saved as `my_lstm_model.h5` with:
- Input shape: `(batch_size, 100, 1)`
- Output shape: `(batch_size, 1)`

## Error Handling

The application includes comprehensive error handling for:
- Invalid input format
- Incorrect number of values (not exactly 100)
- Model loading failures
- Prediction errors
- Network connectivity issues

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

This project is open source and available under the MIT License.
