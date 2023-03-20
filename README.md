# AirBnB_clone - The Console

## Description

    This is the first step of the AirBnB project. The goal of this project is to
    recreat the AirBnB Website.The console is a command interpreter to manage
    objects for the AirBnb project.

## Requirements

    This project was tested on ubuntu 14.04 LTS using Python version 3.4.3

## Installation

    - Clone this repository
    - Access to AirBnb directory: cd AirBnb_clone
    - Run console (Interactive mode): ./console.py
    - Run (Non-interactive mode): echo "<command>" | ./console.py

## Using the console

    List of available commands:
    - quit and EOF: exits the console
        Example: (htbn) quit or (htbn) EOF
    - help: lists all available commands or the description for a command
        Example: (htbn) help or (htbn) ? or (htbn) help <command>
    - create: creates a new instance of a class
        Example: (hbtn) create <class>
            Available classes:
                - Amenity
                - BaseModel
                - City
                - Place
                - Review
                - State
                - User
    - show: prints the string representation of an instance
        Example: (hbtn) show <class> <id>
            The <id> could be readed from file.json or obtained from the command all
    - all: prints all string representation of all instances of a class or all instances
        Example: (htbn) all <class> or (htbn) all
    - update: updates an instance adding or updating an attribute (only once at time)
        Example: (htbn) update <class> <id> <attribute_name> <attribute_value>
    - destroy: deletes an instance
        Example: (htbn) destroy <class> <id>

## Content

| File | Description |
| --- | --- |
| [console.py](./console.py) | Console |

### Models directory

| File | Description |
| --- | --- |
| [\_\_init__.py](./models/__init__.py) | Init for models module. Links base_model and file_storage |
| [amenity.py](./models/amenity.py) | Module for Amenity class |
| [base_model.py](./models/base_model.py) | Module for BaseModel class. All other classes for models module inherit from this one |
| [city.py](./models/city.py) | Module for City class |
| [place.py](./models/place.py) | Module for Place class |
| [review.py](./models/review.py) | Module for Review class |
| [state.py](./models/state.py) | Module for State class |
| [user.py](./models/user.py) | Module for User class |

#### Models/Engine directory

| File | Description |
| --- | --- |
| [\_\_init__.py](./models/engine/__init__.py) | Init for engine module |
| [file_storage.py](./models/engine/file_storage.py) | Module for FileStorage class. Manages the storage of all objects |

### Tests directory

    Test suite fo this project

## Bugs

    No bugs at this time
