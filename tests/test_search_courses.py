

# Python imports
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))


from umlnow.search import Search, get_courses_by_department_prefix
from umlnow.data import DEPARTMENT_PREFIXES
import time
import json
import fire


# Write python dictionary to file as JSON
def write_json(data, filename):
    with open(filename, 'w') as outfile:
        # Write the dictionary to the file in JSON format
        json.dump(data, outfile)

# Test the search courses function
def test_search_courses(start_prefix=None, parse=True, debug=True):
    
    print("Starting Script:")
    start_time = time.time()
    departments = DEPARTMENT_PREFIXES
    
    if start_prefix:
        # Get the index of the starting prefix
        start_index = DEPARTMENT_PREFIXES.index(start_prefix)
        
        # Cut the list in half
        departments = DEPARTMENT_PREFIXES[DEPARTMENT_PREFIXES.index(start_prefix):]
    
    # For department in DEPARTMENT_PREFIXES, get the department prefex
    for department in departments:
        
        # Get the courses by department prefix
        print("- Starting search for department: " + department)
        output = get_courses_by_department_prefix(department, parse=True, debug=True)
        
        # Save the output to a file
        write_json(output, f'{department}.json')
        
    print("Completed Script in " + str(time.time() - start_time) + " seconds")


# if __name__ == "__main__":
    
#     # Run the test
#     test_search_courses('POLI')

fire.Fire(test_search_courses)