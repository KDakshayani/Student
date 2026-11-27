from Student import get_student_details

def test_get_student_details():
    student = get_student_details(
        "Rahul",
        "4XX23CS001",
        "ABC College",
        "rahul@gmail.com",
        "Bangalore"
    )

    assert student["name"] == "Rahul"
    assert student["usn"] == "4XX23CS001"
    assert student["college"] == "ABC College"
    assert student["email"] == "rahul@gmail.com"
    assert student["city"] == "Bangalore"