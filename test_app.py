#!/usr/bin/env python3
"""
Test script for the Energy Consumption Prediction Web App
This script tests the Flask application locally before deployment.
"""

import requests
import json
import numpy as np

def test_prediction_api():
    """Test the prediction API endpoint"""
    base_url = "http://localhost:5000"
    
    # Generate test data (100 random values)
    test_data = np.random.uniform(1.0, 2.0, 100).tolist()
    test_input = ", ".join([f"{x:.2f}" for x in test_data])
    
    print("🧪 Testing Energy Consumption Prediction API")
    print("=" * 50)
    
    try:
        # Test prediction endpoint
        response = requests.post(
            f"{base_url}/predict",
            data={"energy_data": test_input},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ Prediction successful!")
                print(f"📊 Input values: {len(result['input_values'])} values")
                print(f"🔮 Predicted value: {result['prediction']:.4f}")
                print(f"💬 Message: {result['message']}")
            else:
                print(f"❌ Prediction failed: {result.get('error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure the Flask app is running on localhost:5000")
        print("💡 Run: python app.py")
    except Exception as e:
        print(f"❌ Test failed: {e}")

def test_validation():
    """Test input validation"""
    base_url = "http://localhost:5000"
    
    print("\n🔍 Testing Input Validation")
    print("=" * 30)
    
    test_cases = [
        ("Too few values", "1.2, 1.5, 1.3"),
        ("Too many values", ", ".join([str(i) for i in range(101)])),
        ("Invalid format", "1.2, abc, 1.3, 1.4"),
        ("Empty input", ""),
    ]
    
    for test_name, test_input in test_cases:
        try:
            response = requests.post(
                f"{base_url}/predict",
                data={"energy_data": test_input},
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if not result.get('success'):
                    print(f"✅ {test_name}: Correctly rejected - {result.get('error')}")
                else:
                    print(f"❌ {test_name}: Should have been rejected")
            else:
                print(f"❌ {test_name}: HTTP Error {response.status_code}")
                
        except Exception as e:
            print(f"❌ {test_name}: Test failed - {e}")

if __name__ == "__main__":
    print("🚀 Energy Consumption Prediction App - Test Suite")
    print("=" * 60)
    
    # Test main functionality
    test_prediction_api()
    
    # Test validation
    test_validation()
    
    print("\n" + "=" * 60)
    print("🏁 Test suite completed!")
    print("💡 If all tests passed, your app is ready for Railway deployment!")
