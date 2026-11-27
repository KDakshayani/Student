from Student import get_student_details


def test_student_name():
    student = get_student_details(
        "Rahul", "01FE25BCA001", "ABC College", "Hubballi"
    )
    assert student["name"] == "Rahul"


def test_student_usn():
    student = get_student_details(
        "Rahul", "01FE25BCA001", "ABC College", "Hubballi"
    )
    assert student["usn"] == "01FE25BCA001"


def test_student_college():
    student = get_student_details(
        "Rahul", "01FE25BCA001", "ABC College", "Hubballi"
    )
    assert student["college"] == "ABC College"

def test_student_email():
    student = get_student_details(
        "Rahul", "01FE25BCA001", "ABC College",
        "Hubballi", "rahul@example.com"
    )
    assert student["email"] == "rahul@example.com"


def test_student_city():
    student = get_student_details(
        "Rahul", "01FE25BCA001", "ABC College", "Hubballi"
    )
    assert student["city"] == "Hubballi"
