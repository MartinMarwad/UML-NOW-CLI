# UML-NOW-CLI

A Command Line Interface for the University of Massachusetts Lowell's NOW Student Dashboard API.

**By using this, you agree to the terms and conditions set forth in the [University of Massachusetts Lowell API Terms of Service](https://www.uml.edu/api/Static/tos.html).**

Currently a work in progress.

## Installation

Install with pip:

```
$ pip3 install git+https://github.com/MartinMarwad/UML-NOW-CLI
```

If you would like to create a shortcut script, copy the `umlnow.sh` file into your user or system bin folder. 


## Basic Usage

The following commands can be used to output data:
- Course
- Search (Not implemented yet)
- API

### Course

This command utilizes web-scraping to extract information about a specific course from the UML Course Catalog website without using the API. **Note that this may produce inaccurate results if there is an error parsing the data.**

The `course` command expects a **course prefix** combined with a **course number**. Examples:
- `COMP.1010`
- `EECE.2020`
- `MATH.2310`

```
$ python3 -m umlnow course COMP.1010
```

```
{
    "name": "COMP.1010 Computing I (Formerly 91.101)",
    "url": "https://www.uml.edu/catalog/courses/COMP/1010/",
    "id": "008055",
    "description": "Introduction to computing environments: introduction to an integrated development environment; C, C++, or a similar language.  Linear data structures; arrays, records, and linked lists.  Abstract data types, stacks, and queues.  Simple sorting via exchange, selection, and insertion, basic file I/O. Programming style documentation and testing.  Ethical and social issues.  Effective Fall 2013, Co-req 91.103 Computing 1 Lab.",
    "credits": {
        "min": "3",
        "max": "3"
    },
    "requirements-text": "Co-req: COMP.1030L Comp. 1 Lab.",
    "requirements": {
        "pre-reqs": [],
        "pre-reqs-all-required": true,
        "co-reqs": [
            "COMP.1030L"
        ],
        "co-reqs-all-required": true
    }
}
```

It also allows getting specific data:
```
$ python3 -m umlnow course COMP.1010 --requirements
```
```
{
    "requirements": {
        "pre-reqs": [],
        "pre-reqs-all-required": true,
        "co-reqs": [
            "COMP.1030L"
        ],
        "co-reqs-all-required": true
    }
}
```


### Search

**Currently not implemented yet.**

An abstraction layer that combines features of the UML Now API and the UML Course Catalog API.  

Sub commands:
- classes
- professors
- majors
- minors
- degree-pathways/programs


### API

If you want to access the UML APIs directly, use the following commands. This is useful for testing or exploring what the APIs can provide. 


#### Search

Query the UML Now API directly. 

```
$ python3 -m umlnow api search --term=3210 --subjects=COMP
```

```
$ python3 -m umlnow api search --term=3210 --subjects=COMP --courseTitle=computing
```



#### Catalog

Query the UML Catalog API directly. 

```
$ python3 -m umlnow api catalog --pathCollege=SCI --pathDepartment=LCOMPSCI --pathType=undergraduate --SearchType=path
```


## Library

To use within your own Python program as a library, simply import the commands. 

```python
from umlnow import course, Search, API

# todo: add documentation
```
