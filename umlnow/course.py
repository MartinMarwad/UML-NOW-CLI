"""
Courses
"""

# Python Packages
from bs4 import BeautifulSoup
import requests
import json

# Local
from .data import PREFIXES


def get_html_response(url: str):
    """Get the html response from a url."""
    response = requests.get(url)
    return response

def get_course_url(course: str):
    """Get the url for a course."""
    prefix, number = course.split(".")
    return f"https://www.uml.edu/catalog/courses/{prefix}/{number}/"

def get_course_requirements(response: requests.models.Response):
    """Returns the course requirements as a string from a html response."""
    soup = BeautifulSoup(response.content, "html.parser")
    html = soup.select("p:nth-child(7)")[0]
    return html.text

def parse_requirements_as_dict(text: str):
    
    # SYMBOLS
    PREREQ = "Pre-Reqs:"
    COREQ1 = "and Co-Req:"
    COREQ2 = "and Co-req:"
    COREQ3 = "Co-req:"
    COREQ4 = "Co-Req:"
    
    # Outputs
    prereqs = "None"
    prereqs_all_required = None
    coreqs = "None"
    coreqs_all_required = None
    
    # INTIAL CHECKS
    
    # If "Co-req:" in text, split into prereqs and coreqs. We are assuming this gives a list with two strings.
    if COREQ1 in text:   prereqs, coreqs = text.split(COREQ1)
    elif COREQ2 in text: prereqs, coreqs = text.split(COREQ2)
    elif COREQ3 in text: prereqs, coreqs = text.split(COREQ3)
    elif COREQ4 in text: prereqs, coreqs = text.split(COREQ4)
        
    # Otherwise assume prereqs are all text
    else:
        prereqs = text
        
    ## PREREQS
    
    # Break string into list. This should put the course prefix right before the course numeber in the list.
    prereqs = prereqs.replace('.', ' ').split(" ")
    
    # If 'or' in prereqs, then all except one are optional
    if 'or' in prereqs: prereqs_all_required = False
    
    # If 'and' in prereqs, then these are all required
    if 'and' in prereqs: prereqs_all_required = True
    
    # If both 'or' and 'and' in prereqs, then something really bad just happened.
    if 'or' in prereqs and 'and' in prereqs: prereqs_all_required = "Something bad happened, both 'and' & 'or' detected!"
    
    # if not 'or' or 'and' in prereqs, then all are required
    if not 'or' in prereqs and not 'and' in prereqs: prereqs_all_required = True
    
    # Get final list of prereqs
    FINAL_PREREQS = []
    for index, item in enumerate(prereqs):
        if item in PREFIXES:
            FINAL_PREREQS.append(f"{item}.{prereqs[index + 1]}")
    
    # COREQS
        
    # Break string into list
    coreqs = coreqs.replace('.', ' ').split(" ")
    
    # If 'or' in coreqs, then all except one are optional
    if 'or' in coreqs: coreqs_all_required = False
    
    # If 'and' in coreqs, then these are all required
    if 'and' in coreqs: coreqs_all_required = True
    
    # If both 'or' and 'and' in coreqs, then something really bad just happened.
    if 'or' in coreqs and 'and' in coreqs: coreqs_all_required = "Something bad happened, both 'and' & 'or' detected!"
    
    # If not 'or' or 'and' in coreqs, then all are required
    if 'or' not in coreqs and 'and' not in coreqs: coreqs_all_required = True
    
    
    # Get final list of coreqs
    FINAL_COREQS = []
    for index, item in enumerate(coreqs):
        if item in PREFIXES:
            FINAL_COREQS.append(f"{item}.{coreqs[index + 1]}")
            
            
    ## Return final result  
    return {
        # 'pre-reqs-string': prereqs, # for debugging
        'pre-reqs': FINAL_PREREQS,
        'pre-reqs-all-required': prereqs_all_required,
        
        # 'co-reqs-string': coreqs, # for debugging
        'co-reqs': FINAL_COREQS,
        'co-reqs-all-required': coreqs_all_required,
    }
    
def get_course_name(response: requests.models.Response):
    """Returns the course name as a string from a html response."""
    soup = BeautifulSoup(response.content, "html.parser")
    html = soup.select("h1")[0]
    return html.text

def get_course_description(response: requests.models.Response):
    """Returns the course description as a string from a html response."""
    soup = BeautifulSoup(response.content, "html.parser")
    html = soup.select("p:nth-child(5)")[0]
    return html.text

def get_course_id(response: requests.models.Response):
    """Returns the course id as a string from a html response."""
    soup = BeautifulSoup(response.content, "html.parser")
    course_id = soup.select(".outline:nth-child(1)")[0].text
    
    # Sanitize
    if "id:" in course_id.lower(): course_id = course_id.split("Id: ")[1]
    
    # return 
    return course_id

def get_course_credits(response: requests.models.Response):
    """Returns the course credits as a dict from a html response."""
    soup = BeautifulSoup(response.content, "html.parser")
    min_credits = soup.select(".outline:nth-child(2)")[0].text
    max_credits = soup.select(".outline:nth-child(3)")[0].text
    
    # Sanitize
    if 'credits' in min_credits.lower(): min_credits = min_credits.split("Credits Min: ")[1]
    if 'credits' in max_credits.lower(): max_credits = max_credits.split("Credits Max: ")[1]
    
    # Return
    return {
        'min': min_credits,
        'max': max_credits,
    }

# Course Command
def Course(course, **kwargs):
    """ """
    
    course_url = get_course_url(course)
    response = get_html_response(course_url)
    requirements_text = get_course_requirements(response)
    parsed_requirements = parse_requirements_as_dict(requirements_text)
    course_name = get_course_name(response)
    course_description = get_course_description(response)
    course_id = get_course_id(response)
    course_credits = get_course_credits(response)
    
    
    if kwargs.get('name'): return {'name': course_name,}
    if kwargs.get('url'): return {'url': course_url,}
    if kwargs.get('id'): return {'id': course_id,}
    if kwargs.get('description'): return {'description': course_description,}
    if kwargs.get('credits'): return {'credits': course_credits,}
    if kwargs.get('requirements-text'): return {'requirements-text': requirements_text,}
    if kwargs.get('requirements'): return {'requirements': parsed_requirements,}
            
    return {
        'name': course_name,
        'url': course_url,
        'id': course_id,
        'description': course_description,
        'credits': course_credits,
        'requirements-text': requirements_text,
        'requirements': parsed_requirements,
    }