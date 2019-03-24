import json


class Student:
    def __init__(self):
        self.name = input('Enter your name:')
        self.surname = input('Enter your surname:')
        self.age = int(input('Enter your age:'))

    def __str__(self):
        return f'Hello, my name is {self.name} {self.surname} and I\'m {self.age} years old!'

    def make_dict(self):
        return {'name': self.name, 'surname': self.surname, 'age': self.age}


def main():
    stud_1 = Student()
    stud_2 = Student()

    stud_1_json = json.dumps(stud_1.make_dict())
    stud_2_json = json.dumps(stud_2.make_dict())

    with open('students.inf', 'w') as ofile:
        json.dump((stud_1_json, stud_2_json), ofile)

    read_students = [json.loads(stud_2_json), json.loads(stud_1_json)]
    for stud in read_students:
        print(stud)


if __name__ == "__main__":
    main()
