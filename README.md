# UML-NOW-CLI

A Command Line Interface for the University of Massachusetts Lowell's NOW Student Dashboard API.

**By using this, you agree to the terms and conditions set forth in the [University of Massachusetts Lowell API Terms of Service](https://www.uml.edu/api/Static/tos.html).**

Currently a work in progress.

## Installation

Install with pip:

```
$ pip3 install git+https://github.com/MartinMarwad/UML-NOW-CLI
```


## Basic Usage

The following commands will output the raw JSON data from the API.

### Search

```
$ python3 -m umlnow search --term=3210 --subjects=COM
```


```
$ python3 -m umlnow search --term=3210 --subjects=COMP --courseTitle=computing
```
