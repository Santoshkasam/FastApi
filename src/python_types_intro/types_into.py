# Str #

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
# print(get_full_name("chingi", "rao"))

# Str and Int #

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is " + f"{age}"
    return name_with_age

# print(get_name_with_age("santosh", 26))

# int, str, float, bool, bytes #

def get_items(item_a: int, item_b: str, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

# List #

def process_items_l(items: list[str]):
    for item in items:
        print(item.capitalize())

# process_items_l(["santosh", "is", "a", "good", "boy"])

        
# Tuple and Set #
def process_items_ts(tuple_items: tuple[int, str, int], set_items: set[bool|int]):
    return tuple_items, set_items

# print(process_items_ts((1, "numer", 2), {True, 2}))

# Dict #
def process_items_d(items: dict[str, int|str|bool]):
    return items
"""
print(process_items_d({
    "name": "Santosh",
    "age"   : 29,
    "married" : True
}))
"""

# None #

def process_items_ln(items: list[int|None]):
    for item in items:
        print("List contains None") if item == None else print("List not None")
    return items

# process_items_ln([None])

# Class #

class person:
    def __init__(self, name: str) -> None:
        self.name = name

one_person = person("Santosh")

def get_person_name(item: person):
    return item.name

# print(get_person_name(one_person))

# Pydantic Object #

from pydantic import BaseModel

class py_obj(BaseModel):
    name: str
    age: int|None = None
    married : bool

example = {
    "name": "Santosh",
    "age": 27,
    "married": True
} 

user = py_obj(**example)

print(user.age)