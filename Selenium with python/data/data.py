from dataclasses import dataclass

"""Generating of the random test data to create the person"""
@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None
        
"""Random of the color generation"""
@dataclass
class Color:
    color_name: list = None

"""Random of the date generation"""
@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
