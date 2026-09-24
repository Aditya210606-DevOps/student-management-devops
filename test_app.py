from app import add_student, find_student, get_students


def test_add_student():
    students_before = len(get_students())

    add_student(101, "Rahul", "AI & DS")

    assert len(get_students()) == students_before + 1


def test_find_student():
    add_student(102, "Amit", "Computer Engineering")

    student = find_student(102)

    assert student is not None
    assert student["name"] == "Amit"