@echo off
echo Starting Energy Consumption Prediction Web App...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask application...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
