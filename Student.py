import sys
def get_student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city
    }


if __name__ == "__main__":
    name=sys.argv[1]
    usn=sys.argv[2]
    college=sys.argv[3]
    city=sys.argv[4]

    student = get_student_details(name, usn, college, city)

    print("\n--- Student Details ---")
    print("Name:", name)
    print("USN:", usn)
    print("College:", college)
    print("City:", city)
