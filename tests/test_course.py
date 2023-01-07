""" 
This modules tests the course command of the CLI to see if it extract course requirements correctly.
"""

from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
# print(sys.path)

from umlnow.course import Course, get_course_requirements_dict


TEST_CASES = [
    
    # Case 1
    {
        "class": "COMP.1010",
        "input": "Co-req: COMP.1030L Comp. 1 Lab.",
        "output": {
            "prerequisites": [],
            "corequisites": [
                ['COMP.1030L'],
            ],
        }   
    },
    
    # Case 2    
    {
        "class": "COMP.1020",
        "input": "COMP.1010 Computing I with a B- or better, and COMP.1030L Computing I Lab, and Co-req: COMP.1040L Computing II Lab.",
        "output": {
            "prerequisites": [
                ['COMP.1010'],
                ['COMP.1030L'],
            ],
            "corequisites": [
                ['COMP.1040L'],
            ],
        }
    },
    
    # Case 3
    {
        "class": "COMP.1040L",
        "input": "Co-req: Computing II COMP.1020.",
        "output": {
            "prerequisites": [],
            "corequisites": [['COMP.1020'],],
        }
    },
    
    # Case 4
    {
        "class": "COMP.2010",
        "input": "COMP.1020 Computing ll, and Co-req: COMP.2010L Computing lll Lab.",
        "output": {
            "prerequisites": [['COMP.1020'],],
            "corequisites": [['COMP.2010L'],],
        }
    },
    
    # Case 5
    {
        "class": "COMP.2010R",
        "input": "COMP.1020 Computing ll, and Co-req: COMP.2010 Computing lll.",
        "output": {
            "prerequisites": [['COMP.1020'],],
            "corequisites": [['COMP.2010'],],
        }
    },
    
    # Case 6
    {
        "class": "COMP.2030",
        "input": "COMP.1020 Computing ll, and Co-req: COMP.2030L Assembly Language Lab.",
        "output": {
            "prerequisites": [['COMP.1020'],],
            "corequisites": [['COMP.2030L'],],
        }
    },
    
    # Case 7
    {
        "class": "COMP.2030R",
        "input": "COMP.1020 Computing ll, and Co-req: COMP.2030 Computer Organization and Assembly Language.",
        "output": {
            "prerequisites": [['COMP.1020'],],
            "corequisites": [['COMP.2030'],],
        }
    },
    
    # Case 8
    {
        "class": "COMP.2040",
        "input": "Pre-Req: COMP.2010 Computing III.",
        "output": {
            "prerequisites": [
                ['COMP.2010'],
            ],
            "corequisites": [],
        }
    },

    # Case 9
    {
        "class": "COMP.2300",
        "input": "Pre-Req: COMP.1020 Computing II.",
        "output": {
            "prerequisites": [['COMP.1020'],],
            "corequisites": [],
        }
    },

    # Case 10
    {
        "class": "COMP.2350",
        "input": "COMP.2300 Intro to Computer Security.",
        "output": {
            "prerequisites": [
                ['COMP.2300']
            ],
            "corequisites": [],
        }
    },

    # Case 11
    {
        "class": "COMP.3010",
        "input": "Pre-Req: COMP.2010 Computing III.",
        "output": {
            "prerequisites": [
                ['COMP.2010'],
            ],
            "corequisites": [],
        }
    },
    
    # Case 12
    {
        "class": "COMP.3040",
        "input": "Pre-Req: COMP 1020 Computing II, and MATH 3220 Discrete Structures II.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
                ['MATH.3220'],
            ],
            "corequisites": [],
        }
    },

    # Case 13
    {
        "class": "COMP.3050",
        "input": "Pre-Req: EECE 2650 Intro to Logic Design, COMP 1020 Computing II, COMP 2030 Comp Org & Assembly Lang or EECE 3170 Microprocessor Syst Des I.",
        "output": {
            "prerequisites": [
                ['EECE.2650'],
                ['COMP.1020'],
                ['COMP.2030', 'EECE.3170'],
            ],
            "corequisites": [],
        }
    },

    # Case 14
    {
        "class": "COMP.3080",
        "input": "Pre-Req: COMP.3050 Computer Architecture.",
        "output": {
            "prerequisites": [
                ['COMP.3050'],
            ],
            "corequisites": [],
        }
    },
    
    # Case 15
    {
        "class": "COMP.3085",
        "input": "COMP.2030 Assembly Language Programming.",
        "output": {
            "prerequisites": [
                ['COMP.2030']
            ],
            "corequisites": [],
        }
    },
    
    # Case 16
    {
        "class": "COMP.3090",
        "input": "Pre-Req: COMP.2040 Computing IV.",
        "output": {
            "prerequisites": [
                ['COMP.2040'],
            ],
            "corequisites": [],
        }
    },
    
    # Case 17
    {
        "class": "COMP.3300",
        "input": "COMP.2300 Intro to Computer Security.",
        "output": {
            "prerequisites": [
                ['COMP.2300']
            ],
            "corequisites": [],
        }
    },
    
    # Case 18 
    {
        "class": "COMP.3310",
        "input": "COMP.2300 Intro to Computer Security.",
        "output": {
            "prerequisites": [
                ['COMP.2300']
            ],
            "corequisites": [],
        }
    },

    # Case 19
    {
        "class": "COMP.3500",
        "input": "COMP.3050 Computer Architecture, or permission of instructor.",
        "output": {
            "prerequisites": [
                ['COMP.3050'],
            ],
            "corequisites": [],
        }
    },

    # Case 20
    {
        "class": "COMP.4040",
        "input": "Pre-Reqs: COMP 1020 Computing II, MATH 3220 Discrete Structures ll and MATH 3860 Probability  & Statistics I.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
                ['MATH.3220'],
                ['MATH.3860'],
            ],
            "corequisites": [],
        }
    },

    # Case 21
    {
        "class": "COMP.4130",
        "input": "COMP.2030 Assembly Language Programming, or Permission of Instructor.",
        "output": {
            "prerequisites": [
                ['COMP.2030'],
            ],
            "corequisites": [],
        }
    },

    # Case 22
    {
        "class": "COMP.4150",
        "input": "COMP.4220 Machine Learning.",
        "output": {
            "prerequisites": [
                ['COMP.4220']
            ],
            "corequisites": [],
        }
    },

    # Case 23
    {
        "class": "COMP.4200",
        "input": "Co-req: COMP 3010 Organization of Programming Languages and MATH 3860 Probability and Statistics I.",
        "output": {
            "prerequisites": [],
            "corequisites": [
                ['COMP.3010'],
                ['MATH.3860'],
            ],
        }
    },

    # Case 24
    {
        "class": "COMP.4210",
        "input": "Pre-Req: COMP 4200 Artificial Intelligence or COMP 3100 Database II.",
        "output": {
            "prerequisites": [
                ['COMP.4200', 'COMP.3100'],
            ],
            "corequisites": [],
        }
    },
    
    # Case 25
    {
        "class": "COMP.4220",
        "input": "Pre-Reqs: COMP 1020 Computing II, MATH 3220 Discrete Structures ll and MATH 3860 Probability  & Statistics I.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
                ['MATH.3220'],
                ['MATH.3860'],
            ],
            "corequisites": [],
        }
    },

    # Case 26
    {
        "class": "COMP.4230",
        "input": "COMP 1020 Computing II, MATH 1320 Calculus II, and MATH 3220 Discrete Structures II.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
                ['MATH.1320'],
                ['MATH.3220'],
            ],
            "corequisites": [],
        }
    },

    # Case 27
    {
        "class": "COMP.4240",
        "input": "COMP.2010 Computing III, and MATH.3860 Probability and Statistics I, or Permission of Instructor.(Students seeking this permission are expected to have knowledge of calculus, linear algebra, and Python).",
        "output": {
            "prerequisites": [
                ['COMP.2010'],
                ['MATH.3860'],
            ],
            "corequisites": [],
        }
    },

    # Case 28
    {
        "class": "COMP.4270",
        "input": "Pre-Req: COMP.2010 Computing III.",
        "output": {
            "prerequisites": [
                ['COMP.2010'],
            ],
            "corequisites": [],
        }
    },

    # Case 29
    {
        "class": "COMP.4290",
        "input": "COMP.1020 Computing II, and MATH.3860 Probability and Statistics I.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
                ['MATH.3860'],
            ],
            "corequisites": [],
        }
    },

    # Case 30
    {
        "class": "COMP.4500",
        "input": "COMP 1020 Computing II, or Co-req: EECE 3170 Microprocessor System Design I.",
        "output": {
            "prerequisites": [
                ['COMP.1020'],
            ],
            "corequisites": [
                ['EECE.3170'],
            ],
        }
    },

    # Case 31 
    {
        "class": "COMP.4510",
        "input": "COMP.1020 Computing II, or EECE.3170 Microprocessor System Design I and Co-req: MATH.3860 Probability and Statistics I.",
        "output": {
            "prerequisites": [
                ['COMP.1020', 'EECE.3170'],
            ],
            "corequisites": [
                ['MATH.3860'],
            ],
        }
    },
    
    # Case 32: BIOL.1220 - Has an anti-requirement
    # Case 33: CHEM.4750 - Has a requirement that uses "Math", which is a prefix.
    
]

# Test the function against the test cases
index = 0
for case in TEST_CASES:
    index += 1
    if get_course_requirements_dict(case['input']) != case['output']:
        print(f"Failed: Test {index} - {case['class']}")
        print("    - Input: ", case['input'])
        print("    - Expected: ", case['output'])
        print("    - Actual:   ", get_course_requirements_dict(case['input']))

print(f"Completed: {index} tests")