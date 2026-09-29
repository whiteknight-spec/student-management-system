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

# display_students()

def add_student():
    name=input("enter the student name :")
    age=int(input("enter the student age :"))
    mark1=int(input("enter mark1 :"))
    mark2=int(input("enter mark2 :"))
    mark3=int(input("enter mark3 :"))
    marks=[mark1,mark2,mark3]
    student={
        "name":name,
        "age":age,
        "marks":marks
    }
    students.append(student)

add_student()

def search_student():
    name=input("enter the student name to search:")
    for student in students:
        if student["name"]==name:
            print("Name:",student["name"])
            print("Age:",student["age"])
            print("marks:",student["marks"])

search_student()
# display_students()