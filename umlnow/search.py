"""
Search CLI

This module contains the CLI for the search command. This command is used to create a user friendly
abstraction for the both the UML Now API and the UML Catalog API.
"""
        

class Search(object):
    """Search API. 
    This object provides the CLI for the search command. This command is used to create a user friendly
    abstraction for the both the UML Now API and the UML Catalog API."""
    
    def __init__(self, **params):
        self.params = params
        
    def classes(self):
        """Search courses."""
        return "Sorry, not implemented yet."
    
    def professors(self):
        """Search professors."""
        return "Sorry, not implemented yet."
    
    def majors(self):
        """Search majors."""
        return "Sorry, not implemented yet."
    
    def minors(self):
        """Search minors."""
        return "Sorry, not implemented yet."
    
    def degree_pathways(self):
        """Search degree pathways."""
        return "Sorry, not implemented yet."
    
        
