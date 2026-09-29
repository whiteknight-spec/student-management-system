students = [
    {
        "name": "keerthi",
        "age": 23,
        "marks":[60,70,75]
    },
    {
        "name":"vasan",
        "age": 23,
        "marks":[62,65,79]
    },
    {
        "name":"lana",
        "age":20,
        "marks": [70,80,93]
    }
]
def display_students():
    for student in students:
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("marks:",student["marks"])

display_students()