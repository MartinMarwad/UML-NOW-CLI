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
- Search (in progress)
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

An abstraction layer that combines features of the UML Now API and the UML Course Catalog API.

Sub commands:

- courses
- professors
- programs
  - majors
  - minors
- pathways


#### Search: Courses

Provides the ability to query for all courses offered by UML.


To see all courses offered by UML:

```bash
$ python3 -m umlnow search courses
```


To see all courses offered by a department prefix

```bash
$ python3 -m umlnow search courses --departments=COMP
```


##### Using the `--parse` flag

By default, the search command just scrapes and returns results from the UML Course Catalog search page: https://www.uml.edu/catalog/advance-search.aspx.

The data provided is only the course prefix, name, and id. If you want to get all the details from a course like from the `umlnow course` command, you can do so by including the `--parse` flag.

**However, this requests a new webpage from the UML website for every course found. Using this flag on a large queryset (like all the courses) will take a long time to run and could break the terms of the UML website. Use this flag at your own risk.**


#### Search: Professors

***Not Implmented***

Provides the ability to query for all professors teaching courses at UML.


#### Search: Programs

***Not Implmented***

Provides the ability to query for all programs offered at UML.


#### Search: Pathways

***Not Implmented***

Provides the ability to query for degree-pathways offered by UML.


### API

***Needs Documentation***

If you want to access the UML APIs directly, use the following commands. This is useful for testing or exploring what the APIs can provide.


#### API: Search

Query the UML Now API directly.

```
$ python3 -m umlnow api search --term=3210 --subjects=COMP
```

```
$ python3 -m umlnow api search --term=3210 --subjects=COMP --courseTitle=computing
```



#### API: Catalog

Query the UML Catalog API directly.

```
$ python3 -m umlnow api catalog --pathCollege=SCI --pathDepartment=LCOMPSCI --pathType=undergraduate --SearchType=path
```



## Library

***Needs Documentation***

To use within your own Python program as a library, simply import the commands.

```python
from umlnow import course, Search, API

# todo: add documentation
```
