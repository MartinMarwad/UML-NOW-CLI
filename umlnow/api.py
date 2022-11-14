"""
API
"""

# Python Packages
import requests


# API
class API(object):
    """API Class.
    This object provides the CLI for the api command. This command is used to directly
    interface with the UML Now API and the UML Catalog API."""
    
    def __init__(self):
        """Initialize API Class"""
        pass
        
    def search(self, **params):
        """Search the UML Now API and return raw JSON."""
        # If no params:
        if not params:
            return "No params provided"
        
        # Base URL
        URL = "https://www.uml.edu/student-dashboard/api/ClassSchedule/RealTime/Search/?"
        
        # Create Request URL
        for key, value in params.items():
            URL += f"{key}={value}&"
            
        # Request
        response = requests.get(URL).json()
        return response
    
    def catalog(self, **params):
        """Search the UML Course Catalog API and return raw JSON."""
        # Base URL
        URL = "https://www.uml.edu/catalog/advance-search.aspx?"
        
        # Create Request URL
        for key, value in params.items():
            URL += f"{key}={value}&"
            
        # Request
        response = requests.post(URL).json()
        return response    

