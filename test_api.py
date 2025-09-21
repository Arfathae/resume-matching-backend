#!/usr/bin/env python3
"""
Simple test script for the Resume Matching API
"""
import requests
import json

# API base URL
BASE_URL = "http://127.0.0.1:8000"

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_match(query_text):
    """Test the match endpoint"""
    print(f"Testing match endpoint with query: '{query_text}'")
    payload = {"text": query_text}
    response = requests.post(f"{BASE_URL}/match", json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

if __name__ == "__main__":
    print("🚀 Testing Resume Matching API")
    print("=" * 50)
    
    # Test health endpoint
    test_health()
    
    # Test match endpoint with different queries
    test_queries = [
        "B.Tech student skilled in React",
        "Python developer with machine learning experience",
        "UI/UX designer with Figma skills",
        "Full stack developer with Node.js"
    ]
    
    for query in test_queries:
        test_match(query)
    
    print("✅ All tests completed!")
