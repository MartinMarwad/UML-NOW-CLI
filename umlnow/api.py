"""
API
"""

# Python Standard
import requests
import json

# Python Extended
import fire


# Request API
def search(**params):
    """Search """
    
    # Base URL
    URL = "https://www.uml.edu/student-dashboard/api/ClassSchedule/RealTime/Search/?"
    
    # Create Request URL
    for key, value in params.items():
        URL += f"{key}={value}&"
        
    # Request
    response = requests.get(URL).json()
    
    return json.dumps(response, indent=4)
    
    return response



