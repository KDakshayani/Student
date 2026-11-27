def get_student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city
    }


if __name__ == "__main__":
    name = input("Enter student name: ")
    usn = input("Enter USN: ")
    college = input("Enter college name: ")
    city = input("Enter city: ")

    student = get_student_details(name, usn, college, city)

    print("\n--- Student Details ---")
    print("Name:", student["name"])
    print("USN:", student["usn"])
    print("College:", student["college"])
    print("City:", student["city"])
