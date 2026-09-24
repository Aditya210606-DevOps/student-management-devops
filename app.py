students = []


def add_student(student_id, name, department):
    student = {
        "student_id": student_id,
        "name": name,
        "department": department
    }

    students.append(student)
    return student


def get_students():
    return students


def find_student(student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student

    return None


if __name__ == "__main__":
    add_student(1, "Greeshma", "AI & DS")
    print(get_students())

    import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None