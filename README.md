# Coding assignment answer - Food database
---
<a href="https://www.python.org/"><img alt="Python Version" src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

---
You will find in this repository code of the [Coding assignement][1].

Architecture of folder/file:
```
.
└── coding-assigment-answer
    ├── INSTRUCTIONS.md # Original README.md
    ├── README.md
    ├── datan # Folder with json to test class/method
    │   ├── expected_status.json
    │   ├── graph_build.json
    │   ├── graph_edits.json
    │   └── img_extract.json
    ├── src # Main folder for classes
    │   ├── __init__.py # Init file
    │   ├── database.py # Contain class Database with the requested methods
    │   ├── directed_graph.py # Contain DirectedGraph and Node class, two class to build graph for the Database
    │   └── utils.py # Contain Enum status and utils functions
    └── test # Main folder to test preceding classes
        ├── __init__.py # Init file
        ├── evaluation_test.py # Contains 3 methods to evaluate the classes and methods written
        └── test.py # Unit test on some methods
```

## Prerequisite

Required packages are in `requirements.txt`, use following command to install them:
```
pip install -r requirements.txt
```

## Evaluate

To evaluate the scripts with [test json data][2] and handmade database run:
```
python test/evaluation_test.py
```
It should return the following if everything works well:
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.021s

OK
```

## References

- FoodVisor Coding Assigment : https://github.com/Foodvisor/coding-assignment

[1]: https://github.com/Foodvisor/coding-assignment
[2]: https://github.com/Foodvisor/coding-assignment/releases/tag/v0.1.0